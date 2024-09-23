import time
from typing import Dict

execution_time: Dict[str, float] = {}

def time_decorator(fn):
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = fn(*args, **kwargs)
        execution_time[fn.__name__] = time.perf_counter() - start_time
        return result
    return wrapper

# Example usage
@time_decorator
def func_add(a, b):
    time.sleep(0.2)
    return a + b


"""
Create a decorator function time_decorator which has to calculate the decorated function execution time 
and put this time value in the execution_time dictionary where the key is the decorated function name. 
The value is this function's execution time. 
For example:

@time_decorator
def func_add(a, b):
    sleep(0.2)
    return a + b

>>> func_add(10, 20)
30

>>> execution_time['func_add']
0.212341254
"""
