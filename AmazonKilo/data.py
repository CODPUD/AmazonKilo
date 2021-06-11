class Category:
    def __init__(self, id, value, text):
        self.id = id
        self.value = value
        self.text = text

    def __str__(self):
        return self.text

class Product:
    def __init__(self, title=None, price=None, rating=None):
        self.title = title
        self.price = price
        self.rating = rating

    def __str__(self):
        return self.title