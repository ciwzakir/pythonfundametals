"""
We have to import it and abstractmethod
call @abstractmethod just top of the function
It is used as a model
There is no body of abstract class
We can make an abstract class
"""
from abc import ABC, abstractmethod

class Shape(ABC):
    def __init__(self, dim1, dim2):
        self.dim1 = dim1
        self.dim2 = dim2

    @abstractmethod
    def area(self):
        pass

class Triangle(Shape):
    def area(self):
        area = 0.50 * self.dim1 * self.dim2
        print("Area of triangle is ", area)

class Rectangle(Shape):
    def area(self):
        area = self.dim1 * self.dim2
        print("Area of Rectangle is ", area)

triangle = Triangle(2,3)
rectangle =  Rectangle(2,3)
triangle.area()
rectangle.area()

# objofshapeclass = Shape(2,3) # We can make an abstract class
# objofshapeclass.area()

