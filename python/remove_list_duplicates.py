#Approach 1

#1
original_list = [1,3,5,7,2,1,5,2,8]

print("Original list : {}".format(original_list))

#2
final_list = []

#3
for item in original_list :
    #4
    if item not in final_list :
        final_list.append(item)

#5
print("Modified list : {}".format(final_list))

#Approach 2 
#1
original_list = [1,3,5,7,2,1,5,2,8]

#2
print("Original list : {}".format(original_list))

#3
final_list = list(set(original_list))

#4
print("Modified list : {}".format(final_list))
