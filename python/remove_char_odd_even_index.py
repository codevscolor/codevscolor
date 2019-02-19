input_string = input("Enter a string : ")

output_string = ""

oddOrEven = int(input("Enter '1' if you want to remove odd positioned characters , '2' for even positioned characters : "))

if oddOrEven ==1 :
	print ("String after removing characters on odd position : ")
	for i in range(len(input_string)):
		if i%2 != 0:
			output_string = output_string + input_string[i]

elif oddOrEven == 2 :
	print ("String after removing characters on even position : ")
	for i in range(len(input_string)):
		if i%2 == 0:
			output_string = output_string + input_string[i]

print (output_string)
