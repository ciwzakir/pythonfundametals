"""
class is a template or plan or blueprint
we can create objects using a class
class keyword start always with small letter class
then class name start with Capital letter
class is a keyword. It has
    state = Properties
    behaviour = start(), run(), stop(), brake()
"""

class Car: # Head of the class
    name = "Toyota"  # name, color and cc are the properties/fields/attributes of class Car
    color = "Red"    #three lines are body of the class
    cc = 2500         #class has also scope
# print(Car)

"""
variables, functions, lists, tuples, set dict all are objects
object works with class
syntax of a class
objectsName is small letter
nameOfObject= className()
see bellow
object print objectname.classProperty
"""

objectsOne = Car() # objectsOne is called the object of class Car()
objectstwo = Car() # objectstwo is the object of class Car()
objectsthree = Car() # objectsthree is the object of class Car()


print("........................")
print("The name of your car is " + objectsOne.name)
print("and the color of your car is " + objectsOne.color)
print("and the color of your car is " + str(objectsOne.cc)) #string and number concatenate at a time

print(">>>>>>> Devider >>>>>>>>>")

objectstwo.name = "Honda"
objectsthree.name = "Mercedeeze"
objectsthree.cc = 3000

print(objectsOne.name)
print(objectstwo.name)
print(objectsthree.name)
print(objectsthree.cc)
