import logging

logger = logging.getLogger(__name__)

class InventoryService:

    def __init__(self, inventory):
        self.inventory = inventory

    def reduce_stock(self, product_id, quantity):
        try:
            current = self.inventory.get_stock(product_id)
            if current < quantity:
                raise ValueError("Insufficient stock")
            elif current == quantity:
                logger.warning(f"Stock for product {product_id} is now depleted.")
            self.inventory.stock[product_id] -= quantity
            return True
        except ValueError as e:
            logger.exception(f"Error reducing stock for product {product_id}")
            return False

    def fill_stock(self, product_id, quantity):
        self.inventory.stock[product_id] = self.inventory.stock.get(product_id, 0) + quantity