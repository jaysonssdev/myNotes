# Playwright with Python & Pytest
1. Setup Environment & Writing Tests
2. Playwright Built-In Locators
3. How to use CSS Locators in Playwright
4. How to use XPath Locators in Playwright
5. How to Handle Input Box, Radio Buttons And Checkboxes
6. How to Handle Single & Multi Select Dropdowns
7. Handling Bootstrap and Hidden Dropdowns
8. Handling Web Tables
9. Handling Dynamic & Pagination Web Tables
10. Handling Date Pickers 
11. Handling Dialogs and Frames in Playwright
12. Mouse Hover, Right Click, Double Click, Drag & Drop
13. Handle Keyboard Actions, File Uploads And downloads
14. Playwright Browser Context, Handle Popups & Tabs
15. Capture Videos & Screenshots, TraceViewer& Flaky Tests
16. Data Driven Testing using JSON, CSV & Excel Files
17. Reporting | How To Generate PyTest & Allure Reports

<br>

## 1. Setup Environment & Writing Tests
- [Youtube Link: Playwright with Python & Pytest| Setup Environment & Writing Tests ( Session 1)](https://www.youtube.com/watch?v=7pgCLbX2sVM&list=PLUDwpEzHYYLtFprdVOrMLBJcqCJ-gRDYa&index=17)

### Introduction
- **Python** - programming language
- **Pytest** - testing framework developed using Python
- **Playwright** - is available as a plugin on top of Pytest

### Installation (with `uv`)
```bash
uv init
uv add --dev pytest-playwright  # To install pytest-playwright
uv run playwright install       # To install playwright browsers

uv run pytest                   # To run the test
```

### Conventional Project Folder Structure (with `uv`)
```
playwright-tests/
├── .github/
│   └── workflows/
│       └── playwright.yml      # CI/CD automation pipeline
├── page_objects/               # Page Object Model (POM) directory
│   ├── __init__.py
│   ├── base_page.py            # Common browser interaction helpers
│   ├── login_page.py           # Specific page selectors and actions
│   └── dashboard_page.py
├── tests/                      # Core test suite folder
│   ├── conftest.py             # Global fixtures, hooks, and browser setups
│   ├── test_auth.py            # Authentication test cases
│   └── test_dashboard.py       # Feature-specific test cases
├── test_artifacts/             # Ignored directory for test run outputs
│   ├── screenshots/            # Saved images on test failures
│   ├── videos/                 # Recorded browser sessions
│   └── traces/                 # Playwright trace viewer zip files
├── .gitignore                  # Excludes venv, tokens, and test_artifacts/
├── pyproject.toml              # Project metadata and pytest configurations
└── uv.lock                     # Strict uv dependency lockfile
```

#### Core Directory Breakdown
1. **The `tests/` Directory & `conftest.py`**

    - Keep all your actual test files inside a dedicated `tests/` folder. Every test file name must start with `test_` for the runner to detect it.

    - Place a `conftest.py` file directly inside this folder. It is automatically loaded by the framework and holds shared setups, such as custom login credentials, API state injection, or global teardown steps.

2. **The `page_objects/` Directory**

    - As your test suite scales, avoid hardcoding UI selectors (like IDs or CSS classes) inside your tests. Use the **Page Object Model (POM)**.
        - Create a `page_objects/` directory at the root level.
        - Define a class for each web page. The class houses the selectors and specific action methods (e.g., `login_page.enter_credentials()`), keeping your tests highly readable and easy to maintain when the UI changes.

3. **The `test_artifacts/` Directory**

    - Playwright can record videos, capture screenshots on failure, and generate detailed interaction traces.
        - Route these files into a centralized output directory at the root level.
        - Ensure this folder is added to your `.gitignore` file so large binary video and image files are never accidentally committed to your repository.

#### Recommended `pyproject.toml` Configuration
To tie this structure together cleanly, configure your `pytest` defaults directly inside your `pyproject.toml` file. This eliminates the need to pass long CLI arguments every time you execute a test:
```
[tool.pytest.ini_options]
testpaths = ["tests"]
addopts = """
    --browser chromium \
    --headed \
    --screenshot=only-on-failure \
    --video=retain-on-failure \
    --output=test_artifacts/
"""
```

