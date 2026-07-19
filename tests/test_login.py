from pages.login_page import LoginPage

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
