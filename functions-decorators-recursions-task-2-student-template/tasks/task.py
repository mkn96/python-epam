from typing import List, Tuple, Union

def linear_seq(sequence: Union[List, Tuple]) -> List:
    flattened_sequence = []
    for item in sequence:
        if isinstance(item, (list, tuple)):
            flattened_sequence.extend(linear_seq(item))
        else:
            flattened_sequence.append(item)
    return flattened_sequence
