import pytest
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
