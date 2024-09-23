from typing import List


class Counter:
    def __init__(self, items):
        self.items = items

    def __add__(self, other):
        if isinstance(other, str):
            return [f"{item} {other}" for item in self.items]
        else:
            raise TypeError("Unsupported operand type(s) for +: 'Counter' and '{}'".format(type(other)))
