# How to slice strings 
print("\n How to slice strings\n")

string1 = "Greetings, Earthlings"
print(string1[0])   # Prints “G”
print(string1[4:8]) # Prints “ting”
print(string1[11:]) # Prints “Earthlings”
print(string1[:5])  # Prints “Greet”

print("\n playing \n")
print(string1)
print(string1[:])   # Prints “Greetings, Earthlings”
print(string1[-1])  # Prints “s”
print(string1[::2]) # Prints “Getns atrns”
print(string1[::-1])# Prints “sgnilhtraE ,sgniteerG”


# Negative indices
print("\n Negative indices\n")
print(string1[-10:]) # Prints “Earthlings” again

#beyond the end of the string
print("\n beyond the end of the string\n")
print(string1[55:]) # Prints “” 

# How to join strings
print("\n How to join strings\n")

# Plus operator
print("\n Plus operator\n")
print("Hello" + " " + "world") #Prints “Hello world”

# Join method
greetings = ["Hello", "world"]
print(" ".join(greetings)) # Prints "Hello world"
# You can also concatenate a combination of strings and variables like in the following example.
name = "Alice"
print("Hello, " + name + "!") # Prints "Hello, Alice!"

# How to combine slicing and joining strings
print("\n How to combine slicing and joining strings\n")

# The first 3 digits are the area code:
phonenum = "2025551212"
print(phonenum)
area_code = "(" + phonenum[:3] + ")"
print(area_code) # Prints “(202)”

# The next 3 digits are called the “exchange”:
exchange = phonenum[3:6]
print(exchange) # Prints “555”

# The next 3 digits are the line number:
line = phonenum[-4:]
print(line) # Prints “1212”

# Put the pieces back together into a nicely formatted string:
print(area_code + " " + exchange + "-" + line) # Prints “(202) 555-1212”

# Function to format phone numbers

def format_phone(phonenum):
    area_code = "(" + phonenum[:3] + ")"
    exchange = phonenum[3:6]
    line = phonenum[-4:]
    return area_code + " " + exchange + "-" + line

print(format_phone("2025551212")) # Outputs: (202) 555-1212