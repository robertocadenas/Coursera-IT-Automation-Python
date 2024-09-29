# Review: Branching with if statements
print("\n Review: Branching with if statements\n")

def hint_username(username):
    if len(username) < 3:
        print("Invalid username. Must be at least 3 characters long")

hint_username("John")
hint_username("J")