#example 1
height = int(input("Enter the height of the triangle :"))
for i in range(1,height+1):
  for j in range(1,i+1):
    print(str(i)+" ", end='')
  print()
  
#example 2
height = int(input("Enter the height of the triangle : "))
c = str(input("Enter the character you want to print the triangle : "))
for i in range(1,height+1):
  for j in range(1,i+1):
    print(c+" ", end='')
  print()
