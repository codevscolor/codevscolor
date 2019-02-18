#1
input_no = int(input("Enter a number : "))
total = 0

#2
is_abundant = 0

#3
for i in range(1,input_no):
	#4
	if(input_no % i == 0):
		#5
		total = total + i 
		if(total > input_no):
			is_abundant = 1
			break

#6
if((total > input_no) or (is_abundant ==1)):
	print("It is an abundant number.")
else :
	print("It is not an abundant number.")
