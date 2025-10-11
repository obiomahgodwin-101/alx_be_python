# Exercise 3: Custom Exception

# Define a custom exception class
class ValueTooHighError(Exception):
    """Raised when the input value is too high"""
    pass

# Main program
try:
    number = int(input("Enter a number: "))
    if number > 100:
        raise ValueTooHighError("The value is too high! Must be 100 or less.")
    else:
        print(f"Valid number: {number}")
except ValueTooHighError as e:
    print("Error:", e)
