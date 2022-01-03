
class Person:
    name = "Rahat Abdullah"
    age = 5
    roll = 1001

    def displaydata(self):
        print("His name is " + self.name)

persobj1 = Person()
print(persobj1.name)
print(persobj1.age)
print(persobj1.roll)

print(persobj1.displaydata()) # Call by method

print(">>>>>>> Devider>>>>>>>>>>>>>>>>>>>>>>>>")
persobj1.name  = "His fathers name is Zakir Hossen"
print(persobj1.displaydata()) #will show displaydata concate and update of self.name