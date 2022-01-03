
int_num =12
float_Num = 12.15
bool_check = True
number_in_tuple = (1,2,3)

# print(dir(number_in_tuple))

# values_of_int_num = int_num.__iter__()
# print(values_of_int_num) # int number is not  iterable

# values_of_float_Num = float_Num.__iter__()
# print(values_of_float_Num) # float_Num is not  iterable

# values_of_bool_check = bool_check.__iter__()
# print(values_of_bool_check) # boolean is not  iterable

values_of_tuple = number_in_tuple.__iter__()
print(values_of_tuple) # so tuple is iterable
