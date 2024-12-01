# List-specific operations and methods
'''
- index
- append()
- insert()
- pop()
- remove()
- sort()
- reverse()
- clear()
- copy()
- extend()
- map()
- zip()

list[index] = x
list.append(x)
list.insert(index, x)
list.pop(index)
list.remove(x)
list.sort()
list.reverse()
list.clear()
list.copy()
list.extend(iterable)
list.map(function, iterable)
list.zip(iterable1, iterable2)

'''

# index
print("\nindex")
my_list = ['h', 'e', 'l', 'l', 'o']
print(my_list.index('l'))  # 2
# print(my_list.index('z'))  # ValueError
print(my_list.index('o'))  # 4
print(my_list.index('l', 3))  # 3

# append
print("\nappend")
my_list = ['h', 'e', 'l', 'l', 'o']
my_list.append(' ')
my_list.append('W')
my_list.append('o')
my_list.append('r')
my_list.append('l')
my_list.append('d')

print(my_list)  # ['h', 'e', 'l', 'l', 'o', ' ', 'W', 'o', 'r', 'l', 'd']

# insert
print("\ninsert")
my_list = ['h', 'e', 'l', 'l', 'o']
my_list.insert(3, ' ')
my_list.insert(4, 'W')
my_list.insert(5, 'o')
my_list.insert(6, 'r')
my_list.insert(7, 'l')
my_list.insert(8, 'd')

print(my_list)  # ['h', 'e', 'l', ' ', 'W', 'o', 'r', 'l', 'd', 'o']

# pop
print("\npop")
my_list = ['h', 'e', 'l', 'l', 'o']
print(my_list.pop())  # o
print(my_list.pop(0))  # h
print(my_list.pop(2))  # l
print(my_list)  # ['e', 'l']

# remove
print("\nremove")
my_list = ['h', 'e', 'l', 'l', 'o']
my_list.remove('l')
print(my_list)  # ['h', 'e', 'l', 'o']

# sort
print("\nsort")
my_list = ['h', 'e', 'l', 'l', 'o']
my_list.sort()
print(my_list)  # ['e', 'h', 'l', 'l', 'o']

# reverse
print("\nreverse")
my_list = ['h', 'e', 'l', 'l', 'o']
my_list.reverse()
print(my_list)  # ['o', 'l', 'l', 'e', 'h']

# clear
print("\nclear")
my_list = ['h', 'e', 'l', 'l', 'o']
my_list.clear()
print(my_list)  # []

# copy
print("\ncopy")
my_list = ['h', 'e', 'l', 'l', 'o']
my_list_copy = my_list.copy()
print(my_list_copy)  # ['h', 'e', 'l', 'l', 'o']

# extend
print("\nextend")
my_list = ['h', 'e', 'l', 'l', 'o']
my_list.extend([' ', 'W', 'o', 'r', 'l', 'd'])
print(my_list)  # ['h', 'e', 'l', 'l', 'o', ' ', 'W', 'o', 'r', 'l', 'd']

# map
print("\nmap")
my_list = ['h', 'e', 'l', 'l', 'o']
my_list = list(map(str.upper, my_list))
print(my_list)  # ['H', 'E', 'L', 'L', 'O']

# zip
print("\nzip")
my_list = ['h', 'e', 'l', 'l', 'o']
my_list = list(zip(my_list, ['H', 'E', 'L', 'L', 'O']))
print(my_list)  # [('h', 'H'), ('e', 'E'), ('l', 'L'), ('l', 'L'), ('o', 'O')]


