# class_and_static_methods.py

# ---------------- Exercise 1: Class Methods for Counting Instances ----------------
class Book:
    total_books = 0  # Class variable to count number of books

    def __init__(self, title, author):
        self.title = title
        self.author = author
        Book.total_books += 1  # Increment count when a book is created

    @classmethod
    def display_total_books(cls):
        print(f"Total number of books created: {cls.total_books}")


# ---------------- Exercise 2: Static Method for Utility Calculation ----------------
class Calculator:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def multiply(a, b):
        return a * b


# ---------------- Exercise 3: Class Method for Factory Creation ----------------
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def create_child(cls, name):
        # Creates a child with age 0
        return cls(name, 0)

    def __str__(self):
        return f"{self.name}, {self.age} years old"


# ---------------- Testing the code ----------------
if __name__ == "__main__":
    print("\n--- Exercise 1: Class Methods for Counting Instances ---")
    b1 = Book("The Alchemist", "Paulo Coelho")
    b2 = Book("Rich Dad Poor Dad", "Robert Kiyosaki")
    Book.display_total_books()

    print("\n--- Exercise 2: Static Method for Utility Calculation ---")
    print(f"Addition: 10 + 5 = {Calculator.add(10, 5)}")
    print(f"Multiplication: 10 × 5 = {Calculator.multiply(10, 5)}")

    print("\n--- Exercise 3: Class Method for Factory Creation ---")
    child = Person.create_child("Godwin Jr.")
    print(child)
