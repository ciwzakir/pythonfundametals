# Base class/ Parents class /Sperclass
class Vehicle:

    def __init__(self, name, color, price): # Parameter of constructor
        self.name = name # self.name = instance variable
        self.color = color # after = always place parameter name of constructor
        self.price = price

    def info(self): #  instance method
        print(self.name, self.color, self.price)

# Child class / subclass/
class Car(Vehicle):

    def change_gear(self, no):
        print(self.name, 'change gear to number', no)

# Create object of Car
car = Car('BMW X1', 'Black', 35000) # car is the  object of Car class
car.info()
car.change_gear(5)

"""
Inside a Class, we can define the following three types of methods.

Instance method: Used to access or modify the object attributes. If we use instance variables inside a method, such methods are called instance methods.
Class method: Used to access or modify the class state. In method implementation, if we use only class variables, then such type of methods we should declare as a class method.
Static method: It is a general utility method that performs a task in isolation. Inside this method, we don’t use instance or class variable because this static method doesn’t have access to the class attributes

"""