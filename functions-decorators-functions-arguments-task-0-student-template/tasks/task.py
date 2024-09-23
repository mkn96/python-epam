from typing import Dict

def generate_squares(num: int)-> Dict[int, int]:
    generated = {}  # declare the dictionary
    for i in range(1, num + 1):  # iterate through numbers from 1 to num (inclusive)
        generated[i] = i ** 2  # assign the square of the number as the value
    return generated

print(generate_squares(5))

"""
Implement a function that takes a number as an argument and returns a dictionary, 
where the key is a number and the value is the square of that number.

Example:

>>> generate_squares(5)
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
"""