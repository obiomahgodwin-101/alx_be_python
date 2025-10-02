# library_management.py

class Book:
    def __init__(self, title, author):
        self.title = title            # public attribute
        self.author = author          # public attribute
        self._is_checked_out = False  # private attribute to track availability

    def check_out(self):
        """Mark the book as checked out."""
        self._is_checked_out = True

    def return_book(self):
        """Mark the book as returned/available."""
        self._is_checked_out = False


class Library:
    def __init__(self):
        self._books = []  # private list to store Book instances

    def add_book(self, book):
        """Add a Book instance to the library."""
        self._books.append(book)

    def check_out_book(self, title):
        """Check out a book by title if it is available."""
        for book in self._books:
            if book.title == title and not book._is_checked_out:
                book.check_out()
                return True
        return False

    def return_book(self, title):
        """Return a book by title."""
        for book in self._books:
            if book.title == title and book._is_checked_out:
                book.return_book()
                return True
        return False

    def list_available_books(self):
        """Print all books that are not checked out."""
        for book in self._books:
            if not book._is_checked_out:
                print(f"{book.title} by {book.author}")

