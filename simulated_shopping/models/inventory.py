class Inventory:

    def __init__(self):
        self._stock = {}  # product_id → quantity

    def set_stock(self, product_id, quantity):
        self._stock[product_id] = quantity

    @property
    def stock(self, product_id):
        return self._stock.get(product_id, 0)