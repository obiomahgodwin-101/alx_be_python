# student.py

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Student Name: {self.name}, Age: {self.age}")


# Test the class
if __name__ == "__main__":
    student1 = Student("Alice", 20)
    student1.display_info()

    student2 = Student("Godwin", 25)
    student2.display_info()
