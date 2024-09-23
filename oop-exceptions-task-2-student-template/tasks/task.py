ZERO_DIVISION_ERROR_CODE = "Error code: division by zero"
INVALID_LITERAL = "Error code: invalid literal for int() with base 10: {}"


def divide(input_str):
    try:
        # Split the input string into two integers
        a, b = map(int, input_str.split())

        # Perform division
        result = a / b

        return result
    except ValueError:
        # Handle invalid literal for int()
        return "Error code: invalid literal for int() with base 10"
    except ZeroDivisionError:
        # Handle division by zero
        return "Error code: division by zero"


# Test cases
print(divide("4 2"))  # Output: 2.0
print(divide("5 5"))  # Output: 1.0
print(divide("7 2"))  # Output: 3.5
print(divide("1 0"))  # Output: Error code: division by zero
print(divide("$ 1"))  # Output: Error code: invalid literal for int() with base 10: '$'
print(divide("4 *"))  # Output: Error code: invalid literal for int() with base 10: '*'
print(divide("% &"))  # Output: Error code: invalid literal for int() with base 10: '%'

