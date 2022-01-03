""" 

before Single underscore means weak private
Double underscore used for strong private encapsulation
"""
class Person:
    _name = "No Name"
    def set_name(self, name): # Parameter of constructor
        self._name = name # self.name = instance variable
     
        print(f"His name is  {self._name} and his age is ")


person1 = Person()

person1.set_name("Rahat Abdullah Ibne Zakir") 
print(f"weak private {person1._name}")

person1._name = "Oh no! actually his real name is emu"
print(f"weak private {person1._name}")