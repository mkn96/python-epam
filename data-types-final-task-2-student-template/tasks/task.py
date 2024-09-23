from typing import List

def check(row_start:int, row_end:int, column_start:int, column_end:int) -> List[List[int]]:
    table = [[row * col for col in range(column_start, column_end + 1)] for row in range(row_start, row_end + 1)]
    return table