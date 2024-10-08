# Common ways to loop over a string

greeting = 'Hello'
for char in greeting:
	print(char)


# Looping over a string using range and len functions to get the position of each character
print("\n**********\n")

for i in range(len(greeting)):
	print(i)

# while loop with indexing
print("\n**********\n")

greeting = 'Hello'
index = 0
while index < len(greeting):
	print(greeting[index])
	index += 1

# List comprehensions
print("\n**********\n")

numbers = [1, 2, 3, 4, 5]
squared_numbers = [x ** 2 for x in numbers]
print(squared_numbers)

# Looping over the squared numbers -mine-
print("\n**********\n")
for number in squared_numbers:
	print(number)