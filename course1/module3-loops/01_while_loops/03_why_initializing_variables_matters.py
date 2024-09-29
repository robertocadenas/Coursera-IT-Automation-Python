# If my_variable is not initialized, the while loop will not run. NameError: name 'my_variable' is not defined
my_variable = 5
while my_variable < 10:
    print("Hello")
    my_variable += 1


x = 1
sum = 0
while x < 10:
    sum = sum + x
    x = x + 1

product = 1
while x < 10: # This loop will not run because x is already 10
    product = product * x
    x = x + 1

print(sum, product)
#Ouput 45 1


def count_down(start_number):
  current = start_number
  while (current > 0):
    print(current)
    current -= 1
  print("Zero!")

count_down(3)