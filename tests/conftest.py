import os
import shutil
from datetime import datetime
import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from config import Config
from server import SimpleFEServer

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

def inject_styles_and_toolbar(report_path: str, timestamp_str: str) -> None:
    if not os.path.exists(report_path):
        return

    with open(report_path, "r", encoding="utf-8") as f:
        html_content = f.read()

    customized_snippet = PRINT_AND_CSS_SNIPPET.replace("REPORT_TIMESTAMP_PLACEHOLDER", timestamp_str)

    if "</head>" in html_content:
        html_content = html_content.replace("</head>", f"{customized_snippet}\n</head>")
    elif "</body>" in html_content:
        html_content = html_content.replace("</body>", f"{customized_snippet}\n</body>")
    else:
        html_content += customized_snippet

    with open(report_path, "w", encoding="utf-8") as f:
        f.write(html_content)

@pytest.fixture(scope="session")
def live_server_url():
    server = SimpleFEServer()
    url = server.start()
    yield url
    server.stop()

@pytest.fixture
def driver():
    browser = Config.BROWSER

    if browser == "firefox":
        options = FirefoxOptions()
        if Config.HEADLESS:
            options.add_argument("-headless")
        options.add_argument("--width=1920")
        options.add_argument("--height=1080")
        options.set_preference("dom.webnotifications.enabled", False)

        gecko_path = shutil.which("geckodriver") or "/snap/bin/geckodriver"
        if os.path.exists(gecko_path):
            service = FirefoxService(executable_path=gecko_path)
            drv = webdriver.Firefox(service=service, options=options)
        else:
            drv = webdriver.Firefox(options=options)

    elif browser == "chrome":
        options = ChromeOptions()
        if Config.HEADLESS:
            options.add_argument("--headless=new")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        drv = webdriver.Chrome(options=options)
    else:
        raise ValueError(f"Unsupported browser: {browser}")

    drv.implicitly_wait(Config.EXPLICIT_WAIT)
    yield drv
    drv.quit()

def pytest_terminal_summary(terminalreporter, exitstatus, config):
    root_dir = str(config.rootpath)
    reports_dir = os.path.join(root_dir, "reports")
    archive_dir = os.path.join(reports_dir, "archive")
    os.makedirs(archive_dir, exist_ok=True)

    latest_report = os.path.join(reports_dir, "test_report.html")

    if os.path.exists(latest_report):
        timestamp_str = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        inject_styles_and_toolbar(latest_report, timestamp_str)

        archived_report = os.path.join(archive_dir, f"test_report_{timestamp_str}.html")
        shutil.copy2(latest_report, archived_report)

        terminalreporter.write_sep("=", "CUSTOM QA REPORT READY")
        terminalreporter.write_line(f"Latest Report : file://{latest_report}")
        terminalreporter.write_line(f"Archived Run  : file://{archived_report}")