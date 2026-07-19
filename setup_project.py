"""
Run this once inside your saucedemo-test-automation folder.
It creates all the folders and files, pre-filled with code,
including cross-browser testing (Chromium, Firefox, WebKit) from the start.

Usage:
    python setup_project.py
"""

import os

files = {
    "pages/__init__.py": "",

    "pages/login_page.py": '''class LoginPage:
    def __init__(self, page):
        self.page = page
        self.url = "https://www.saucedemo.com/"
        self.username_input = page.locator("#user-name")
        self.password_input = page.locator("#password")
        self.login_button = page.locator("#login-button")
        self.error_message = page.locator("[data-test='error']")

    def goto(self):
        self.page.goto(self.url)

    def login(self, username, password):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()
''',

    "pages/inventory_page.py": '''class InventoryPage:
    def __init__(self, page):
        self.page = page
        self.inventory_items = page.locator(".inventory_item")
        self.cart_icon = page.locator(".shopping_cart_link")
        self.sort_dropdown = page.locator(".product_sort_container")

    def add_item_to_cart(self, item_name):
        item = self.page.locator(".inventory_item", has_text=item_name)
        item.locator("button", has_text="Add to cart").click()

    def get_item_count(self):
        return self.inventory_items.count()

    def sort_by(self, option_value):
        self.sort_dropdown.select_option(option_value)
''',

    "pages/cart_page.py": '''class CartPage:
    def __init__(self, page):
        self.page = page
        self.checkout_button = page.locator("#checkout")
        self.cart_items = page.locator(".cart_item")

    def go_to_checkout(self):
        self.checkout_button.click()
''',

    "tests/__init__.py": "",

    "tests/test_login.py": '''from pages.login_page import LoginPage

def test_valid_login(page):
    login = LoginPage(page)
    login.goto()
    login.login("standard_user", "secret_sauce")
    assert page.url == "https://www.saucedemo.com/inventory.html"

def test_invalid_login_shows_error(page):
    login = LoginPage(page)
    login.goto()
    login.login("invalid_user", "wrong_pass")
    assert login.error_message.is_visible()

def test_locked_out_user(page):
    login = LoginPage(page)
    login.goto()
    login.login("locked_out_user", "secret_sauce")
    assert "locked out" in login.error_message.inner_text().lower()
''',

    "tests/test_inventory.py": '''from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

def test_products_are_listed(page):
    login = LoginPage(page)
    login.goto()
    login.login("standard_user", "secret_sauce")

    inventory = InventoryPage(page)
    assert inventory.get_item_count() == 6

def test_add_item_to_cart(page):
    login = LoginPage(page)
    login.goto()
    login.login("standard_user", "secret_sauce")

    inventory = InventoryPage(page)
    inventory.add_item_to_cart("Sauce Labs Backpack")
    assert page.locator(".shopping_cart_badge").inner_text() == "1"
''',

    "tests/test_checkout.py": '''from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage

def test_checkout_flow(page):
    login = LoginPage(page)
    login.goto()
    login.login("standard_user", "secret_sauce")

    inventory = InventoryPage(page)
    inventory.add_item_to_cart("Sauce Labs Backpack")
    inventory.cart_icon.click()

    cart = CartPage(page)
    cart.go_to_checkout()

    page.locator("#first-name").fill("Namu")
    page.locator("#last-name").fill("Tano")
    page.locator("#postal-code").fill("1100")
    page.locator("#continue").click()

    assert page.locator(".summary_info").is_visible()
    page.locator("#finish").click()
    assert page.locator(".complete-header").inner_text() == "Thank you for your order!"
''',

    "conftest.py": '''import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="function", params=["chromium", "firefox", "webkit"])
def page(request):
    with sync_playwright() as p:
        browser_type = getattr(p, request.param)
        browser = browser_type.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()
        yield page
        browser.close()
''',

    "pytest.ini": '''[pytest]
testpaths = tests
''',

    ".gitignore": '''venv/
__pycache__/
.pytest_cache/
test-results/
playwright-report/
*.pyc
.env
''',

    "README.md": '''# SauceDemo Test Automation Suite

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
''',

    ".github/workflows/tests.yml": '''name: Run Playwright Tests

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: '3.11'
      - name: Install dependencies
        run: |
          pip install -r requirements.txt
          playwright install --with-deps chromium firefox webkit
      - name: Run tests
        run: pytest -v
''',
}


def main():
    for filepath, content in files.items():
        folder = os.path.dirname(filepath)
        if folder:
            os.makedirs(folder, exist_ok=True)
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Created file: {filepath}")

    print("\nAll done! Your project structure is ready.")
    print("Next steps:")
    print("  1. pip freeze > requirements.txt")
    print("  2. pytest -v")


if __name__ == "__main__":
    main()