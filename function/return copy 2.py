

def calculation_function(first_parameter, second_parameter):
    add = first_parameter + second_parameter
    sub = first_parameter - second_parameter
    multiply = first_parameter * second_parameter
    division = first_parameter / second_parameter
    return add, sub, multiply, division   # return method

# print(calculation_function(20,20))

output = calculation_function(20, 10)
print(output)