# product.py

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_value(self):
        return self.price * self.quantity

    def display_info(self):
        print(f"Product: {self.name}, Price: ${self.price}, Quantity: {self.quantity}, Total Value: ${self.total_value()}")


# Test the class
if __name__ == "__main__":
    product1 = Product("Laptop", 1200, 3)
    product2 = Product("Phone", 600, 5)

    product1.display_info()
    product2.display_info()
