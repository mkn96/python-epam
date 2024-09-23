from typing import List, Dict

def combine_dicts(*args:List[Dict[str, int]]) -> Dict[str, int]:
    result = {}
    for dictionary in args:
        for key, value in dictionary.items():
            if key in result:
                result[key] += value
            else:
                result[key] = value
    return result
