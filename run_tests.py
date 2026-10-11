import os
import sys
import shutil
import subprocess
from datetime import datetime

PRINT_AND_CSS_SNIPPET = """
<style id="qa-dashboard-modern-styles">
 @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');


 body {
   font-family: 'Inter', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif !important;
   background-color: #f8fafc !important;
   color: #1e293b !important;
   font-size: 13px !important;
   margin: 0 !important;
   padding: 30px 45px !important;
   line-height: 1.6 !important;
 }


 h1 {
   font-size: 24px !important;
   font-weight: 700 !important;
   color: #0f172a !important;
   margin-bottom: 25px !important;
   display: flex !important;
   align-items: center !important;
   gap: 12px !important;
   letter-spacing: -0.5px !important;
 }


 h2 {
   font-size: 15px !important;
   font-weight: 600 !important;
   color: #475569 !important;
   margin-top: 28px !important;
   margin-bottom: 14px !important;
   text-transform: uppercase !important;
   letter-spacing: 0.5px !important;
 }


 p {
   color: #475569 !important;
 }


 /* Environment & Results Tables */
 table#environment, table#results-table {
   width: 100% !important;
   background: #ffffff !important;
   border-radius: 10px !important;
   border: 1px solid #e2e8f0 !important;
   box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05), 0 2px 4px -1px rgba(0, 0, 0, 0.03) !important;
   border-collapse: separate !important;
   border-spacing: 0 !important;
   overflow: hidden !important;
   margin-bottom: 30px !important;
 }


 th {
   background: #f1f5f9 !important;
   color: #334155 !important;
   font-weight: 600 !important;
   text-transform: uppercase !important;
   font-size: 11px !important;
   letter-spacing: 0.6px !important;
   padding: 13px 18px !important;
   border-bottom: 1px solid #cbd5e1 !important;
 }


 td {
   padding: 13px 18px !important;
   border-bottom: 1px solid #f1f5f9 !important;
   color: #334155 !important;
   vertical-align: middle !important;
 }


 tr:last-child td {
   border-bottom: none !important;
 }


 tbody tr:hover {
   background-color: #f8fafc !important;
 }


 /* Status Badges */
 span.passed, .col-result.passed {
   background-color: #dcfce7 !important;
   color: #15803d !important;
   padding: 4px 12px !important;
   border-radius: 9999px !important;
   font-weight: 600 !important;
   font-size: 11px !important;
   display: inline-block !important;
   border: 1px solid #bbf7d0 !important;
 }


 span.failed, .col-result.failed {
   background-color: #fee2e2 !important;
   color: #b91c1c !important;
   padding: 4px 12px !important;
   border-radius: 9999px !important;
   font-weight: 600 !important;
   font-size: 11px !important;
   display: inline-block !important;
   border: 1px solid #fecaca !important;
 }


 span.skipped, .col-result.skipped {
   background-color: #fef3c7 !important;
   color: #b45309 !important;
   padding: 4px 12px !important;
   border-radius: 9999px !important;
   font-weight: 600 !important;
   font-size: 11px !important;
   display: inline-block !important;
   border: 1px solid #fde68a !important;
 }


 /* Filters */
 div.filters {
   background: #ffffff !important;
   padding: 14px 20px !important;
   border-radius: 10px !important;
   border: 1px solid #e2e8f0 !important;
   box-shadow: 0 2px 4px rgba(0,0,0,0.03) !important;
   margin-bottom: 25px !important;
   display: flex !important;
   gap: 15px !important;
   align-items: center !important;
   font-weight: 500 !important;
 }


 /* Floating Print Toolbar */
 .qa-toolbar {
   position: fixed;
   top: 15px;
   right: 30px;
   z-index: 999999;
   display: flex;
   gap: 12px;
   align-items: center;
   background: rgba(255, 255, 255, 0.95);
   backdrop-filter: blur(8px);
   padding: 7px 14px;
   border-radius: 10px;
   box-shadow: 0 10px 25px rgba(0, 0, 0, 0.1), 0 2px 6px rgba(0, 0, 0, 0.05);
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
   font-family: inherit;
   box-shadow: 0 2px 6px rgba(37, 99, 235, 0.3);
   transition: all 0.2s ease;
 }


 .qa-print-btn:hover {
   background: linear-gradient(135deg, #1d4ed8, #1e40af);
   transform: translateY(-1px);
   box-shadow: 0 4px 10px rgba(37, 99, 235, 0.45);
 }


 .qa-badge-history {
   font-size: 11px;
   color: #64748b;
   font-family: monospace;
   font-weight: 600;
   background: #f1f5f9;
   padding: 4px 8px;
   border-radius: 4px;
 }


 @media print {
   .qa-toolbar, .no-print, div.filters {
     display: none !important;
   }
   body {
     background: #ffffff !important;
     -webkit-print-color-adjust: exact !important;
     print-color-adjust: exact !important;
     padding: 0 !important;
   }
   table#environment, table#results-table {
     box-shadow: none !important;
     border: 1px solid #ccc !important;
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


def inject_styles_and_toolbar(file_path: str, timestamp_str: str):
   """Injects modern styles, print button, and print CSS into the generated HTML report"""
   try:
       with open(file_path, "r", encoding="utf-8") as f:
           content = f.read()


       snippet = PRINT_AND_CSS_SNIPPET.replace("REPORT_TIMESTAMP_PLACEHOLDER", timestamp_str)


       if "</head>" in content:
           new_content = content.replace("</head>", f"{snippet}\n</head>")
       elif "</body>" in content:
           new_content = content.replace("</body>", f"{snippet}\n</body>")
       else:
           new_content = content + snippet


       with open(file_path, "w", encoding="utf-8") as f:
           f.write(new_content)
   except Exception as e:
       print(f"Warning: Could not inject styles: {e}")


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


   # Inject the Modern CSS + Print/PDF Toolbar into the freshly generated report
   if os.path.exists(latest_report):
       inject_styles_and_toolbar(latest_report, timestamp_str)
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
   print(f"  🎨 Modern CSS & 'Print / Save as PDF' Toolbar embedded!")
   print("=" * 70)


   return result.returncode


if __name__ == "__main__":
   sys.exit(main())



