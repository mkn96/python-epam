import functools

def decorator_apply(func):
    def decorator(func_to_decorate):
        @functools.wraps(func_to_decorate)
        def wrapper(*args, **kwargs):
            result = func(func_to_decorate(*args, **kwargs))
            return result
        return wrapper
    return decorator

# Example usage
@decorator_apply(lambda user_id: user_id + 1)
def return_user_id(num: int):
    return num

# Example usage
print(return_user_id(42))  # Output: 43
