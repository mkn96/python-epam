from typing import Any, Dict, List, Set

def check(lst: List[Dict[Any, Any]]) -> Set[Any]:
    unique_vals = set()
    for d in lst:
        unique_vals.update(d.values())
    return unique_vals