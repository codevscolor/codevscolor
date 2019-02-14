#example 1

#1
list_size = int(input("How many numbers you want to store in the list : "))
#2
user_list = []
#3
for i in range(list_size ):
    user_list.append(int(input("Enter element %d : "%(i+1))))
#4
print("This is your list : ",user_list)
#5
flag = int(input("Enter the number you want to remove from this list : "))
#6
while flag in user_list :
    user_list.remove(flag)
#7
print("Final list : ",user_list)


#example 2
list_size = int(input("How many numbers you want to store in the list : "))
user_list = []
for i in range(list_size ):
    user_list.append(int(input("Enter element %d : "%(i+1))))
print("This is your list : ",user_list)
flag = int(input("Enter the number you want to remove from this list : "))
final_list = [item for item in user_list if item != flag]
print("Final list : ",final_list)
