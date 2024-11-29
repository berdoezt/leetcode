# s : single responsibility principle
# this UserManager violate the s because it doing many things inside 1 functionality
class UserManager:
    def authenticate_user():
        pass

    def update_user():
        pass

    def send_email_notification():
        pass

# can change to below 3 classes. These class now have 1 responsbility only
class UserAuthenticator:
    def authenticate_user():
        pass

class UserUpdater:
    def update_user():
        pass

class UserNotifier:
    def send_email_notification():
        pass

# o : open / close principle, should be open for extention but close for modification
# this ShapeCalculator violate this principle if there's new shape, we need to modify the calculate_area()
class ShapeCalculator:
    def calculate_area(self, shape):
        if shape == 'circle':
            return 3.14 * r * r
        elif shape == 'rectangle':
            return p * l

# we can change to below implementation to satisfy open / close principle
# shape is an abstract class
# and when there're multiple implementation of shape, we can extend it with new class that's inherit from shape class
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        raise NotImplementedError("not implemented")

class Circle(Shape):
    def __init__(self, radius):
        self.__radius = radius
    
    def calculate_area(self):
        return 3.14 * self.__radius * self.__radius

class Rectangle(Shape):
    def __init__(self, width, height) -> None:
        self.__width = width
        self.__height = height
    
    def calculate_area(self):
        return self.__width * self.__height

class ShapeCalculator:
    def __init__(self, shape: Shape) -> None:
        self.__shape = shape
        pass

    def calc(self):
        print(self.__shape.calculate_area())

# c = Circle(7)
# sc = ShapeCalculator(c)
# sc.calc()

# L : liskov substitution principle
# below implementation is violating the liskov substitution, because it should be if parent object is changed with the child object, child should have similar capability
# but in below implementation, the parent class Vehicle have start_engine() behavior. Bike class inherit from Vehicle class, but it doesn't make sense for Bike to start_engine() as well
# because Bike doesn't have engine
class Vehicle:
    def start_engine(self):
        pass

class Car(Vehicle):
    def start_engine(self):
        print("brum brum")

class Bike(Vehicle):
    def start_engine(self):
        # not possible, doesn't make sense for bike to start engine
        pass

# the correct one is the child should have similar behavior with the parent one. So we can the Vehicle class to below
# in this one, we change from start_engine() to start() ,so in this sense, it will be more make sense for Bike as well
class Vehicle:
    def start(self):
        pass