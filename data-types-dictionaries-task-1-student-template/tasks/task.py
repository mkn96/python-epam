from typing import Dict


def get_dict(s: str) -> Dict[str, int]:
    # declare the dictionary
    frequency = {}
    # set the string to lowercase
    s = s.lower()
    # iterate
    for char in s:
        frequency[char] = frequency.get(char, 0) + 1
    return frequency

print(get_dict("this is Mike"))

result = 20 / 2 + 12 * 2 - 9
print (result)