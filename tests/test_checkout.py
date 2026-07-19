from pages.login_page import LoginPage
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
