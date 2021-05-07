# Reverse a string in different ways
# Method 1: for loop
def reverse_str(str):
    rev_str = ''
    for c in str:
        rev_str = c + rev_str
    return rev_str

given_str = input('Enter a string : ')
print('Reversed string is : {}'.format(reverse_str(given_str)))


# Method 2: Recursive
def reverse_str_recursive(str):
    if len(str) == 0:
        return str
    else:
        return reverse_str_recursive(str[1:]) + str[0]

given_str = input('Enter a string : ')
print('Reversed string is : {}'.format(reverse_str_recursive(given_str)))


# Method 3: reversed()
def reverse_str_reversed(str):
    return ''.join(reversed(str))

given_str = input('Enter a string : ')
print('Reversed string is : {}'.format(reverse_str_reversed(given_str)))


# Method 4: String slicing
def reverse_str_slicing(str):
    return str[::-1]

given_str = input('Enter a string : ')
print('Reversed string is : {}'.format(reverse_str_slicing(given_str)))
