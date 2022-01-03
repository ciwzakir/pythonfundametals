"""

Tuples are ordered collections of elements that are unchangeable. The tuple is the same as the list, except the tuple is immutable means we can’t modify the tuple once created.

In other words, we can say a tuple is a read-only version of the list.

For example: If you want to store the roll numbers of students that you don’t change, you can use the tuple data type.

Note: Tuple maintains the insertion order and also, allows us to store duplicate elements.

We can create a tuple using the two ways

By enclosing elements in the parenthesis ()
Using a tuple() class.


"""

# create a tuple
my_tuple = (11, 24, 56, 88, 78)
print(my_tuple)  # (11, 24, 56, 88, 78)
print(type(my_tuple))  # class 'tuple'

# Accessing 3rd element of a tuple
print(my_tuple[2])  # 56

# slice a tuple
print(my_tuple[2:7])  # (56, 88, 78)

# create a tuple using a tuple() class
my_tuple2 = tuple((10, 20, 30, 40))
print(my_tuple2)  # (10, 20, 30, 40)


# A tuple is immutable means once we create a tuple, we can’t modify it

# create a tuple
my_tuple = (11, 24, 56, 88, 78)

# modify 2nd element of tuple
my_tuple[1] = 35
print(my_tuple)
# TypeError: 'tuple' object does not support item assignment