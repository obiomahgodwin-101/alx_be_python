# library_management.py

# Book class
class Book:
    def __init__(self, title, author):
        self.title = title          # public attribute
        self.author = author        # public attribute
        self._is_checked_out = False  # private attribute to track availability

    def check_out(self):
        """Mark the book as checked out"""
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

    def return_book(self):
        """Mark the book as returned"""
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False

    def is_available(self):
        """Return True if the book is not checked out"""
        return not self._is_checked_out


# Library class
class Library:
    def __init__(self):
        self._books = []  # private list to store Book instances

    def add_book(self, book):
        """Add a Book instance to the library"""
        self._books.append(book)

    def check_out_book(self, title):
        """Check out a book by title"""
        for book in self._books:
            if book.title == title and book.is_available():
                book.check_out()
                return True
        print(f"Book '{title}' is not available.")
        return False

    def return_book(self, title):
        """Return a book by title"""
        for book in self._books:
            if book.title == title and not book.is_available():
                book.return_book()
                return True
        print(f"Book '{title}' was not checked out.")
        return False

    def list_available_books(self):
        """Print all available books"""
        for book in self._books:
            if book.is_available():
                print(f"{book.title} by {book.author}")

