"""
before and after
it means special to Python like __init__ or __main__

"""
class Person:

    def __init__(self, name, date_of_birth, age): # Parameter of constructor
        self.name = name # self.name = instance variable
        self._dob = date_of_birth #  Single underscore used for weak private not encapsulatoin can be accesed by instance variable
        self.__age = age # Double underscore used for stronger  private and  encapsulation. can not be called directly by instance varriable


    def biodata(self): #  instance method
        return f"He/She is {self.name} and his/ her date of birth is {self._dob}, as well as he/ she is {self.__age} years old"


Person1 = Person("Zakir Hossen", "07 Jan 1990", 32)
Person2 = Person("Rahat Abdullah", "18 Jun 2016", 5)

print(Person1.biodata()) # Called by instance Method / funtion
print(Person2.biodata()) # Called by instance Method / funtion