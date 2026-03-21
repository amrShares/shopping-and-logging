class Order:

    def __init__(self, order_id, user_id, cart):
        self.order_id = order_id
        self.user_id = user_id
        self.cart = cart

    def __str__(self):
        return f"Order ID: {self.order_id}, user_id: {self.user_id}, {self.cart}"

    def get_total_price(self):
        return sum(item['price'] for item in self.cart.items.values())