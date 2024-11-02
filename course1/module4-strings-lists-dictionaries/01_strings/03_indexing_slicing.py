fruit = "Mangosteen"
print(fruit[1:4]) # prints 'ang' beginning at index 1 and ending at index 4 (El index 1 si se incluye y el index 4 no se incluye)
print(fruit[:5]) # prints 'Mango' beginning at index 0 and ending at index 5 (El index 5 no se incluye)
print(fruit[5:]) # prints 'steen' beginning at index 5 and ending at the last index
print(fruit[:5] + fruit[5:]) # prints 'Mangosteen' concatenating the two slices