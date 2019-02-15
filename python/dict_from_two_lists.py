#1
first_list = []
second_list = []
#2
first_list_size = int(input("Enter total elements for the first list : "))
second_list_size = int(input("Enter total elements for the second list : "))
#3
for i in range(first_list_size):
    first_list.append(input("Enter value for the first list : "))
#4
for i in range(second_list_size):
    second_list.append(input("Enter value for the second list : "))
#5
print("Your first list : ",first_list)
print("Your second list : ",second_list)
#6
combined_dict = dict(zip(first_list,second_list))
#7
print("Final dictionary : ",combined_dict)
