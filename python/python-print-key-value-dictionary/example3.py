my_dict = {"one": 1, "two": 2, "three": 3, "four": 4}

dict_list = list(my_dict.items())[:2]

for k, v in dict_list:
    print(f"Key: {k}, Value: {v}")