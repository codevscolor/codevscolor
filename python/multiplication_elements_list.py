#1
my_list = []
#2
for i in range(1,5):
  my_list.append(i)
#3
print(my_list)
#4
result = 1
#5
for item in my_list:
  result = result * item
#6
print("multiplication of all elements : ",result)
