class Cart:

    def __init__(self):
        self.items = {}  # product_id → quantity

    def add_item(self, product_id, quantity):

        if product_id in self.items:
            self.items[product_id] += quantity
        else:
            self.items[product_id] = quantity

    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)
            print(f"Removed {item} from the cart.")
        else:
            print(f"{item} not found in the cart.")

    def view_cart(self):
        if self.items:
            print("Items in the cart:")
            for item in self.items:
                print(f"- {item}")
        else:
            print("The cart is empty.")

    def __str__(self):
        return f"Cart with items: {', '.join(f'{product_id} (x{quantity})' for product_id, quantity in self.items.items())}"