multiples = []
for x in range(1, 11):
    multiples.append(x*7)
print(multiples)

# List comprehension - the same in one line
print("\nList comprehension")
multiples = [x*7 for x in range(1, 11)]
print(multiples)

# List comprehension - Len languages
print("\nList comprehension - Len languages")
languages = ["Python", "Perl", "Ruby", "Go", "Java", "C"]
lenghts = [len(language) for language in languages]
print(lenghts)

# List comprehension - % 3
print("\nList comprehension - % 3")
z = [x for x in range(0, 101) if x % 3 == 0]
print(z)

# Reflect - List comprehension
print("\nReflect - List comprehension")

def odd_numbers(n):
	return [x for x in range(1, n+1) if x % 2 != 0]

print(odd_numbers(5))  # Should print [1, 3, 5]
print(odd_numbers(10)) # Should print [1, 3, 5, 7, 9]
print(odd_numbers(11)) # Should print [1, 3, 5, 7, 9, 11]
print(odd_numbers(1))  # Should print [1]
print(odd_numbers(-1)) # Should print []