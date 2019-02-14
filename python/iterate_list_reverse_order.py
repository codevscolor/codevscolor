#example 1

#1
my_list = [1,2,3,4,5,6]
#2
for i in range(len(my_list) - 1,-1,-1) :
    print(my_list[i])
    
#example 2

#1
my_list = [1,2,3,4,5,6]
#2
list_length = len(my_list)
#3
index = list_length - 1
#4
while index >= 0 :
    print(my_list[index])
    index -= 1
    
    
#example 3

my_list = [1,2,3,4,5,6]
reverse_list = my_list[::-1]
print(reverse_list)
