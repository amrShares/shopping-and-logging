import json
import logging

logger = logging.getLogger(__name__)

class Inventory:

    def __init__(self, stock_path, details_path):
        self._stock = {}  # product_id → quantity
        self._product_details = {}  # product_id → product details
        self.stock_path = stock_path
        self.details_path = details_path
        self.load_stock()
        self.load_product_details()

    def load_stock(self):
        try:
            with open(self.stock_path, 'r') as f:
                self._stock = json.load(f)
            logger.info(f"Loaded stock from {self.stock_path}")
        except FileNotFoundError:
            logger.exception(f"Stock file {self.stock_path} not found. Starting with empty stock.")
            self._stock = {}

    def load_product_details(self):
        try:
            with open(self.details_path, 'r') as f:
                self._product_details = json.load(f)
            logger.info(f"Loaded stock details from {self.details_path}")
        except FileNotFoundError:
            logger.exception(f"Stock details file {self.details_path} not found. Starting with empty stock details.")
            self._product_details = {}

    def set_stock(self, product_id, quantity):
        self._stock[product_id] = quantity

    def get_product_details(self, product_id):
        return self._product_details.get(str(product_id), False)

    def get_stock(self, product_id):
        return self._stock.get(product_id, 0)

    @property
    def no_of_products(self):
        return len(self._product_details)
    