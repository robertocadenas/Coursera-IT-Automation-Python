# there are a lot of things you can do with strings
# here are some examples

# string operations
print("string operations")

# len(string)
print("\nlen(string)")
print(    len("abcde"))  # prints 5

# for character in string - Iterates over each character in the string
print("\nfor character in string")
for c in "abcde": print(c)    

# if substring in string - Checks whether the substring is part of the string
print("abc" in "abcde") # Prints True
print("def" in "abcde")  # Prints False


# string[i] - Accesses the character at index i of the string, starting at zero
print("\nstring[i]")

print("abcde"[2])  # prints "c"
print("abcde"[-1]) # prints "e"


# string methods
print("\nstring methods")

# string.lower() - Returns a copy of the string with all lowercase characters
print("\nstring.lower()")
print("AaBbCcDdEe".lower()) # prints "aabbccddee"

# string.upper() - Returns a copy of the string with all uppercase characters
print("\nstring.upper()")
print("AaBbCcDdEe".upper()) # prints "AABBCCDDEE"

# string.lstrip() - Returns a copy of the string with the left-side whitespace removed
print("\nstring.lstrip()")
print("   Hello   ".lstrip()) # prints "Hello   "

# string.rstrip() - Returns a copy of the string with the right-side whitespace removed
print("\nstring.rstrip()")
print("   Hello   ".rstrip()) # prints "   Hello"

# string.strip() - Returns a copy of the string with both the left and right-side whitespace removed
print("\nstring.strip()")
print("   Hello   ".strip()) # prints "Hello"

# string.count(substring)- Returns the number of times substring is present in the string
print("\nstring.count(substring)")
test = "How much wood would a woodchuck chuck"
print(test.count("wood")) # prints 2

# string.isnumeric() - Returns True if there are only numeric characters in the string. If not, returns False.
print("\nstring.isnumeric()")
print("12345".isnumeric()) # prints True
print("-123.45".isnumeric()) # prints False

# string.isalpha() - Returns True if there are only letters in the string. If not, returns False.
print("\nstring.isalpha()")
print("xyzzy".isalpha()) # prints True
print("xyzzy0".isalpha())# prints False

# string.split() - Returns a list of substrings that were separated by whitespace (whitespace can be a space, tab, or new line)
print("\nstring.split()")
print(test.split()) # prints ['How', 'much', 'wood', 'would', 'a', 'woodchuck', 'chuck']

# string.split(delimiter) - Returns a list of substrings that were separated by whitespace or another string
print("\nstring.split(delimiter)")
test = "How-much-wood-would-a-woodchuck-chuck"
print(test.split(" "))# prints ['How', 'much', 'wood', 'would', 'a', 'woodchuck', 'chuck']

# string.replace(old, new) - Returns a new string where all occurrences of old have been replaced by new.
print("\nstring.replace(old, new)")
print(test.replace("wood", "plastic")) # prints "How much plastic would a plasticchuck chuck"

# delimiter.join(list of strings) - Returns a new string with all the strings joined by the delimiter
print("\ndelimiter.join(list of strings)")
test = "How-much-wood-would-a-woodchuck-chuck"
print("-".join(test.split())) # prints "How-much-wood-would-a-woodchuck-chuck"
