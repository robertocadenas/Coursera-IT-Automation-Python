# print the even numbers from 2 to 12.
print("\nEven numbers function")

number = 2 # Initialize the variable 
while number <= 12: # Complete the while loop condition
    print(number, end=" ")
    number += 2 # Increment the variable

# Should print 2 4 6 8 10 12 

# The loop should check each number from 1 to 5 and identify if the number is odd or even.  
print("\nOdd or Even")

for number in range(1, 5+1):
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


print("rows_asterisks function")
# This function should print rows of asterisks (*), where the number of rows is equal to the “rows” variable. 

def rows_asterisks(rows):
    # Complete the outer loop range to control the number of rows
    for x in range(1, rows+1): 
        # Complete the inner loop range to control the number of 
        # asterisks per row
        for y in range(x): 
            # Prints one asterisk and one space
            print("*", end=" ")
        # An empty print() function inserts a line break at the 
        # end of the row 
        print()


rows_asterisks(5)
# Should print the asterisk rows shown above


# Divisble function
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

# This function should return a space-separated string of all odd positive numbers, up to and including the “maximum” variable that's passed into the function.
print("\nOdd numbers function")

def odd_numbers(maximum):
    
    return_string = "" # Initializes variable as a string

    # Complete the for loop with a range that includes all 
    # odd numbers up to and including the "maximum" value.
    for x in range(maximum + 1): 

        # Complete the body of the loop by appending the odd number
        # followed by a space to the "return_string" variable.
        if x % 2 != 0 or x == 1:
            return_string += str(x) + " "   

    # This .strip command will remove the final " " space 
    # at the end of the "return_string".
    return return_string.strip()


print(odd_numbers(6))  # Should be 1 3 5
print(odd_numbers(10)) # Should be 1 3 5 7 9
print(odd_numbers(1))  # Should be 1
print(odd_numbers(3))  # Should be 1 3
print(odd_numbers(0))  # No numbers displayed

'''
NameError: name 'z' is not defined
for x in range(10):
    if z < x:
        print(x)
'''

for count in range(1, 6):
    print(count+1)

#inner and outer loop
print("\nInner and outer loop")
for outer_loop in range(2, 6+1):
    for inner_loop in range(outer_loop):
        print("outer loop: " + str(outer_loop))
        if inner_loop % 2 == 0:
            print(inner_loop)


# Fixing the code
print("\nFixing the code")

def test_code(num):
  x = num
  while x % 2 == 0 and x != 0:
    x = x / 2
    print(x)

test_code(0)
test_code(10)