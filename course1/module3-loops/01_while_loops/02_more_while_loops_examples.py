def attempts(n):
    x = 1
    while x <= n:
        print("Attempt " + str(x))
        x += 1
    print("Done")

attempts(5)

# Siguiente completado con copilot

# The function attempts(n) prints "Attempt 1", "Attempt 2", ..., "Attempt n", "Done" on separate lines.

def get_username():
    return input("Enter username: ")

def valid_username(username):
    return len(username) >= 6   

# The function get_username() prompts the user to enter a username and returns the inputted username as a string. The function valid_username(username) returns True if the length of the inputted username is greater than or equal to 6 and False otherwise.

username = get_username()
while not valid_username(username):
    print("Invalid username - must be at least 6 characters long")
    username = get_username()