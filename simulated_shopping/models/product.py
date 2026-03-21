class Product:

    def __init__(self, id, name, category, price):
        self.id = id
        self.name = name
        self.category = category
        self.price = price

    def __str__(self):
        return f"Product(id={self.id}, category={self.category} name={self.name}, price={self.price})"