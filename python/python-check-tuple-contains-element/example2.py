# https://codevscolor.com/python-check-tuple-contains-element

def contains(t, item):
    for i in t:
        if i == item:
            return True
    return False


given_tuple = ({"id": 1, "name": "Alex"}, {"id": 2, "name": "Bob"})

print(f"Given tuple: {given_tuple}")
item = {"id": 4, "name": "Bob"}

if contains(given_tuple, item):
    print(f"{item} is in the tuple")
else:
    print(f"{item} is not in the tuple")
