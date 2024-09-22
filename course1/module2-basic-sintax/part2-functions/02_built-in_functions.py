# The built-in function print() is used to display the output on the screen.

month = "September"
print("Investigate failed login attempts during", month, "if more than", 100)


# The built-in function type() is used to determine the data type of a variable.
# And passing one function into another
print(type("security"))
print(type(99))
print(type(99.9))
print(type("This is a string"))


# str() function converts the value passed to it into a string.
number = 12
string_representation = str(number)
print(string_representation)

# sorted() function sorts the elements of a given iterable in a specific order (either ascending or descending).
time_list = [12, 2, 32, 19, 57, 22, 14]
print(sorted(time_list))

desordenado = "Hola, mundo"
print(sorted(desordenado))

time_list = [12, 2, 32, 19, 57, 22, 14]
print(sorted(time_list))
print(time_list)

# max() function returns the largest item in an iterable or the largest of two or more arguments.
# min() function returns the smallest item in an iterable or the smallest of two or more arguments.
print(max(time_list))
print(min(time_list))
print(max(desordenado))
print(min(desordenado))
