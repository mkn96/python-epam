class NameControl:
    def __set_name__(self, owner, name):
        self.name = name

    def __set__(self, instance, value):
        if hasattr(instance, self.name):
            raise ValueError(f"{self.name.capitalize()} can not be changed.")
        if instance.__dict__.get(self.name) is None:  # Allow setting only during initialization
            instance.__dict__[self.name] = value
        else:
            raise AttributeError(f"{self.name.capitalize()} attribute can not be changed after initialization.")

class PriceControl:
    def __set_name__(self, owner, name):
        self.name = name

    def __set__(self, instance, value):
        if not (0 <= value <= 100):
            raise ValueError("Price must be between 0 and 100.")
        instance.__dict__[self.name] = value

class Book:
    author = NameControl()
    name = NameControl()
    price = PriceControl()

    def __init__(self, author, name, price):
        self.author = author
        self.name = name
        self.price = price
