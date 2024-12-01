# List comprehensions
# List comprehensions are a concise way to create lists. They consist of square brackets containing an expression followed by a for clause, then zero or more for or if clauses. The expressions can be anything, meaning you can put in all kinds of objects in lists.

# List comprehension syntax
# [expression for item in iterable]
# [expression for item in iterable if condition]
# [expression if condition else expression for item in iterable]

# [expression for variable in sequence]
print("\nList comprehension - expression for variable in sequence")
my_list = [x*2 for x in range(1,11)]
print(my_list)  # Outputs: [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# [expression for variable in sequence if condition]
print("\nList comprehension - expression for variable in sequence if condition")
my_list = [x for x in range(1,101) if x % 10 == 0]
print(my_list)  # Outputs: [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# Tuple does not have a list comprehension but similar to list comprehension,
# we can use a generator expression to create a tuple.

tuple(i for i in (1, 2, 3))
print(tuple(i*2 for i in (1, 2, 3)))
# Outputs: (2, 4, 6)
