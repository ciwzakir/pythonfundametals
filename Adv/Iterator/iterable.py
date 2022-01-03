strings = "What my name is       "
int_num =12
float_Num = 12.15


number_in_tuple = (1,2,3)
player_list = ["Mosfiqur Rahim", "Tamim", 'Liton Das', "Sumya Sarkar"]
diner_sets = {"Plates", "Half Plates", 'Rice Serving Dish', "Tea Cup", "Curry Bowl"} 
dictionery = {"Come": "আসা", "Go":"যাওয়া", "eat":"খাওয়া", "understand":"বুঝতে পারা"} 

# print(dir(number_in_tuple))

values_of_tuple = number_in_tuple.__iter__()
print(values_of_tuple) # so tuple is iterable

values_of_list = player_list.__iter__()
print(values_of_list) # list tuple is iterable

values_of_set = diner_sets.__iter__()
print(values_of_set) # so set is iterable

values_of_dict = dictionery.__iter__()
print(values_of_dict) # so dict_key is iterable

values_of_strings = strings.__iter__()
print(values_of_strings) # so string is iterable

values_of_int_num = int_num.__iter__()
print(values_of_int_num) # so string is iterable