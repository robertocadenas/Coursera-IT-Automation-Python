# Sum positive numbers using recursion

def sum_positive_numbers(n):
    # The base case is n being smaller than 1
    if n < 1:
        return 0
    return n + sum_positive_numbers(n - 1)

print(sum_positive_numbers(3)) # Should be 6
print(sum_positive_numbers(5)) # Should be 15

# Factorial using recursion
print("\n Factorial using recursion\n")

def factorial(n):
    if n < 2:
        return 1
    return n * factorial(n - 1)

print("Other version of factorial")

def factorial(n):
    print("Factorial called with " + str(n))
    if n < 2:
        print("Returning 1")
        return 1
    result = n * factorial(n - 1)
    print("Returning " + str(result) + " for factorial of " + str(n))
    return result

factorial(4)

