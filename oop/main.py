class Book:
    """
    A class representing a book with title, author, and publication year.
    Demonstrates the use of Python magic methods.
    """

    def __init__(self, title: str, author: str, year: int):
        """Constructor method to initialize the Book instance."""
        self.title = title
        self.author = author
        self.year = year

    def __del__(self):
        """Destructor method that prints a message when the object is deleted."""
        print(f"Deleting {self.title}")

    def __str__(self):
        """Returns a user-friendly string representation of the book."""
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        """Returns an official string representation for debugging/recreation."""
        return f"Book('{self.title}', '{self.author}', {self.year})"

