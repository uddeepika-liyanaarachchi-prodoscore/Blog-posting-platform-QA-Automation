
import os
import sys
import subprocess


def main():
   project_dir = os.path.dirname(os.path.abspath(__file__))
   os.chdir(project_dir)


   reports_dir = os.path.join(project_dir, "reports")
   os.makedirs(reports_dir, exist_ok=True)
   report_file = os.path.join(reports_dir, "test_report.html")


   print("=" * 70)
   print("  🚀 Blog Poster Frontend QA Automation (Selenium + UV + Pytest)")
   print(f"  Report Target: {report_file}")
   print("=" * 70)


   # Use uv run pytest to execute the test suite dynamically
   cmd = [
       "uv", "run", "pytest",
       "tests",
       "-v",
       f"--html={report_file}",
       "--self-contained-html",
   ]


   # If extra arguments were passed from CLI, forward them to pytest
   if len(sys.argv) > 1:
       cmd.extend(sys.argv[1:])


   # Ensure uv is in PATH
   env = os.environ.copy()
   local_bin = os.path.expanduser("~/.local/bin")
   if local_bin not in env.get("PATH", ""):
       env["PATH"] = f"{local_bin}:{env.get('PATH', '')}"


   result = subprocess.run(cmd, env=env)


   print("\n" + "=" * 70)
   if result.returncode == 0:
       print("  ✅ All Frontend tests passed successfully!")
   else:
       print(f"  ⚠️ Test execution completed with exit code: {result.returncode}")
   print(f"  📊 Dynamic HTML Test Report generated at:\n     file://{report_file}")
   print("=" * 70)


   return result.returncode


if __name__ == "__main__":
   sys.exit(main())



