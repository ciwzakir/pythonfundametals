"""
Same function name for different purposes
"""
class Shape():
    def __init__(self, dim1, dim2):
        self.dim1 = dim1
        self.dim2 = dim2

    def area(self):
        print("Shape has no area")

class Triangle(Shape):
    def area(self):
        area = 0.50 * self.dim1 * self.dim2
        print("Area of triangle is ", area)

class Rectangle(Shape):
    def area(self):
        area = self.dim1 * self.dim2
        print("Area of Rectangle is ", area)

objofshapeclass = Shape(2,3)
triangle = Triangle(2,3)
rectangle =  Rectangle(2,3)

objofshapeclass.area()
triangle.area()
rectangle.area()

