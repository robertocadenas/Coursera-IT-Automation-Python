# Tuple use cases
# Tuple is a collection of items which is ordered and unchangeable. In Python tuples are written with round brackets.
# Tuples are inmutable, so they can't be changed after they are created.
# Tuples are faster than lists.
# Tuples are used to protect data from being changed.

# tuple() operator
# The tuple() operator creates a tuple from an iterable.

# tuple() operato
print("\ntuple() operator")

# Convert a list to a tuple
my_list = [1, 2, 3, 4]
my_tuple = tuple(my_list)

print(my_tuple)  # Outputs: (1, 2, 3, 4)

# Remember that although parentheses are often used to define a tuple, 
# they're not always necessary. The following syntax is also valid:

my_tuple = 1, 2, 3, 4
print(my_tuple)  # Outputs: (1, 2, 3, 4)

# Tuples with mutable objects
print("\nTuples with mutable objects")

# A tuple with a list as an element
my_tuple = (1, 2, ['a', 'b', 'c'])

# You can't change the tuple itself
# my_tuple[0] = 3  # This would raise a TypeError

# But you can modify the mutable elements within the tuple
my_tuple[2][0] = 'x'  
print(my_tuple)  # Outputs: (1, 2, ['x', 'b', 'c'])

# Returning multiple values from functions
print("\nReturning multiple values from functions")

def calculate_numbers(a, b):
    return a+b, a-b, a*b, a/b

result = calculate_numbers(10, 2)
print(result)  # Outputs: (12, 8, 20, 5.0)

# Unpacking tuples
print("\nUnpacking tuples")

def calculate_numbers(a, b):
    return a+b, a-b, a*b, a/b

add_result, sub_result, mul_result, div_result = calculate_numbers(10, 2)
print(add_result)  # Outputs: 12
print(sub_result)  # Outputs: 8