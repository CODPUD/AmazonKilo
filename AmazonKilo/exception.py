class AmazonExceptions(Exception):
    pass

class ConnectionException(AmazonExceptions):
    def __init__(self, respond="403"):
        super().__init__(f"Connection Error: {respond}")

class CategoryNotFound(AmazonExceptions):
    def __init__(self):
        super().__init__("Category not found")

class WrongProductException(AmazonExceptions):
    def __init__(self):
        super().__init__("Product doesn`t exist")