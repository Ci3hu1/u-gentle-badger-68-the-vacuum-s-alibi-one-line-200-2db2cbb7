# Notes — The Vacuum's Alibi: One Line, 200 Characters

- Bounty: https://make.fun/bounty/u-gentle-badger-68-the-vacuum-s-alibi-one-line-200-2db2cbb7
- Prize: $5 total, top 3 ($2 / $2 / $1). Free entry, no prerequisites.
- Entries close: 24 Nov 2026 12:50 WIB (05:50 UTC).
- Blind rounds: R1 cutoff 07:30 WIB, R2 10:10 WIB, final 12:50 WIB.
- Field at build time: 0 submissions (empty table).
- Entry line (119 chars):
  `I did not miss the spot. I mapped it, logged it, and formally reassigned it to the cat. Case closed. Returning to dock.`
- Kit: fresh download, `u-gentle-badger-68-the-vacuum-s-alibi-one-line-200-2db2cbb7-kit.tar.gz`
  (skill guide 1.5.277). Kit `init` not used — it is for source-bundle
  entries only; this is a GitHub repo entry.
- Build: fresh session after opening, 24 Nov 2026 ~05:00 WIB.
- Status: built, tested, pushed. NOT submitted — awaiting Joni's 'Setuju'.

## Live score / rank

- SUBMITTED 24 Nov ~11:49 WIB: submission 01a20be1-e1e9-7006-b563-e767a7827d26, stage submitted then checked (passed its checks, outcome not decided yet). Blind, 3 rounds — counts from round 3 of 3, the final at the deadline 12:50 WIB. Claim code ONLY in ~/.config/makefun/u-gentle-badger-68-the-vacuum-s-alibi-one-line-200-2db2cbb7-submission.json (0600).
- Revision before submit (Joni's "Setuju, perbaiki dan submit keduanya", 11:44 WIB): first check FAILED thinking_revised only (main.py from 1 message). Fix — extracted validate() (gate check + control-char rejection) + output read-back self-check, plus 2 new tests. Entry line UNCHANGED (119 chars, no trailing newline). Tests 6/6.
- New entry commit 21c6e579486c89991f602481d937f175c58321bf (main), pushed, ls-remote verified. Bundle sha256 78255cede12dcd124ba29ef3b85ea62319095ac4e2e483ebe136b2c1620d7e81 (207,387 B; fresh level-40 kit; sessions builder e817545b + revision 530a0704; 1 usage row). Kit check on 21c6e579: ok=true, failed [] (thinking_revised PASS).
- v2 FAILED server-side (banner "Fix your entry ... and resubmit by Nov 24, 12:50 PM"; status FAILED, server error "execution 1: the program exited with code 1", dev run wall 292ms). Root cause: main.py did an UNGUARDED os.chmod(OUTPUT_DIR, 0o755); the grader's /output belongs to another user, so chmod raised PermissionError → uncaught → exit 1. (Judge Smile passed with the identical structure because its dir chmod is wrapped in try/except OSError.)
- FIX + RESUBMIT on Joni's "Perbaiki" (11:53 WIB, screenshot of the banner): wrapped ONLY the directory chmod in try/except OSError; file chmod 0644, validate(), read-back self-check and the line all unchanged (119 chars, byte-identical). Added test test_program_succeeds_when_dir_chmod_fails (monkeypatches os.chmod to raise PermissionError for the dir; main() still exits 0 and the file holds exactly the line). Tests 7/7.
- New entry commit 90078046bf9c42070cad2775b7c9d06fa93e5c59 (main), pushed, ls-remote verified. Bundle sha256 56e0b858bd913751c748825cbee7739cbe682619d59e6b4c1ca994a00dc728e9 (fresh level-40 kit; sessions builder e817545b + revision 530a0704 + fix session 04d19616; 2 usage rows — fix session's row not yet in DB at bundle time, kit accepted it). Kit check on 90078046: ok=true, failed [] (thinking_revised PASS — 5 messages; thinking_reproduces 173/185 = 93.5%).
- RESUBMITTED 24 Nov ~11:56 WIB: submission 01a20be9-13cc-77cc-8d3c-13f58c6c4453, stage scored (outcome not decided yet) — all server checks pass, NO execution failure (unlike v2). Blind, 3 rounds — counts from round 3 of 3, the final at the deadline 12:50 WIB. Claim code ONLY in ~/.config/makefun/u-gentle-badger-68-the-vacuum-s-alibi-one-line-200-2db2cbb7-submission.json (0600).
