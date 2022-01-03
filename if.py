"""
print("Conditional statement or Data control  Flow or if Statements:")
a = 1000
b = 10000
if a>b:
    print("a is greater than b")
elif a==b:
    print("a and b are equal")
else:
    print("a is lesser than b")
    print("and this line is a block of else")
    print("As well as this line is under the scope of else")

print("This line out of if else block and and scope")

"""

taxrate =0
taxamount= 15


if taxrate >= 0 and taxamount ==0:
    print(taxrate)
          
elif taxrate == 0 and taxamount >=0:
    print(taxamount)
else:
    print("Insert TAX Correctly")
         