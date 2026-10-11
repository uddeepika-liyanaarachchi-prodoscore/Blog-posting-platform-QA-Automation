import os
import sys
import shutil
import subprocess
from datetime import datetime


PRINT_BUTTON_SNIPPET = """
<!-- INJECTED QA PRINT TOOLBAR & PRINT-FRIENDLY CSS -->
<style id="qa-print-styles">
 .qa-toolbar {
   position: fixed;
   top: 15px;
   right: 25px;
   z-index: 999999;
   display: flex;
   gap: 10px;
   align-items: center;
   background: rgba(255, 255, 255, 0.95);
   padding: 6px 12px;
   border-radius: 8px;
   box-shadow: 0 4px 15px rgba(0, 0, 0, 0.15);
   border: 1px solid #e2e8f0;
 }
 .qa-print-btn {
   background: linear-gradient(135deg, #2563eb, #1d4ed8);
   color: #ffffff !important;
   border: none;
   padding: 8px 16px;
   font-size: 13px;
   font-weight: 600;
   border-radius: 6px;
   cursor: pointer;
   display: inline-flex;
   align-items: center;
   gap: 7px;
   font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
   box-shadow: 0 2px 6px rgba(37, 99, 235, 0.3);
   transition: all 0.2s ease;
   text-decoration: none;
 }
 .qa-print-btn:hover {
   background: linear-gradient(135deg, #1d4ed8, #1e40af);
   transform: translateY(-1px);
   box-shadow: 0 4px 10px rgba(37, 99, 235, 0.45);
 }
 .qa-print-btn:active {
   transform: translateY(0);
 }
 .qa-badge-history {
   font-size: 11px;
   color: #64748b;
   font-family: monospace;
   font-weight: 500;
 }
 @media print {
   .qa-toolbar, .no-print {
     display: none !important;
   }
   body {
     -webkit-print-color-adjust: exact !important;
     print-color-adjust: exact !important;
     color: #000 !important;
   }
   table {
     page-break-inside: auto;
   }
   tr {
     page-break-inside: avoid;
     page-break-after: auto;
   }
 }
</style>
<div class="qa-toolbar no-print">
 <span class="qa-badge-history">REPORT_TIMESTAMP_PLACEHOLDER</span>
 <button class="qa-print-btn" onclick="window.print()" title="Print report or save as PDF">
   <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
     <polyline points="6 9 6 2 18 2 18 9"></polyline>
     <path d="M6 18H4a2 2 0 0 1-2-2v-5a2 2 0 0 1 2-2h16a2 2 0 0 1 2 2v5a2 2 0 0 1-2 2h-2"></path>
     <rect x="6" y="14" width="12" height="8"></rect>
   </svg>
   Print / Save as PDF
 </button>
</div>
"""


def inject_print_toolbar(file_path: str, timestamp_str: str):
   """Injects print button and print styling into the HTML report"""
   try:
       with open(file_path, "r", encoding="utf-8") as f:
           content = f.read()


       snippet = PRINT_BUTTON_SNIPPET.replace("REPORT_TIMESTAMP_PLACEHOLDER", timestamp_str)


       if "</body>" in content:
           new_content = content.replace("</body>", f"{snippet}\n</body>")
       else:
           new_content = content + snippet


       with open(file_path, "w", encoding="utf-8") as f:
           f.write(new_content)
   except Exception as e:
       print(f"Warning: Could not inject print button: {e}")


def main():
   project_dir = os.path.dirname(os.path.abspath(__file__))
   os.chdir(project_dir)


   reports_dir = os.path.join(project_dir, "reports")
   archive_dir = os.path.join(reports_dir, "archive")
   os.makedirs(archive_dir, exist_ok=True)


   timestamp_str = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
   latest_report = os.path.join(reports_dir, "test_report.html")
   archived_report = os.path.join(archive_dir, f"test_report_{timestamp_str}.html")


   print("=" * 70)
   print("  🚀 Blog Poster Frontend QA Automation (Selenium + UV + Pytest)")
   print(f"  Execution Time: {timestamp_str}")
   print("=" * 70)


   # Use uv run pytest to execute test suite dynamically
   cmd = [
       "uv", "run", "pytest",
       "tests",
       "-v",
       f"--html={latest_report}",
       "--self-contained-html",
   ]


   if len(sys.argv) > 1:
       cmd.extend(sys.argv[1:])


   env = os.environ.copy()
   local_bin = os.path.expanduser("~/.local/bin")
   if local_bin not in env.get("PATH", ""):
       env["PATH"] = f"{local_bin}:{env.get('PATH', '')}"


   result = subprocess.run(cmd, env=env)


   # Inject the Print / PDF toolbar into the generated report
   if os.path.exists(latest_report):
       inject_print_toolbar(latest_report, timestamp_str)
       # Create an archived copy with timestamp so previous reports are NEVER lost
       shutil.copy2(latest_report, archived_report)


   # Count historical reports
   archived_count = len([f for f in os.listdir(archive_dir) if f.endswith(".html")])


   print("\n" + "=" * 70)
   if result.returncode == 0:
       print("  ✅ All Frontend tests passed successfully!")
   else:
       print(f"  ⚠️ Test execution completed with exit code: {result.returncode}")
   print(f"  📊 Latest Report: file://{latest_report}")
   print(f"  📁 Archived Report: file://{archived_report}")
   print(f"  🗄️ Total Historical Runs Saved in reports/archive/: {archived_count}")
   print(f"  🖨️ Interactive 'Print / Save as PDF' button added to report!")
   print("=" * 70)


   return result.returncode


if __name__ == "__main__":
   sys.exit(main())



