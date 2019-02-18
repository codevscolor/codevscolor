#5
def isAbundant(input_no):
	#6
	total = 0

	#7
	for i in range(1,input_no):
		#8
		if(input_no % i == 0):
			#9
			total = total + i 
			if(total > input_no):
				return True

	#10			
	if(total > input_no):
		return True
	else :
		return False

#1
no = 1
while(True):
	#2
	if(isAbundant(no) and no%2 != 0):
		#3
		print("Odd abundant no : ",no)
		break
	#4
	no += 1
