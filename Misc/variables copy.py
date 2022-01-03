
variable_is = """ Variable is like a container in which we can store value
Variables are case sensitive and can not be started with number (Like 1list)
We can assign all types of data into variable (string, int, float, tuple, list, set, dict) 
It may be class variable or instance variable

"""
print(variable_is)

a = "My name Zakir Hossen" # string must be enclosed (ভিতরে রাখা) into single or Double quotation
b = 32 # Integer is পূর্ণসংখ্যা
c = 32.00 #  Float is দশমিক সংখ্যা
d = True 
# Tuple is enclosed into first bracket and its value can not be changed 
# Tuple maintains the insertion order and also, allows us to store duplicate elements.
e = (1,2,3,4,5,6) 


# List is enclosed into Square / Third Bracket and it allows duplicate values
f = ["Rahim", "Karim", 'Modhu', "Ratan", "Ratan"]

# Set is enclosed into Curly / Second Bracket and it does not allow duplicate values. Its value is unique
g = {"Rahim", "Karim", 'Modhu', "Ratan"} 

# Dict is also enclosed into Curly / Second Bracket and it has keys and its value' Its Key is unique but value may be duplicate
h = {"Name": "Rahim", "Age":25, "Dept":"Finance", "Roll":12} 

print("Data Types Check")
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))
print(type(g))
print(type(h))