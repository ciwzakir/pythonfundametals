""" 
after single or double or more underscore used to avoid python defaault keyword name avoiding
its a name convention

"""
class Person:
    _name = "No Name"
    def set_name(self, name): # Parameter of constructor
        self._name = name # self.name = instance variable
     
        print(f"His name is  {self._name}")


# class = Person() # class keyword is a keyword it can not be taken a variable/ Here reference vaiable
# true = Person() # true keyword  is a keyword it can not be taken a variable/ Here reference vaiable
# false = Person() # false keyword is a keyword it can not be taken a variable/ Here reference vaiable
# and = Person() # and keyword is a keyword it can not be taken a variable/ Here reference vaiable
# or = Person() # or keyword is a keyword it can not be taken a variable/ Here reference vaiable
# in = Person() # in keyword is a keyword it can not be taken a variable/ Here reference vaiable

class_ = Person() # class_ is refence variable
class__ = Person() # class__ is refence variable
class___ = Person() # class___ is refence variable

class_._name = "Single underscore after reference variable"
print(f"Getting output ussing single underscore after reference variable {class_._name}")

class__._name = "Double underscore after reference variable"
print(f"Getting output using double underscore after reference variable {class__._name}")

class__._name = "More than double underscore after reference variable"
print(f"Getting output using ore than double underscore after reference variable {class__._name}")
