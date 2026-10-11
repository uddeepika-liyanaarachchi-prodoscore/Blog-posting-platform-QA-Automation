# 🧪 Blog Poster Frontend QA Automation


A simple, lightweight, and modern **Frontend Functional QA Automation** project for the **Blog Posting Platform**, built with **Selenium WebDriver**, **Python**, **UV package manager**, and **Pytest** following the **Page Object Model (POM)** design pattern.


---


## 🌟 Key Features


- **Frontend Focused**: Specifically built and tailored for the Blog Posting Platform Frontend (`app/index.html`, CSS, and JavaScript modules).
- **Package Management via `uv`**: Ultra-fast dependency resolution and virtual environment management via Astral's `uv`.
- **Page Object Model (POM)**: Clean, maintainable separation of UI locators, DOM interactions, and test assertions (`pages/`).
- **Dynamic HTML Test Reports**: Generates interactive, dynamic HTML execution reports on every run using `pytest-html` in `reports/test_report.html`.
- **Zero Mock Overengineering**: Directly tests real frontend DOM elements, native HTML5 validations, view switching, modal controls, and `localStorage` session state.
- **Headless Firefox Execution**: Runs automatically in headless mode via `geckodriver`.


---


## 📁 Project Structure


```
blogposter-qa-automation/
├── pyproject.toml              # UV Project Configuration & Dependencies
├── uv.lock                     # UV Dependency Lockfile
├── .venv/                      # Virtual environment managed by UV
├── config.py                   # Global configuration (URL, browser, timeouts)
├── server.py                   # Automatic local static server for Frontend files
├── pages/                      # Page Object Classes (POM)
│   ├── base_page.py            # Core Selenium wait, click, type & script helpers
│   ├── navbar.py               # Navbar buttons (Home, Login, Dashboard)
│   ├── login_page.py           # Login view interactions & validations
│   ├── register_page.py        # Sign-up view interactions
│   ├── dashboard_page.py       # My View (Dashboard, heading, logout)
│   └── explore_page.py         # Main View & Blog Post details modal
├── tests/                      # Automated Test Suites
│   ├── conftest.py             # Fixtures for driver & server lifecycle
│   ├── test_navigation.py      # TC_NAV_01 to TC_NAV_04
│   ├── test_login_ui.py        # TC_LOGIN_01 to TC_LOGIN_04
│   ├── test_register_ui.py     # TC_REG_01 to TC_REG_03
│   ├── test_dashboard_ui.py    # TC_DASH_01 to TC_DASH_02
│   └── test_modal_ui.py        # TC_MODAL_01 to TC_MODAL_04
├── docs/
│   └── TEST_CASES.md           # Detailed Test Cases Specification Table
├── reports/
│   └── test_report.html        # Dynamically Generated HTML Test Report
├── run_tests.py                # One-click Test Runner & Report Generator
└── README.md                   # Project Documentation
```


---


## 🚀 Getting Started


### 1. Prerequisites
- Python 3.12+
- `uv` installed (`curl -LsSf https://astral.sh/uv/install.sh | sh`)
- Firefox browser installed


### 2. Run All Tests & Generate Dynamic Report


Simply run:
```bash
python3 run_tests.py
```
Or directly with `uv`:
```bash
uv run pytest tests -v --html=reports/test_report.html --self-contained-html
```


---


## 📊 Viewing the Test Report


Open the generated HTML report in any web browser:
```bash
firefox reports/test_report.html
```
File Path: `reports/test_report.html`


The report includes:
- Live timestamp and environment details
- Total tests executed, pass/fail counts, and success rate
- Exact execution time for every individual test case
- Filterable test result grid



