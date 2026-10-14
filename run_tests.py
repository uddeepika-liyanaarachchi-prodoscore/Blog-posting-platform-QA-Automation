import os
import sys
import pytest


def main() -> int:
    # Ensure execution happens from project root directory
    project_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(project_dir)

    # Ensure reports directory exists before running tests
    os.makedirs(os.path.join(project_dir, "reports"), exist_ok=True)

    latest_report = os.path.join("reports", "test_report.html")

    # Base pytest arguments
    cmd_args = [
        "tests",
        "-v",
        f"--html={latest_report}",
        "--self-contained-html",
    ]

    # Append any custom CLI flags passed to run_tests.py (e.g. -k test_login)
    if len(sys.argv) > 1:
        cmd_args.extend(sys.argv[1:])

    # Run pytest directly in-process without subprocess or OS path injection
    return pytest.main(cmd_args)


if __name__ == "__main__":
    sys.exit(main())

