# HR management web application – Selenium Python POM + Pytest + Allure

This repository contains a complete Page Object Model (POM) test automation framework for
the OrangeHRM demo site: https://opensource-demo.orangehrmlive.com

## ✅ Features
- Selenium 4 + Python
- Page Object Model (POM)
- Pytest with parametrization and fixtures
- Allure Reporting
- Data-driven tests (CSV)
- Cross-browser with webdriver-manager (Chrome/Firefox)

---

## 🚀 Quick Start (macOS Big Sur 11.7.10)
1) Create and activate a virtual environment
```bash
python3 -m venv .venv
source .venv/bin/activate
```

2) Install project dependencies
```bash
pip install -r requirements.txt
```

3) Install Allure CLI (so `allure` command works)
```bash
brew install allure
allure --version
```

4) Run tests and generate Allure results
```bash
pytest --alluredir=allure-results
```

5) View the Allure report
```bash
allure serve allure-results
```

---

## 🧭 Project Structure
```
HRM_Automation/
├── pages/                 # Page Objects
├── tests/                 # Test cases (TC1–TC10)
├── utils/                 # Driver factory, test data
├── allure-results/        # Test result artifacts (generated)
├── reports/               # For static report output (optional)
├── conftest.py            # Pytest fixtures
├── pytest.ini
├── requirements.txt
└── README.md
```

---

## 🧪 Mapping to Test Cases
- **TC1–TC3**: `tests/test_login.py`
- **TC4, TC8**: `tests/test_menu.py`
- **TC5, TC6**: `tests/test_user_management.py`
- **TC7**: `tests/test_forgot_password.py`
- **TC9**: `tests/test_leave.py`
- **TC10**: `tests/test_claim.py`

> Note: The OrangeHRM demo occasionally changes UI/locators. The Page Objects use robust, text/label-based XPaths,
but you may need to tweak selectors if the demo is updated.

---

## 🧰 Useful Commands
```bash
# Run all tests with 4 parallel workers
pytest -n 4 --alluredir=allure-results

# Run only smoke tests
pytest -m smoke --alluredir=allure-results

# Regenerate report
allure generate allure-results -o reports --clean
```

---

## 🔧 Troubleshooting
- If you see `bash: allure: command not found` → Install with `brew install allure`.
- If browsers fail to start, update your browser and rerun. `webdriver-manager` downloads drivers automatically.
- If a locator fails, open DevTools and adjust the XPath/CSS in the corresponding Page Object.
