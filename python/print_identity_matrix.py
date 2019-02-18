#1
size = int(input("Enter the size of the matrix : "))

#2
for i in range(0,size):
	#3
	for j in range(0,size):
		#4
		if(i==j):
			print("1",end = " ")
		else:
			print("0",end = " ")
	#5
	print()
