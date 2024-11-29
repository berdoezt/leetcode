# class is a blueprint or templates that define the properties and behavior of an object
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        pass

    def start_engine(self):
        print("start engine")

# object is a instance of a class / representation of a real world object that has PROPERTIES and BEHAVIOR
# toyota_car = Car('Toyota', "Avanza", 2023)
# toyota_car.start_engine()

# honda_car = Car('Honda', 'Civic', 2005)
# honda_car.start_engine()
# print(honda_car.year)

class BankAccount:
    def __init__(self, account_number) -> None:
        self.__acount_number = account_number

        # encapsulation : process of hiding the detail implementation from outside world and only expose necessary behavior and properties
        # this properties is private, can't accessed directly from outside world
        # to interact with this property, we can use the exposed method
        self.__balance = 0
    
    def deposit(self, amount):
        if not self.__is_valid_amount(amount):
            raise Exception("invalid amount")
        
        self.__balance += amount
        pass

    def get_balance(self):
        return self.__balance

    def withdrawal(self, amount):
        if not self.__is_valid_amount(amount):
            raise Exception("invalid amount")
        
        if self.__balance < amount:
            raise Exception("insufficient funds")
        
        self.__balance -= amount
        pass

    # encapsulation : this method can't be accessed from outside world, can only accessible inside the class and can be interact using exposed method from outside world
    def __is_valid_amount(self, amount):
        return amount > 0
        pass

# ba = BankAccount("1234")
# print(ba.get_balance())
# ba.withdrawal(0)
# print(ba.get_balance())


class Vehicle:
    def __init__(self, color) -> None:
        self.__color = color
        pass

    def get_color(self):
        return self.__color

    def start(self):
        pass

# inheritance : allow a class to inherit properties and behavior from other class called parent class / super class
# class that inherit is called subclass / child class
class Car(Vehicle):
    def __init__(self, color, model) -> None:
        super().__init__(color)
        self.__model = model
    
    def get_model(self):
        return self.__model
    
    def start(self):
        print("brum brum")

# c = Car("red", "civic")
# print(c.get_color())
# print(c.get_model())

from abc import ABC, abstractmethod

# polymorphism : object can have many form
# this document is an abstract class
class Document:
    @abstractmethod
    def show(self):
        raise NotImplementedError("no implementation")

class PdfDocument(Document):
    # overriding : child method override parent method
    # duck typing when a class implement the required method from an abstract, then its equal to the abstract
    def show(self):
        print("show pdf document")

class WordDocument(Document):
    # overriding : child method override parent method
    def show(self):
        print("show word document")

class Printer:
    # dependency inversion : the dependency is injected from outside, not initiated from the class that need it
    # this to promote loose coupling between the class and its dependency
    def __init__(self, document: Document) -> None:
        self.__document: Document = document
        pass

    def print(self):
        self.__document.show()

pdf_document = PdfDocument()
p = Printer(pdf_document)
p.print()
