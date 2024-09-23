from typing import List, Tuple, Union

def seq_sum(sequence: Union[List, Tuple]) -> int:
    total = 0
    for item in sequence:
        if isinstance(item, (list, tuple)):
            total += seq_sum(item)
        else:
            total += item
    return total
