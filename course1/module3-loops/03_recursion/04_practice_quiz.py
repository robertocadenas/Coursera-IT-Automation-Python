# Return true/false is a number is a power of given base

def is_power_of(number, base):
    # Base case: when number is smaller than base
    if number < base:
        # If number is equal to 1, it's a power (base^0)
        return number == 1
    # Recursive case: keep dividing number by base
    return is_power_of(number / base, base)

# Test cases
print(is_power_of(8, 2)) # Should be True
print(is_power_of(64, 4)) # Should be True
print(is_power_of(70, 10)) # Should be False


# Sum all positive numbers up to n
print("Sum all positive numbers up to n")

def sum_positive_numbers(n):
    # Base case: n is smaller or equal to 0
    if n <= 0:
        return 0
    # Recursive case: add current n with sum of numbers smaller than n
    return n + sum_positive_numbers(n - 1)

# Test cases
print(sum_positive_numbers(3)) # Should be 6
print(sum_positive_numbers(5)) # Should be 15


