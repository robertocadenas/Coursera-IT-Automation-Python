def is_power_of_two(number):
  # This while loop checks if the "number" can be divided by two
  # without leaving a remainder. How can you change the while loop to
  # avoid a Python ZeroDivisionError?
  if number == 0:
    return False
  while number % 2 == 0:
    number = number / 2
  # If after dividing by 2 "number" equals 1, then "number" is a power
  # of 2.
  if number == 1:
    return True
  return False
  
# Calls to the function
print(is_power_of_two(0)) # Should be False
print(is_power_of_two(1)) # Should be True
print(is_power_of_two(8)) # Should be True
print(is_power_of_two(9)) # Should be False

# Sum of integers

def sum_of_integers(n):
  if n < 1:
    return 0
  i = 1
  sum = 0
  while i <= n:
    sum = sum + i
    i = i + 1
  return sum


print(sum_of_integers(3))  # should print 6
print(sum_of_integers(4))  # should print 10
print(sum_of_integers(5))  # should print 15

# Multiplication table

def multiplication_table(number):
    # Initialize the appropriate variable
    multiplier = 1
    result = 0


    # Complete the while loop condition.
    while result <= 25:
        result = number * multiplier 
        if  result > 25 or multiplier > 5:
            # Enter the action to take if the result > 25
            break
        print(str(number) + "x" + str(multiplier) + "=" + str(result))
        
        # Increment the appropriate variable
        multiplier += 1




multiplication_table(3) 
# Should print: 
# 3x1=3 
# 3x2=6 
# 3x3=9 
# 3x4=12 
# 3x5=15


multiplication_table(5) 
# Should print: 
# 5x1=5
# 5x2=10
# 5x3=15
# 5x4=20
# 5x5=25


multiplication_table(8) 
# Should print:
# 8x1=8
# 8x2=16
# 8x3=24