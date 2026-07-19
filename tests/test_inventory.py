from pages.login_page import LoginPage
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
