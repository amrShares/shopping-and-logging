import logging

logger = logging.getLogger(__name__)

class InventoryService:

    def __init__(self, inventory):
        self.inventory = inventory

    def reduce_stock(self, product_id, quantity):
        product_id = str(product_id)
        current = self.inventory.get_stock(product_id)
        print('current is', current)
        if current < 3:
            logger.info(f'refilling stock for product {product_id} with a quantity of 20')
            self.fill_stock(product_id, 20)
        if current > quantity:
            self.inventory.set_stock(product_id, self.inventory.get_stock(product_id) - quantity)
        elif current == quantity:
            logger.info(f"Stock for product {product_id} is now depleted.")
            self.inventory.set_stock(product_id, self.inventory.get_stock(product_id) - quantity)
        else:
            logger.warning(f"attempting to take more than the current stock for product {product_id}")
            return False
        return True

    def fill_stock(self, product_id, quantity):
        self.inventory.set_stock(product_id, self.inventory.get_stock(product_id) + quantity)