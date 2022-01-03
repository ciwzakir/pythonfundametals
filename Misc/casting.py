# string and number can not be concatinate at a time. So we should casting it
name = "Zakir"
age = 32
print("The name of the student is " + name + " and his/her age is "+ str(age)) 

name = "Rahim"
age = str(33)
print("The name of the student is " + name + " and his/her age is " + age) 

# or formating
print("<<<<<<<<<<<<<<<<<  Formating  >>>>>>>>>>>>>>>>")
print(f"The name of the students is {name} and his / her age is {age}")