""" 
Encapsulation / Private method
Encapsulation must be  called by method/Function  
Single and Double underscore used just before variable name (prefix) 
"""
class Person:

    def __init__(self, name, date_of_birth, age): # Parameter of constructor
        self.name = name # self.name = instance variable
        self._dob = date_of_birth #  Single underscore used for weak private not encapsulatoin can be accesed by instance variable
        self.__age = age # Double underscore used for stronger  private and  encapsulation. can not be called directly by instance varriable


    def biodata(self): #  instance method
        return f"Name {self.name}, Date of Birth : {self._dob}, Age : {self.__age}"


Person1 = Person("Zakir Hossen", "07 Jan 1990", 32)

print(Person1.biodata()) # Called by instance Method / funtion
print(Person1.name) # Directly called by instance variable name_of_object.instance_variable_name without self
print(Person1._dob) # Can  be directly called by instance variable name_of_object.instance_variable_name without self. must call by method/functon name

"""
print(Person1.__age) # Can not directly called by instance variable name_of_object.instance_variable_name without self. must call by method/functon name

"""
