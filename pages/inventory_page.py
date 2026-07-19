class InventoryPage:
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
