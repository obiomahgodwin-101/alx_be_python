# inheritance_polymorphism.py

# ---------------- Exercise 1: Single Inheritance ----------------
class Shape:
    def calculate_area(self):
        print("This method should be overridden by subclasses.")


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        area = self.width * self.height
        print(f"The area of the rectangle is {area} square units.")


# ---------------- Exercise 2: Multiple Inheritance ----------------
class Bird:
    def fly(self):
        print("The bird is flying.")


class Mammal:
    def run(self):
        print("The mammal is running.")


class Bat(Bird, Mammal):
    def fly(self):
        print("The bat is flying using its wings.")

    def run(self):
        print("The bat can also crawl or run a little.")


# ---------------- Exercise 3: Polymorphism with Duck Typing ----------------
class Dog:
    def make_sound(self):
        print("Woof! Woof!")


class Cat:
    def make_sound(self):
        print("Meow! Meow!")


class BirdSound:
    def make_sound(self):
        print("Chirp! Chirp!")


def let_them_speak(animals):
    for animal in animals:
        animal.make_sound()


# ---------------- Testing the code ----------------
if __name__ == "__main__":
    print("\n--- Exercise 1: Single Inheritance ---")
    rect = Rectangle(10, 5)
    rect.calculate_area()

    print("\n--- Exercise 2: Multiple Inheritance ---")
    bat = Bat()
    bat.fly()
    bat.run()

    print("\n--- Exercise 3: Polymorphism with Duck Typing ---")
    dog = Dog()
    cat = Cat()
    bird = BirdSound()
    animals = [dog, cat, bird]
    let_them_speak(animals)
