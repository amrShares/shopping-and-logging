class CartService:
    def add_to_cart(self, cart, product_id, quantity):
        cart.add_item(product_id, quantity)
    def remove_from_cart(self, cart, product_id, quantity):
        cart.remove_item(product_id, quantity)
