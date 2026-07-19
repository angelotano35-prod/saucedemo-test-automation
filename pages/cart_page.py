class CartPage:
    def __init__(self, page):
        self.page = page
        self.checkout_button = page.locator("#checkout")
        self.cart_items = page.locator(".cart_item")

    def go_to_checkout(self):
        self.checkout_button.click()
