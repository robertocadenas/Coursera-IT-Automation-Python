def print_range(start, end):
	# Loop through the numbers from start to end
	n = start
	while n <= end:
		print(n)
		n = n + 1

print_range(1, 5)  # Should print 1 2 3 4 5 (each number on its own line) 


'''
while True:
    do_something_cool()
    if user_requested_to_stop():
        break
#This code will give an error because do_something_cool is not defined
'''