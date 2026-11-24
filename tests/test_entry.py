"""Tests for the Vacuum's Alibi entry."""

import os
import subprocess
import sys
import tempfile
import unittest
from unittest import mock

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, REPO)

import main  # noqa: E402


class TestEntryLine(unittest.TestCase):
    def test_validate_accepts_the_line(self):
        """validate() passes the approved line through unchanged."""
        self.assertEqual(main.validate(main.LINE), main.LINE)

    def test_validate_rejects_bad_lines(self):
        """validate() rejects blank, over-long, multi-line and control-char lines."""
        for bad in ("", "   ", "x" * 201, "one\ntwo", "a\rb", "tab\there"):
            with self.assertRaises(ValueError, msg=repr(bad)):
                main.validate(bad)

    def test_line_length(self):
        self.assertGreaterEqual(len(main.LINE), 1)
        self.assertLessEqual(len(main.LINE), 200)

    def test_line_non_blank_single_line(self):
        self.assertTrue(main.LINE.strip())
        self.assertNotIn("\n", main.LINE)
        self.assertNotIn("\r", main.LINE)

    def test_line_is_utf8(self):
        main.LINE.encode("utf-8")

    def test_program_writes_exact_output(self):
        with tempfile.TemporaryDirectory() as tmp:
            env = dict(os.environ, VACUUM_OUTPUT_DIR=tmp)
            result = subprocess.run(
                [sys.executable, os.path.join(REPO, "main.py")],
                env=env, capture_output=True, text=True,
            )
            self.assertEqual(result.returncode, 0, result.stderr)
            path = os.path.join(tmp, "entry.txt")
            with open(path, encoding="utf-8") as f:
                content = f.read()
            self.assertEqual(content, main.LINE)
            self.assertEqual(len(content), len(main.LINE))
            self.assertTrue(1 <= len(content) <= 200)
            self.assertTrue(content.strip())
            # Outputs must be readable by the grader's collector user.
            self.assertEqual(oct(os.stat(path).st_mode & 0o777), "0o644")

    def test_program_succeeds_when_dir_chmod_fails(self):
        """main() still succeeds when the output directory cannot be
        chmodded — the grader's /output belongs to another user, and the
        unguarded directory chmod crashed the v2 submission (exit 1)."""
        with tempfile.TemporaryDirectory() as tmp:
            out_file = os.path.join(tmp, "entry.txt")
            orig_dir, orig_file = main.OUTPUT_DIR, main.OUTPUT_FILE
            main.OUTPUT_DIR, main.OUTPUT_FILE = tmp, out_file
            real_chmod = os.chmod

            def fake_chmod(path, mode):
                if os.path.abspath(path) == os.path.abspath(tmp):
                    raise PermissionError("directory owned by another user")
                return real_chmod(path, mode)

            try:
                with mock.patch.object(os, "chmod", fake_chmod):
                    main.main()
            finally:
                main.OUTPUT_DIR, main.OUTPUT_FILE = orig_dir, orig_file
            with open(out_file, encoding="utf-8") as f:
                self.assertEqual(f.read(), main.LINE)


if __name__ == "__main__":
    unittest.main()
