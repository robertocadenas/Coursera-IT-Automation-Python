# Review: else statements
print("\n Review: else statements\n")

def hint_username(username):
    if len(username) < 3:
        print("Invalid username. Must be at least 3 characters long")
    else:
        print("Valid username")
#This code will not have an output. 

hint_username("John")
hint_username("J")
# Output:
# Valid username
# Invalid username. Must be at least 3 characters long

# module

def is_even(number):
    if number % 2 == 0:
        return True
    return False
#This code has no ouput

print(is_even(4))
print(is_even(5))