# First step to fix a type y locate the index

animals = "lions tigers and bears"
animals.index("g")
print(animals)
print("\'g\' in " + animals + " is in index: " + str(animals.index("g")))

animals = "lions tigers and bears"
animals.index("bears")
print("\'bears\' in " + animals + " is in index: " + str(animals.index("bears")))

# Avoid a ValueError by first checking if the substring exists in the string
print("\nAvoid a ValueError by first checking if the substring exists in the string")

"horses" in animals
print("horses" in animals)

animals = "lions tigers and bears"
"tigers" in animals
print("tigers" in animals)

# Mine
print("\nMine")

animals = "lions tigers and bears"
def find_index(animals, substring):
    if substring in animals:
        return animals.index(substring)
    else:
        return -1
    
print(find_index(animals, "g"))
print(find_index(animals, "bears"))
print(find_index(animals, "horses"))
