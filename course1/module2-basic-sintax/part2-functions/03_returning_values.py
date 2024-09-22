def area_triangle(base, height):
    return base*height/2

area_a = area_triangle(5, 4)
area_b = area_triangle(7, 3)

sum_area = area_a + area_b

print("The sum of both areas is: " + str(sum_area))

# The sum of both areas is: 20.5
# The area of a triangle is calculated by multiplying the base and height and dividing the result by 2.
# The area of the first triangle is 10 and the area of the second triangle is 10.5.

# The sum of both areas is 20.5. The function area_triangle() calculates the area of a triangle using the formula base*height/2.
# Two triangles are created using the function, and their areas are stored in the variables area_a and area_b.
# The sum of the areas is calculated and stored in the variable sum_area.
# Finally, the sum of the areas is displayed on the screen.
# The output is:
# The sum of both areas is: 20.5



def convert_seconds(seconds):
    hours = seconds // 3600
    minutes = (seconds - hours * 3600) // 60
    remaining_seconds = seconds - hours * 3600 - minutes * 60
    return hours, minutes, remaining_seconds

hours, minutes, seconds = convert_seconds(5000)
print(hours, minutes, seconds)

# The function convert_seconds() takes the number of seconds as an argument and calculates the equivalent time in hours, minutes, and seconds.
# The function returns the hours, minutes, and remaining seconds.
# The values returned by the function are stored in the variables hours, minutes, and seconds.
# Finally, the values are displayed on the screen.
# The output is:
# 1 23 20
# The equivalent time for 5000 seconds is 1 hour, 23 minutes, and 20 seconds.

# Example: None
# The function greeting() takes a name as an argument and displays a welcome message.
# The function does not return any value.
# The function is called with the argument "Christine".
# The function displays the message "Welcome, Christine".
# The function does not return any value, so the variable result is assigned the value None.
# The output is:
# Welcome, Christine
# None


def greeting(name):
    print("Welcome, " + name)
result = greeting("Christine")
print(result)