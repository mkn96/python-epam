def union(*args) -> set:
    return set(item for arg in args for item in (arg if isinstance(arg, (list, tuple)) else {arg}))

def intersect(*args) -> set:
    if not args:
        return set()
    return set(args[0]).intersection(*args[1:])
