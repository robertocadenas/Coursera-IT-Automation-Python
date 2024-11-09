# Here are the items in the customer's basket. Each item is a tuple
# of (item name, weight, price per pound).
#
basket = [
    ("Peaches", 3.0, 2.99),
    ("Pears", 5.0, 1.66),
    ("Plums", 2.5, 3.99)
]


# Calculate the total price for each item (weight times price per pound)
# and add them up to get a subtotal.
#
subtotal = 0.00
for item in basket:
    fruit, weight, unit_price = item
    subtotal += (weight * unit_price)


# Now calculate the sales tax and total bill.
#
tax_rate = 0.06625 # 6.625% sales tax in New Jersey
tax_amt = subtotal * tax_rate
total = subtotal + tax_amt


# Print the receipt for the customer.
#
print("Subtotal:", subtotal)
print("Sales Tax:", tax_amt)
print("Total:", total)


# Using the format() method
print("\nUsing the format() method")

fruit = "peaches"
weight = 3.0
per_pound = 2.99

# Option 1: The format() method replaces the curly braces with matching values
output = "You are buying {} pounds of {} at {} per pound.".format(weight, fruit, per_pound)
print(output)

# Option 2: The format() method replaces the curly braces with the indexed values
output = "{1} are {2} per pound, and you have {0} pounds of {1}.".format(weight, fruit, per_pound)
print(output)

# Option 3: The format() method replaces the curly braces with the named values
output = "{fruit} are {price} per pound, and you have {weight} pounds of {fruit}.".format(weight=weight, fruit=fruit, price=per_pound)
print(output)


# New version of the code using the format() method
print("\nNew version of the code using the format() method")

# Print the receipt for the customer. The format string ":10,.2f" 
# works as follows:
#   - ":10" makes the output 10 characters wide.
#   - "," inserts thousands separators between groups of digits.
#   - ".2" limits the output to two digits after the decimal.
#   - "f" tells Python to expect a floating-point number.
#
print("Subtotal:    ${:10,.2f}".format(subtotal))
print("Sales Tax:   ${:10,.2f}".format(tax_amt))
print("Total:       ${:10,.2f}".format(total))


# Other examples of format strings
# https://docs.python.org/3/library/string.html#format-specification-mini-language
print("\nOther examples of format strings")

# Integer value - {:d}
print("\nInteger value:")
print("This is ower example que decimals like {:.0f}".format(10.5))
# floating point with that many decimals - {:.2f}
print("This is ower example que decimals like {:.2f}".format(10.5))
# string with that many characters - {:.2s}
print("This is ower example with a string like Hello world: {:.2s}".format("Hello World"))
# string aligned to the left that many spaces - {:<6s}
print("This is ower example with a string like Hello world: {:<6s}".format("Hello World"))
# string aligned to the right that many spaces - {:>6s}
print("This is ower example with a string like Hello world: {:>12s}".format("Hello World"))
# string centered in that many spaces - {:^6s}
print("This is ower example with a string like Hello world: {:^18s}".format("Hello World"))

# formatted string literal feature
# https://docs.python.org/3/reference/lexical_analysis.html#f-strings
print("\nFormatted string literal feature")
# The f-string feature is available in Python 3.6 and later.
name = "Robert"
age = 25
print(f"Hello, {name}. You are {age} years old.")
# You can also use expressions inside f-strings.
print(f"Next year, you will be {age + 1} years old.")

item = "peaches"
amount = 5
weight = 3.0
per_pound = 2.99
price = amount * weight * per_pound
print(f"You are buying {amount} pounds of {item} at {per_pound} per pound. The total price is {price:.2f}.")




