# Review: elif statements

def hint_username(username):
    if len(username) < 3:
        print("Invalid username. Must be at least 3 characters long")
    else:
        if len(username) > 15:
            print("Invalid username. Must be at most 15 characters long")
        else:
            print("Valid username")


# Test cases
hint_username("ab")
hint_username("abcdefg")
hint_username("abcdefghijklmno")

# Example 2

def hint_username(username):
    if len(username) < 3:
        print("Invalid username. Must be at least 3 characters long")
    elif len(username) > 15:
        print("Invalid username. Must be at most 15 characters long")
    else:
        print("Valid username")


# Test cases
hint_username("ab")
hint_username("abcdefg")
hint_username("abcdefghijklmno")