#1
user_list = [1,2,5,4,6,7,8]

#2
temp = user_list[len(user_list) - 1]

#3
user_list[len(user_list) - 1] = user_list[0]

#4
user_list[0] = temp

#5
print(user_list)
