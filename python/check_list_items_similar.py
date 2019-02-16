#example 1:
def is_all_items_unique(input_list):
    first_element = input_list[0]
    for element in input_list:
        if element != first_element :
            return False
    
    return True 
first_list = [1,1,1,1,1,1,1,1,2,1,1,1,1]
second_list = ["one","one","one","one","one","one","one","one","one"]
if is_all_items_unique(first_list):
    print("first_list items are unique")
else:
    print("first_list items are not unique")
if is_all_items_unique(second_list):
    print("second_list items are unique")
else:
    print("second_list items are not unique")
    
#example 2:
def is_all_items_unique(input_list):
    return input_list.count(input_list[0]) == len(input_list)
first_list = [1,1,1,1,1,1,1,1,2,1,1,1,1]
second_list = ["one","one","one","one","one","one","one","one","one"]
if is_all_items_unique(first_list):
    print("first_list items are unique")
else:
    print("first_list items are not unique")
if is_all_items_unique(second_list):
    print("second_list items are unique")
else:
    print("second_list items are not unique")
    
#example 3:
def is_all_items_unique(input_list):
    return len(set(input_list)) == 1
first_list = [1,1,1,1,1,1,1,1,2,1,1,1,1]
second_list = ["one","one","one","one","one","one","one","one","one"]
if is_all_items_unique(first_list):
    print("first_list items are unique")
else:
    print("first_list items are not unique")
if is_all_items_unique(second_list):
    print("second_list items are unique")
else:
    print("second_list items are not unique")
    
#example 4:
def is_all_items_unique(input_list):
    return all(value == input_list[0] for value in input_list)
first_list = [1,1,1,1,1,1,1,1,2,1,1,1,1]
second_list = ["one","one","one","one","one","one","one","one","one"]
if is_all_items_unique(first_list):
    print("first_list items are unique")
else:
    print("first_list items are not unique")
if is_all_items_unique(second_list):
    print("second_list items are unique")
else:
    print("second_list items are not unique")
