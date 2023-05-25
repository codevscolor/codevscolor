# https://codevscolor.com/python-check-tuple-contains-element

def contains(t, given_char):
    for ch in t:
        if ch == given_char:
            return True
    return False


given_tuple = ("a", "b", "c", "d", "e", "f", "g", "h")

print(f"Given tuple: {given_tuple}")
char = input("Enter a character to find: ")

if contains(given_tuple, char):
    print("It is in the tuple")
else:
    print("It is not in the tuple")
