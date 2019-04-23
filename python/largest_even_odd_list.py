# get the total numbers to be stored in the list
total_numbers = int(input("How my numbers you want to add to the list : "))

# create one empty array to store the numbers
numbers_array = []

# run a loop and get the inputs from the user
for i in range(0,total_numbers):
	numbers_array.append(int(input("Number to add : ")))

# create two variables to store largest even and odd number of the list
# store -1 to both of these variables
largest_even = -1
largest_odd = -1

# Now scan the array again and update the largest value if found
for i in range(0,total_numbers):
	if(numbers_array[i] % 2 == 0 and numbers_array[i] > largest_even):
		# even number
		largest_even = numbers_array[i]
	elif(numbers_array[i] % 2 != 0 and numbers_array[i] > largest_odd):
		# odd number
		largest_odd = numbers_array[i]


# All numbers are scanned. Now print the largest odd and even value

print("Largest Odd Number : ",largest_odd)
print("Largest Even Number : ",largest_even)
