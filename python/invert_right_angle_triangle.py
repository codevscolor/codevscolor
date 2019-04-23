#example 1
height = int(input("Enter the height of the triangle : "))

for i in range(1,height+1):
	for j in range(1,height - i+2):
		print(str(j)+" ", end='')
	print()
  
  
  
#example 2
height = int(input("Enter the height of the triangle : "))
c = str(input("Enter the character you want to print the triangle : "))

for i in range(0,height):
	for j in range(0,height - i):
		print(c+" ", end='')
	print()
