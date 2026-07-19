![Tests](https://github.com/angelotano35-prod/saucedemo-test-automation/actions/workflows/tests.yml/badge.svg)


# SauceDemo Test Automation Suite

Automated end-to-end test suite for saucedemo.com built with Playwright and Python,
using the Page Object Model design pattern, running across Chromium, Firefox, and WebKit.

## Tech Stack
- Playwright
- Python + Pytest
- GitHub Actions (CI)

## Features Tested
- Login (valid, invalid, locked-out user)
- Inventory listing and add-to-cart
- Full checkout flow

## Cross-browser support
All tests run automatically across Chromium, Firefox, and WebKit.

## Running Locally
```bash
pip install -r requirements.txt
playwright install
pytest -v
```

## CI
Tests run automatically on every push via GitHub Actions.
