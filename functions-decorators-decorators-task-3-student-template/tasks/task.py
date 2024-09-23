import functools

def validate(func):
    @functools.wraps(func)
    def wrapper(*args):
        if all(0 <= arg <= 256 for arg in args):
            return func(*args)
        else:
            return "Function call is not valid!"
    return wrapper

@validate
def set_pixel(r, g, b):
    """
    Create a pixel with RGB values.

    Parameters:
    - r (int): Red value (0 to 256).
    - g (int): Green value (0 to 256).
    - b (int): Blue value (0 to 256).

    Returns:
    - str: "Pixel created!" if valid, "Function call is not valid!" otherwise.
    """
    return "Pixel created!"

# Example usage
print(set_pixel(0, 127, 300))  # Output: Function call is not valid!
print(set_pixel(0, 127, 250))  # Output: Pixel created!
