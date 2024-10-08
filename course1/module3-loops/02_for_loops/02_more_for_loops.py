product = 1
for n in range(1, 10):
    product = product * n

print(product)

print("\n****\n")

# Faranhite to Celsius
# The formula to convert a temperature from Fahrenheit to Celsius is:
# Celsius = (Fahrenheit - 32) * 5.0/9.0

def to_celsius(x):
    return (x - 32) * 5.0/9.0

for x in range(0, 101, 10):
    print(x, to_celsius(x))