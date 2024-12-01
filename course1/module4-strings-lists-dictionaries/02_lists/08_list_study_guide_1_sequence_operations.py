'''
Common sequence operations - both lists and strings are tuples
- len()
- max()
- min()
- sum()
- in
- not in
- concatenation
- repetition
- indexing
- slicing
- iteration
- list comprehension
'''

my_string = 'hello World'
my_list = ['h', 'e', 'l', 'l', 'o']
my_tuple = ('h', 'e', 'l', 'l', 'o')

# len()
print("\nlen()")
print(len(my_string))  # 5
print(len(my_list))  # 5
print(len(my_tuple))  # 5

# max()
print("\nmax()")
print(max(my_string)) # 'r'
print(max(my_list))  # 'o'
print(max(my_tuple))  # 'o'

# min()
print("\nmin()")
print(min(my_string)) # 'W'
print(min(my_list))  # 'e'
print(min(my_tuple))  # 'e'

# sum()
print("\nsum()")
# print(sum(my_string))  # TypeError: unsupported operand type(s) for +: 'int' and 'str'
# print(sum(my_list))  # TypeError: unsupported operand type(s) for +: 'int' and 'str'
# print(sum(my_tuple))  # TypeError: unsupported operand type(s) for +: 'int' and 'str'

# in
print("\nin")
print('h' in my_string)  # True
print('h' in my_list)  # True
print('h' in my_tuple)  # True

# not in
print("\nnot in")
print('z' not in my_string)  # True
print('z' not in my_list)  # True
print('z' not in my_tuple)  # True

# concatenation
print("\nconcatenation")
print(my_string + ' World')  # hello World World
print(my_list + ['W', 'o', 'r', 'l', 'd'])  # ['h', 'e', 'l', 'l', 'o', 'W', 'o', 'r', 'l', 'd']
print(my_tuple + ('W', 'o', 'r', 'l', 'd'))  # ('h', 'e', 'l', 'l', 'o', 'W', 'o', 'r', 'l', 'd')

# repetition
print("\nrepetition")
print(my_string * 2)  # hello Worldhello World
print(my_list * 2)  # ['h', 'e', 'l', 'l', 'o', 'h', 'e', 'l', 'l', 'o']
print(my_tuple * 2)  # ('h', 'e', 'l', 'l', 'o', 'h', 'e', 'l', 'l', 'o')

# indexing
print("\nindexing")
print(my_string[0])  # h
print(my_list[0])  # h
print(my_tuple[0])  # h

# slicing
print("\nslicing")
print(my_string[0:5])  # hello
print(my_list[0:5])  # ['h', 'e', 'l', 'l', 'o']
print(my_tuple[0:5])  # ('h', 'e', 'l', 'l', 'o')

# iteration
print("\niteration")
for i in my_string:
    print(i, end=' ')  # h e l l o
print()

for i in my_list:
    print(i, end=' ')  # h e l l o 
print()

for i in my_tuple:
    print(i, end=' ')  # h e l l o
print()

# list comprehension
print("\nlist comprehension")
my_list = [i for i in range(5)]
print(my_list)  # [0, 1, 2, 3, 4]

my_list = [i for i in 'hello']
print(my_list)  # ['h', 'e', 'l', 'l', 'o']

my_list = [i for i in (1, 2, 3, 4, 5)]
print(my_list)  # [1, 2, 3, 4, 5]

my_list = [i for i in ['h', 'e', 'l', 'l', 'o']]
print(my_list)  # ['h', 'e', 'l', 'l', 'o']

my_list = [i for i in {'h', 'e', 'l', 'l', 'o'}]
print(my_list)  # ['h', 'e', 'l', 'o']

my_list = [i for i in {'h': 1, 'e': 2, 'l': 3, 'o': 4}]
print(my_list)  # ['h', 'e', 'l', 'o']
'''
'''
