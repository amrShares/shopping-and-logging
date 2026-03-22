from models import Order

class OrderService:

    def __init__(self, inventory_service):

        self.inventory_service = inventory_service
        self.order_counter = 0

    def create_order(self, user_id, available_balance, cart, product_lookup):

        total_price = 0
        items_added  = 0
        for product_id, quantity in cart.items.items():

            product = product_lookup.get_product_details(product_id)

            if self.inventory_service.reduce_stock(
                product_id,
                quantity
            ):
                total_price += product['price'] * quantity
                items_added += 1
            else:
                self.revert_order(cart, items_added)
                return False, 0

        if available_balance < total_price:
            self.revert_order(cart, items_added)
            return False, total_price

        order = Order(
            order_id=self.order_counter,
            user_id=user_id,
            cart=cart
        )

        self.order_counter += 1

        return order, total_price

    def revert_order(self, cart, items_added):

        for product_id, quantity in cart.items.items():

            self.inventory_service.fill_stock(
                product_id,
                quantity
            )
            items_added -= 1

            if items_added == 0:
                return