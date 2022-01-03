"""
Dictionary has some characteristics which are listed below:

A heterogeneous (i.e., str, list, tuple) elements are allowed for both key and value in a dictionary.
The dictionary is mutable which means we can modify its items
Dictionary is unordered so we can’t perform indexing and slicing

We can create a dictionary using the two ways

By enclosing key and values in the curly brackets {}
Using a dict() class.

"""

"""
In a dictionary, duplicate keys are not allowed,
but the value can be duplicated. If we try to insert a value with a duplicate key,
the old value will be replaced with the new value.

"""
# create a dictionary
my_dict = {1: "Smith", 2: "Emma", 3: "Jessa"}

# display dictionary
print(my_dict)  # {1: 'Smith', 2: 'Emma', 3: 'Jessa'}
print(type(my_dict))  # class 'dict'

# create a dictionary using a dit class
my_dict = dict({1: "Smith", 2: "Emma", 3: "Jessa"})

# display dictionary
print(my_dict)  # {1: 'Smith', 2: 'Emma', 3: 'Jessa'}
print(type(my_dict))  # class 'dict'

# access value using a key name
print(my_dict[1])  # Smith

# change the value of a key
my_dict[1] = "Kelly"
print(my_dict[1])  # Kelly