#1
list_size = int(input("How many numbers are in the list : "))
#2
number_list = []
final_list = []
#3
for i in range(0,list_size):
    number_list.append(int(input("Enter list item {} : ".format(i))))
#4
m = int(input("Enter the first divider : "))
n = int(input("Enter the second divider : "))
#5
for i in range(0,list_size):
    if number_list[i] % m == 0 and number_list[i] % n == 0 :
        final_list.append(number_list[i])
#6
print("Numbers that are divisible by {} and {} is : ".format(m,n),final_list)
