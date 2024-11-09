# Error - TypeError: 'str' object does not support item assignment
'''
message = "A kong string with a silly typo"
message[2] = "l"
#This will throw an error
'''

message = "A kong string with a silly typo"
print(message[0:2])
print(message[3:])
new_message = message[0:2] + "l" + message[3:]
print(new_message)


# Second Message
print("\nSecond Message")

message = "This is a new message"
print(message)
message = "And another one"
print(message)

# Third Message
print("\nThird Message")

pets="Cats & Dogs"
pets.index("&")
pets.index("C")
pets.index("Dog")
pets.index("s")
# Print the index pointed aboved
print(pets.index("&"))
print(pets.index("C"))
print(pets.index("Dog"))
print(pets.index("s"))

# Error - ValueError: substring not found
print("\nError")
'''
pets="Cats & Dogs"
pets.index("x")
#This will throw an error
'''

# Other Pet message
print("\nOther Pet Message")

pets="Cats & Dogs"
"Dragons" in pets
"Cats" in pets
print("Dragons" in pets)
print("Cat" in pets)

# Other message with function
print("\nOther message with function")

def replace_domain(email, old_domain, new_domain):
  if "@" + old_domain in email:
    index = email.index("@" + old_domain)
    new_email = email[:index] + "@" + new_domain
    return new_email
  return email

new_message = replace_domain("roberto@robertocade.com", "robertocade.com", "robercad.com")
print(new_message)