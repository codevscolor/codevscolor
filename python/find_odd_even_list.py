#1
size = int(input("Enter the size of the list : "))

#2
sum_odd = 0
sum_even = 0

#3
int_list = []

#4
for i in range(size):
    #5
    n = int(input("Enter element {} : ".format(i+1)))
    int_list.append(n)

#6
for i in range(size):
    #7
    if(int_list[i] % 2 == 0):
        sum_even += int_list[i]
    else:
        sum_odd += int_list[i]

#8
print("Sum of odd numbers : {} ".format(sum_odd))
print("Sum of even numbers : {} ".format(sum_even))
