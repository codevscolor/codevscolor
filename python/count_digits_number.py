#example 1

count = 0
number = int(input("Enter a number "))

while (number > 0):
	number = number//10
	count = count + 1

print ("Total number of digits : ",count)



#example 2
count = 0
number = int(input("Enter a number "))

print ("Total number of digits : ",len(str(abs(number))))
