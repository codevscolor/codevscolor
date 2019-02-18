first_list = []
second_list = []

#get total count for the first list
count_first_list = int(input("Enter total numbers of the first list : "))

#take inputs from the user for the first list
for i in range(1,count_first_list+1):
  no = int(input("Enter : "))
  first_list.append(no)
  
#get total count for the second list
count_second_list = int(input("Enter total numbers of the second list : "))

#take inputs from the user for the second list
for i in range(1,count_second_list+1):
  no = int(input("Enter : "))
  second_list.append(no)
  
#print first and second list
print("First list : ",first_list)
print("Second list : ",second_list)

#append both list
final_list = first_list + second_list
#sort the final list
final_list.sort()

#print the final sorted list
print("Final list : ",final_list)
