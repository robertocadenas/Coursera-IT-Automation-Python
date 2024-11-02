# Fill in the blanks to print the numbers from 15 to 5, counting down by fives.
print("\nFill in the blanks to print the numbers from 15 to 5, counting down by fives")

number = 15 # Initialize the variable
while number >= 5: # Complete the while loop condition
    print(number, end=" ")
    number -= 5 # Increment the variable

# Should print 15 10 5 

# The loop should check each number from 1 to 5 and identify if the number is odd or even.  

for number in range(5+1):
    if number % 2 == 0:
        print("even")
    else:
        print("odd")


# Should print:
# odd
# even
# odd
# even
# odd

# This function will accept an integer variable “n” through the function parameters and produce the factorials of this number (by multiplying this value by every number less than the original number [n*(n-1)], excluding 0).  

print("\nFactorial function")

def factorial(n):
    result = n
    start = n
    n -= 1
    while n > 0: # The while loop should execute as long as n is greater than 0
        result *= n # Multiply the current result by the current value of n
        n -= 1 # Decrement the appropriate variable by -1
    return result


print(factorial(3)) # Should print 6
print(factorial(9)) # Should print 362880
print(factorial(1)) # Should print 1

# . This function should print a multiplication table, where each number is the result of multiplying the first number of its row by the number at the top of its column.
print("\nMultiplication table")

def multiplication_table(start, stop):
    # Complete the outer loop range
    for x in range(start, stop+1): 
         # Complete the inner loop range
        for y in range(start, stop+1):
            # Prints the value of "x" multiplied by "y" 
            # and inserts a space after each value
            print(str(x*y), end=" ")
        # An empty print() function inserts a line break at the 
        # end of the row 
        print()


multiplication_table(1, 3)
# Should print the multiplication table shown above


# his function should count the number of values from 0 to the “max” parameter minus 1 that are evenly divisible by the “divisor” parameter. 
print("\nDivisible function")

def divisible(max, divisor):
    count = 0 # Initialize an incremental variable
    for x in range(max): # Complete the for loop
        if x % divisor == 0:
            count += 1 # Increment the appropriate variable
    return count

print(divisible(100, 10)) # Should be 10
print(divisible(10, 3)) # Should be 4
print(divisible(144, 17)) # Should be 9


# This function should return a space-separated string of all positive even numbers, excluding 0, up to and including the “maximum” variable that's passed into the function. 
print("\nEven numbers function")

def even_numbers(maximum):

    return_string = "" # Initializes variable as a string

    # Complete the for loop with a range that includes all even numbers
    # up to and including the "maximum" value, but excluding 0.
    for x in range(2, maximum+1, 2): 

        # Complete the body of the loop by appending the even number
        # followed by a space to the "return_string" variable.
        return_string += str(x) + ' '  

    # This .strip command will remove the final " " space at the end of
    # the "return_string".
    return return_string.strip() 

print(even_numbers(6))  # Should be 2 4 6
print(even_numbers(10)) # Should be 2 4 6 8 10
print(even_numbers(1))  # No numbers displayed
print(even_numbers(3))  # Should be 2
print(even_numbers(0))  # No numbers displayed

# add together all numbers from x to 10
print("\nSum of numbers function")

x = 1
sum = 0
while x <= 10:
    sum += x
    x += 1
print(sum)
# Should print 55

# Iteration
print("\nIteration")

for count in range(1, 6):
    print(count+1)

# loop
print("\nLoop")

num1 = 0
num2 = 0

for x in range(5):
    num1 = x
    for y in range(14):
        num2 = y + 3

print(num1 + num2)

# loop
print("\nLoop")

def count_to_ten():
  # Loop through the numbers from first to last 
  x = 1
  while x <= 10:
    print(x)
    x += 1


count_to_ten()
# Should print:
# 1
# 2
# 3 
# 4
# 5
# 6
# 7
# 8 
# 9
# 10
