def safe_divide(numerator, denominator):
    """
    Safely divides numerator by denominator.
    Returns result or an exact error message.
    """
    try:
        # Convert inputs to float
        numerator = float(numerator)
        denominator = float(denominator)

        # Perform division
        result = numerator / denominator
        return f"The result of the division is {result}"
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    except ValueError:
        return "Error: Please enter numeric values only."
