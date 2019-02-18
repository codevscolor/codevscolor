#1
my_list = []

#2
count = int(input("How many numbers you want to add : "))

#3
for i in range(1,count+1):
	my_list.append(int(input("Enter number {} : ".format(i))))

#4
print("Input Numbers : ")
print(my_list)

#5
min = my_list[0]
max = my_list[0]

#6
for no in my_list:
	if no < min : min = no elif no > max :
		max = no

#7
print("Minimum number : {}, Maximum number : {}".format(min,max))
