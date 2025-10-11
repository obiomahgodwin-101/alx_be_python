# class_exercises.py
import gc  # To help show destructor message quickly

# ---------------- Exercise 1: Constructors and Destructors ----------------
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print(f"Person created: {self.name}, {self.age} years old")

    def __del__(self):
        print(f"Goodbye {self.name}! The Person object is being deleted.")


# ---------------- Exercise 2: Magic Methods (__str__ and __repr__) ----------------
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f"'{self.title}' by {self.author} ({self.pages} pages)"

    def __repr__(self):
        return f"Book(title='{self.title}', author='{self.author}', pages={self.pages})"


# ---------------- Exercise 3: Class Inheritance ----------------
class Animal:
    def eat(self):
        print("The animal is eating.")

    def sleep(self):
        print("The animal is sleeping.")


class Dog(Animal):
    def bark(self):
        print("The dog is barking.")


# ---------------- Testing the code ----------------
if __name__ == "__main__":
    print("\n--- Exercise 1: Constructor & Destructor ---")
    person1 = Person("Godwin", 25)
    del person1
    gc.collect()  # Force garbage collection to show destructor immediately

    print("\n--- Exercise 2: Magic Methods ---")
    book1 = Book("The Alchemist", "Paulo Coelho", 208)
    print(str(book1))   # User-friendly representation
    print(repr(book1))  # Developer-friendly representation

    print("\n--- Exercise 3: Inheritance ---")
    animal = Animal()
    dog = Dog()
    animal.eat()
    animal.sleep()
    dog.eat()
    dog.sleep()
    dog.bark()
