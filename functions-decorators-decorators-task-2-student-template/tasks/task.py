import time
import functools

def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()

        with open("log.txt", "a") as logfile:
            args_str = ', '.join([f"{arg}={value}" for arg, value in zip(func.__code__.co_varnames[:len(args)], args)])
            kwargs_str = ', '.join([f"{arg}={value}" for arg, value in kwargs.items()])
            log_entry = f"{func.__name__}; args: {args_str}; kwargs: {kwargs_str}; execution time: {end_time - start_time:.2f} sec.\n"
            logfile.write(log_entry)

        return result
    return wrapper
