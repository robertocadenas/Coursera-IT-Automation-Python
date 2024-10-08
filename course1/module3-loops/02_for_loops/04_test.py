# print 3 numbers from a list

for i in [8, 9, 10]:
    print(i) 

# print 5 times "Access denied" message

for i in range(5):
    print("Access denied")

# You want to print out a sequence of numbers starting at 10 and ending at 30.

for i in range(10, 31):
    print(i)

# Print 5 times "Try again." - attempts

attempt = 1
while attempt <= 5:
    print("Try again.")
    attempt += 1

# You want to print out the numbers 20, 19, 18, 17, and 16.

i = 20
while (i > 15):
    print(i)
    i = i - 1

# You want to welcome 3 users from a list by their name (for example, “Welcome, Emerick Larson”).

name = ["Emerick Larson", "Estrella Ortiz", "Tori Shah"]
for i in name:
    print("Welcome, ", i)