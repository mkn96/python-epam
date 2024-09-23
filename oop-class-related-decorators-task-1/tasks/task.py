from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, brand_name, year_of_issue, base_price, mileage):
        self.brand_name = brand_name
        self.year_of_issue = year_of_issue
        self.base_price = base_price
        self.mileage = mileage

    @property
    def vehicle_type(self):
        return f"{self.brand_name} {self.__class__.__name__}"

    @staticmethod
    def is_motorcycle():
        return NotImplemented

    @property
    def purchase_price(self):
        price = self.base_price - 0.1 * self.mileage
        return max(price, 100_000)

class Car(Vehicle):
    @staticmethod
    def is_motorcycle():
        return False

class Motorcycle(Vehicle):
    @staticmethod
    def is_motorcycle():
        return True

class Truck(Vehicle):
    @staticmethod
    def is_motorcycle():
        return False

class Bus(Vehicle):
    @staticmethod
    def is_motorcycle():
        return False
