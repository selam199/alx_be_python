# robust_division_calculator.py

def safe_divide(numerator, denominator):
    """
    Safely divides two numbers, handling errors like division by zero
    and non-numeric inputs.

    Args:
        numerator (str): The numerator value as a string (to allow error handling).
        denominator (str): The denominator value as a string (to allow error handling).

    Returns:
        str: The result of the division or an appropriate error message.
    """
    try:
        # Attempt to convert inputs to floats
        num = float(numerator)
        den = float(denominator)

        # Check for division by zero
        if den == 0:
            return "Error: Cannot divide by zero."

        # Perform the division
        result = num / den
        return f"The result of the division is {result:.2f}"

    except ValueError:
        # Handle non-numeric input
        return "Error: Please enter numeric values only."

