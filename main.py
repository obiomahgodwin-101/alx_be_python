<<<<<<< HEAD
from library_management import Book, Library

def main():
    library = Library()
    library.add_book(Book("Brave New World", "Aldous Huxley"))
    library.add_book(Book("1984", "George Orwell"))

    print("Available books after setup:")
    library.list_available_books()

    library.check_out_book("1984")
    print("\nAvailable books after checking out '1984' :")
    library.list_available_books()

    library.return_book("1984")
    print("\nAvailable books after returning '1984' :")
    library.list_available_books()
=======
import sys
from robust_division_calculator import safe_divide

def main():
    if len(sys.argv) != 3:
        print("Usage: python main.py <numerator> <denominator>")
        sys.exit(1)

    numerator = sys.argv[1]
    denominator = sys.argv[2]

    result = safe_divide(numerator, denominator)
    print(result)
>>>>>>> ee7c3a3a1c9686ca0d322293693b9e8d09fa9d81

if __name__ == "__main__":
    main()
