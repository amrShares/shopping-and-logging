from models import Order

class OrderService:

    def __init__(self, inventory_service):

        self.inventory_service = inventory_service
        self.order_counter = 1

    def create_order(self, user_id, cart, product_lookup):

        total_price = 0
        items_added  = 0
        for product_id, quantity in cart.items.items():

            product = product_lookup[product_id]

            if self.inventory_service.reduce_stock(
                product_id,
                quantity
            ):
                total_price += product.price * quantity
                items_added += 1
            else:
                self.revert_order(user_id, cart, product_lookup, items_added)
                return False

        order = Order(
            order_id=self.order_counter,
            user_id=user_id,
            items=dict(cart.items),
            total_price=total_price
        )

        self.order_counter += 1

        return order

    def revert_order(self, user_id, cart, product_lookup, items_added):


        for product_id, quantity in cart.items.items():

            self.inventory_service.fill_stock(
                product_id,
                quantity
            )
            items_added -= 1

            if items_added == 0:
                return