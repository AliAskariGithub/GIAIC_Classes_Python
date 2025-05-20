class Product:
    def __init__(self, price):
        self._price = price
    
    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative")
        self._price = value
    
    @price.deleter
    def price(self):
        del self._price

# Example usage
if __name__ == "__main__":
    product = Product(100)
    print(product.price)
    product.price = 200
    del product.price