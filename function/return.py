

def add_function(first_parameter, second_parameter):
    return first_parameter + second_parameter * 12  # return method

first = int(input("Insert your first number : " ))
second = int(input("Insert your second number : " ))
sum = add_function(first, second)


print(f"The sum of the two valus are {sum}")

a = add_function(5,4)
print(f"The value of a is {a}")