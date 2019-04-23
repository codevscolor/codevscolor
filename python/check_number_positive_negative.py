def check_number(n):
	if n == 0:
		print ("Zero")
	elif n > 0:
		print (n,"is greater than zero")
	else :
		print (n,"is less than zero")

user_no = int(input("Enter a number : "))

check_number(user_no)
