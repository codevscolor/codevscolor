input_string = input("Enter a string : ")

count = 0

for c in input_string:
	if(c.islower()):
		count = count + 1

if(count == 0):
	print("No Lower case character is found in the string.")
else :
	print("Total no of lower case character : ",count)
