
def functions_Details():
    print("Function is a block of code that only runs when it is called by its name")
    print("A function can return data as a result")
    print("There are parenthesis just after function name")
    print("We can pass any number of parameter into the parenthesis")
    print("We can pass data as a parameter into the function")
    print("We must called a function outside the Scope of the function block")
    print("function name must start with small/running letter or camelCase or underscore ")
    print("but python recommentes underscore")
print("This line will not be shown because it not a part of function. It is outside the scope of this function block")

functions_Details() #  call of a function

print("=====================================")
# Syntax of a function
def function_name(first_name, last_name):
    print(f"His name is {first_name} {last_name}") # print method
    print("His name is " + first_name + " "+  last_name) # same output print method

function_name("Imran", "Kabir")


