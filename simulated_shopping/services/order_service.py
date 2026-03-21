from ..models import Order

class OrderService:

    def __init__(self, inventory_service):

        self.inventory_service = inventory_service
        self.order_counter = 1

    def create_order(self, user_id, cart, product_lookup):

        total_price = 0

        for product_id, quantity in cart.items.items():

            product = product_lookup(product_id)

            self.inventory_service.reduce_stock(
                product_id,
                quantity
            )

            total_price += product.price * quantity

        order = Order(
            order_id=self.order_counter,
            user_id=user_id,
            items=dict(cart.items),
            total_price=total_price
        )

        self.order_counter += 1

        return order