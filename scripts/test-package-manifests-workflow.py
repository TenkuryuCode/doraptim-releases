"""Exercise the workflow's release gate without contacting GitHub."""

import os
from pathlib import Path
import subprocess
from tempfile import TemporaryDirectory
import textwrap
import unittest


WORKFLOW = Path(__file__).resolve().parents[1] / ".github/workflows/package-manifests.yml"


class LatestReleaseGate(unittest.TestCase):
    def test_release_event_excludes_prereleases(self):
        trigger = WORKFLOW.read_text().split("permissions:", 1)[0]
        self.assertIn("types: [released]", trigger)
        condition = next(line for line in WORKFLOW.read_text().splitlines() if "if: github.event_name" in line)
        self.assertIn("github.event.release.draft == false", condition)
        self.assertIn("github.event.release.prerelease == false", condition)

    def test_manifest_writes_require_latest_before_generation_and_push(self):
        source = WORKFLOW.read_text().split("        run: |\n", 1)[1]
        # Use the actual workflow steps with a fake CLI and signed output.
        for tag, latest, final, expected_calls, expected_code in (
            ("v1.0.0-beta.1", "v1.0.0", "v1.0.0", "latest\n", 0),
            ("v1.0.0", "v1.1.0", "v1.1.0", "latest\n", 0),
            ("v1.0.0", "ERROR", "ERROR", "latest\n", 1),
            ("v1.0.0", "v1.0.0", "v1.1.0", "latest\ndownload\nlatest\n", 0),
            ("v1.0.0", "v1.0.0", "v1.0.0", "latest\ndownload\nlatest\npush\n", 0),
        ):
            with self.subTest(tag=tag, latest=latest, final=final), TemporaryDirectory() as temp:
                root = Path(temp)
                (root / "scripts").mkdir()
                (root / "scripts/latest-links.py").touch()
                (root / "scripts/package-manifests.sh").write_text(
                    'mkdir -p "$3/Formula" "$3/bucket" "$3/winget"\n'
                    'touch "$3/latest.json" "$3/latest.json.sig"\n'
                )
                gh = root / "gh"
                gh.write_text(
                    '#!/bin/sh\n'
                    'case "$1 $2" in\n'
                    '  "api repos/test/release/releases/latest")\n'
                    '    value=$FIRST; [ ! -e checked ] || value=$FINAL\n'
                    '    touch checked; echo latest >> calls\n'
                    '    [ "$value" != ERROR ] || exit 1; echo "$value";;\n'
                    '  "release download") echo download >> calls; mkdir -p "$RUNNER_TEMP/release";;\n'
                    '  "release view") echo notes;;\n'
                    '  *) exit 2;;\n'
                    'esac\n'
                )
                git = root / "git"
                git.write_text(
                    '#!/bin/sh\n'
                    'case "$1" in\n'
                    '  diff) exit 1;;\n'
                    '  push) echo push >> calls;;\n'
                    'esac\n'
                )
                for command in (gh, git):
                    command.chmod(0o755)
                result = subprocess.run(
                    ["bash", "-eo", "pipefail", "-c", textwrap.dedent(source)],
                    cwd=root,
                    env={
                        **os.environ,
                        "PATH": str(root) + os.pathsep + os.environ["PATH"],
                        "TAG": tag,
                        "FIRST": latest,
                        "FINAL": final,
                        "GITHUB_REPOSITORY": "test/release",
                        "RUNNER_TEMP": temp,
                        "DORAPTIM_UPDATE_SIGNING_KEY": "test-key",
                    },
                    capture_output=True,
                    text=True,
                )
                self.assertEqual(result.returncode, expected_code, result.stdout + result.stderr)
                self.assertEqual((root / "calls").read_text(), expected_calls)


if __name__ == "__main__":
    unittest.main()
