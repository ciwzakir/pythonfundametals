# Encapsulation / Private method
class Person:

    def __init__(self, name, date_of_birth, age): # Parameter of constructor
        self.name = name # self.name = instance variable
        self.__dob = date_of_birth # encapsulation must be  called by method    
        self.__age = age # underscore underscore used for encapsulation. can not be called directly by instance varriable


    def biodata(self): #  instance method
        return f"Name {self.name}, Date of Birth : {self.__dob}, Age : {self.__age}"


Person1 = Person("Zakir Hossen", "07 Jan 1990", 32)

print(Person1.biodata()) # Called by instance Method
print(Person1.name) # Directly called by instance variable name_of_object.instance_variable_name without self

"""
print(Person1.__dob) # Can not directly called by instance variable name_of_object.instance_variable_name without self. must call by method/functon name

"""