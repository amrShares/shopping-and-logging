import json
import logging

logger = logging.getLogger(__name__)

class Inventory:

    def __init__(self, stock_path, details_path):
        self._stock = {}  # product_id → quantity
        self._stock_details = {}  # product_id → product details
        self.stock_path = stock_path
        self.details_path = details_path
        self.load_stock()
        self.load_stock_details()

    def load_stock(self):
        try:
            with open(self.stock_path, 'r') as f:
                self._stock = json.load(f)
            logger.info(f"Loaded stock from {self.stock_path}")
        except FileNotFoundError:
            logger.exception(f"Stock file {self.stock_path} not found. Starting with empty stock.")
            self._stock = {}

    def load_stock_details(self):
        try:
            with open(self.details_path, 'r') as f:
                self._stock_details = json.load(f)
            logger.info(f"Loaded stock details from {self.details_path}")
        except FileNotFoundError:
            logger.exception(f"Stock details file {self.details_path} not found. Starting with empty stock details.")
            self._stock_details = {}

    def set_stock(self, product_id, quantity):
        self._stock[product_id] = quantity

    @property
    def stock(self, product_id):
        return self._stock.get(product_id, 0)