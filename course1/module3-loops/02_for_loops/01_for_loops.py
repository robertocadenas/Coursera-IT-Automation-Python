# Whot is foor loop?

# For loop is used to iterate over a sequence (list, tuple, string) or other iterable objects.
for x in range(5):
    print(x)

print("\n****\n")

friends = ['Taylor', 'Alex', 'Pat', 'Eli']
for friend in friends:
    print("Hi " + friend)

print("\n****\n")

values = [ 23, 52, 59, 37, 48 ]
sum = 0
length = 0
for value in values:
    sum += value
    length += 1

print("Total sum: " + str(sum) + " - Average: " + str(sum/length))