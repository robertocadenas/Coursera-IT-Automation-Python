# Upper and lower case methods
"Mountains".upper()
"Mountains".lower()
print("Mountains".upper())
print("Mountains".lower())

# Control example
print("\nControl example")

answer = "YES"
if answer.lower() == "yes":
  print("User said yes")

# Strip methods
print("\nStrip methods")
" yes ".strip()
" yes ".lstrip()
" yes ".rstrip()
print(" yes ".strip())
print(" yes ".lstrip())
print(" yes ".rstrip())

# Count method
print("\nCount method")

"The number of times e occurs in this string is 4".count("e")
print("The number of times e occurs in this string is 4".count("e"))
print("The number of times x occurs in this string is 4".count("x"))

# Endswith method
print("\nEndswith method")
"Forest".endswith("rest")
print("Forest".endswith("rest"))

# Isnumeric method
print("\nIsnumeric method")
"Forest".isnumeric()
"12345".isnumeric()
print("Forest".isnumeric())
print("12345".isnumeric())

int("12345") + int("54321")
print(int("12345") + int("54321"))

# Join method
print("\nJoin method")
" ".join(["This", "is", "a", "phrase", "joined", "by", "spaces"])
"...".join(["This", "is", "a", "phrase", "joined", "by", "triple", "dots"])
print(" ".join(["This", "is", "a", "phrase", "joined", "by", "spaces"]))
print("...".join(["This", "is", "a", "phrase", "joined", "by", "triple", "dots"]))

# Split method
print("\nSplit method")
"This is another example".split()
print("This is another example".split())
