from typing import Tuple

def get_tuple(num: int) -> Tuple[int]:
    return tuple(int(digit) for digit in str(num))

result = get_tuple(123456)
print(result)
