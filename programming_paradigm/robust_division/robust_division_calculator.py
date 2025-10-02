def safe_divide(numerator, denominator):
    """
    Safely divide two numbers, handling division by zero
    and non-numeric inputs.
    """
    try:
        numerator = float(numerator)
        denominator = float(denominator)
        result = numerator / denominator
        return f"The result of the division is {result}"
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    except ValueError:
        return "Error: Please enter numeric values only."
