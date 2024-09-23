from typing import List


def split_by_index(s: str, indexes: List[int]) -> List[str]:
    parts = []
    start = 0

    for index in sorted(indexes):
        if index <= len(s):
            parts.append(s[start:index])
            start = index
    parts.append(s[start:])

    return parts


# Test cases
print(split_by_index("pythoniscool,isn'tit?",
                     [6, 8, 12, 13, 18]))  # Output: ["python", "is", "cool", ",", "isn't", "it?"]
print(split_by_index("no luck", [42]))  # Output: ["no luck"]
