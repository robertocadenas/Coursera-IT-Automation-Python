'''
for x in 25:
    print(x)

#this will produce an error
'''

for x in range(25):
    print(x)

#this will make the error go away

def greet_friends(friends):
    for friend in friends:
        print("Hi " + friend)

greet_friends(['Taylor', 'Luisa', 'Jamaal', 'Eli'])
greet_friends("Barry")
greet_friends(['Barry'])