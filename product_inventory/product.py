class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def as_dict(self):
        return {'name': self.name, 'price': self.price}