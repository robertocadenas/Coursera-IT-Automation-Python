# Apend
print("\nAppend")

fruits = ["Pineapple", "Banana", "Apple", "Melon"]
fruits.append("Kiwi")
print(fruits)

# Insert
print("\nInsert")

fruits = ["Pineapple", "Banana", "Apple", "Melon"]
fruits.insert(0, "Orange")
print(fruits)

fruits = ["Pineapple", "Banana", "Apple", "Melon"]
fruits.insert(0, "Orange")
fruits.insert(25, "Peach")
print(fruits)  

# Remove
print("\nRemove")

fruits.remove("Melon")
print(fruits)

'''
fruits = ["Pineapple", "Banana", "Apple", "Melon"]
fruits.remove("Pear")
error: ValueError: list.remove(x): x not in list
'''

# Pop
print("\nPop")

fruits = ["Pineapple", "Banana", "Apple", "Melon"]
fruits.insert(0, "Orange")
fruits.insert(25, "Peach")
fruits.remove("Melon")
fruits.pop(3)
print(fruits)

