#1
given_dict = {}
result_set = set()

#2
total_values = int(
    input("Enter total no of key-value pairs of the dictionary : "))

#3
for i in range(total_values):
    #4
    key_value_str = input(
        "Enter key and value for index {} separated by ',' : ".format(i))
    #5
    key_value = key_value_str.split(',')

    #6
    given_dict[key_value[0]] = key_value[1]

#7
value_to_find = input("Enter value to find in the dictionary : ")

#8
dict_item_list = given_dict.items()

#9
for item in dict_item_list:
    if item[1] == value_to_find:
        #10
        result_set.add(item[0])

#11
print("Following are the keys found for value '{}' : ".format(value_to_find))

for item in result_set:
    print(item)
