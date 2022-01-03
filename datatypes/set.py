"""
The Set data type in Python is represented using a set class.

We can create a Set using the two ways

By enclosing values in the curly brackets {}
Using a set() class.
The set data type has the following characteristics.

It is mutable which means we can change set items
Duplicate elements are not allowed
Heterogeneous (values of all data types) elements are allowed
Insertion order of elements is not preserved, so we can’t perform indexing on a Set

"""
my_set = {100, 25.75, "Jessa"}
print(my_set)  # {25.75, 100, 'Jessa'}
print(type(my_set))  # class 'set'
print(".....................................")

my_set = set({100, 25.75, "Jessa"})
print(my_set)  # {25.75, 100, 'Jessa'}
print(type(my_set))  # class 'set'

# add element to set
my_set.add(300)
print(my_set)  # {25.75, 100, 'Jessa', 300}

# remove element from set
my_set.remove(100)
print(my_set)  # {25.75, 'Jessa', 300}