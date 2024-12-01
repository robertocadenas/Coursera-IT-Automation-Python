x = ["Now", "we", "are", "cooking!"]
type(x)
len(x)

print(x)
print(type(x))
print(len(x))

"are" in x
print("are" in x)
"Today" in x
print("Today" in x)

print(x[0])
print(x[3])
'''
print(x[4])
error: IndexError: list index out of range
'''
print(x[1:3])
print(x[:2])
print(x[2:])

# Reflect
print("\nReflect")

def get_word(sentence, n):
	# Only proceed if n is positive 
	if n > 0:
		words = sentence.split()
		# Only proceed if n is not more than the number of words 
		if n <= len(words):
			return(words[n-1])
	return("")

print(get_word("This is a lesson about lists", 4)) # Should print: lesson
print(get_word("This is a lesson about lists", -4)) # Nothing
print(get_word("Now we are cooking!", 1)) # Should print: Now
print(get_word("Now we are cooking!", 5)) # Nothing


