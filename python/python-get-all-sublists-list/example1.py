# https://codevscolor.com/python-get-all-sublists-list
given_list = list()
result_list = list()

size = int(input('Enter the size of the list :'))

print('Enter all elements of the list :')

for i in range(size):
    given_list.append(int(input('Enter element to add : ')))

for i in range(len(given_list) + 1):
    for j in range(i + 1, len(given_list) + 1):
        result_list.append(given_list[i:j])

print(given_list)
print(result_list)