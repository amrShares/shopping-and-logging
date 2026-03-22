class User:
    def __init__(self, name, email, orders=[], balance=0):
        self.name = name
        self.email = email
        self.orders = orders
        self.balance = balance

    def __str__(self):
        return f"User(name={self.name}, email={self.email} orders={self.orders}, balance={self.balance})"

    def update_email(self, new_email):
        self.email = new_email

    def update_balance(self, new_balance):
        if new_balance < 0:
            raise ValueError("Balance cannot be negative.")
        self.balance = new_balance

    def as_dict(self):
        return {'name' : self.name, 'email':self.email, 'balance':self.balance, 'orders':self.orders}
