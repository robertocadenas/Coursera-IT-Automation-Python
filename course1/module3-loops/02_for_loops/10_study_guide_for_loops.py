# For loop with range

# This loop iterates on the value of the "number" variable in a range
# of 1 to 6+1 (the upper range limit of 6 is excluded, so +1 has
# been added to it to include 6 in the range). The incremental value
# for the loop is 2 (number+2). The print() function will output the
# resulting value of "number" multiplied by 3.

for number in range(1, 6+1, 2):
    print(number * 3)

# The loop should print 3, 9, 15

# Common pitfalls when using the range() function:
print("\nCommon pitfalls when using the range() function:")

# 1. The range() function does not include the upper limit value

# This loop iterates on the value of the "number" variable in a range
# of 2 to 7 (the upper range limit of 8 is excluded). The print() 
# function will output the resulting value of "number" squared.

for number in range(2,8):
    print(number**2)

# The loop should print 4, 9, 16, 25, 36, 49

# Nested for Loops
print("\nNested for Loops:")

for x in range(2):
    print("This is the outer loop iteration number " + str(x))
    for y in range(3+1):
        print("Inner loop iteration number " + str(y))
    print("Exit inner loop")

# for loop with nested if Statement
print("\nFor loop with nested if Statement:")

# This for loop iterates through the numbers 0 to 6. The if statement
# uses the modulo operator to test if the "x" variable is divisible by
# 2. If True, the if statement will print the value of "x" and exit
# back into the for loop for the next iteration of "x". Since no 
# incremental value is specified in the range() parameters, the default
# increment is +1. 

for x in range(7):
    if x % 2 == 0:
        print(x)

# The loop should print 0, 2, 4, 6

# As a list comprehension:
even_numbers = [x for x in range(7) if x % 2 == 0]
print(even_numbers)

# List comprehensions
print("\nList comprehensions:")

sequence = range(10)
new_list = []
for x in sequence:
    if x % 2 == 0:
        new_list.append(x)

print(new_list)

# With list comprehension:
sequence = range(10)
new_list = [x for x in sequence if x % 2 == 0]
print(new_list)

# An example of a useful one-liner is
print("*" * 8)