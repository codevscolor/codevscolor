#1
user_list = ['a', 'b', 'c', 'd', 'e']
#2
print("Original list : {}".format(user_list))
#3
count = int(input("Enter the total number of elements to add : "))
index = int(input("Enter the index in the list : "))
#4
for i in range(count):
    #5
    user_input_value = int(input("Enter element {} : ".format(i)))
    user_list.insert(index+i, user_input_value)
#6
print("Final list : {}".format(user_list))
