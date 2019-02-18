#example 1

#1
number = int(input("Enter a number to find the square root : "))

#2
if number < 0 :
	print("Please enter a valid number.")
else :
	#3
	sq_root = number ** 0.5
	#4
	print("Square root of {} is {} ".format(number,sq_root))
  
  
#example 2

import math

number = int(input("Enter a number to find square root : "))

if number < 0 :
	print("Please enter a valid number .")
else :
	print("Square root of {} is {} ".format(number,math.sqrt(number)))
