# Base class/ Parents class /Sperclass
class Person:

    def __init__(self, name, height, age, marital_status, date_of_birth, no_of_child, education): # Parameter of constructor
        self.name = name # self.name = instance variable
        self.height = height # after = always place parameter name of constructor
        self.age = age
        self.marital_status = marital_status
        self.dob = date_of_birth
        self.no_of_child = no_of_child
        self.education  =   education


    def biodata(self): #  instance method
        # print(self.name, self.height, self.age, self.marital_status, self.no_of_child, self.education, self.dob)
        return f"Name {self.name}, Height : {self.height}, Date of Birth : {self.dob}, Age : {self.age}, Marrial Status :{self.marital_status}, No of Children : {self.no_of_child},Education : {self.education}"

name = "Zakir Hossen"
height = float(6.7)
age = 20
ms = "Married"
dob = "Jan 1990"
noc = 2
education = "Graduate"


Person1 = Person(name, height, age, ms, dob, noc, education)
print(Person1.biodata()) #  calling instance method