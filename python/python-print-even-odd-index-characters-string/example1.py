# https://codevscolor.com/python-print-even-odd-index-characters-string

given_string = input('Enter a string: ')

even_chars = []
odd_chars = []

for i in range(len(given_string)):
    if i % 2 == 0:
        even_chars.append(given_string[i])
    else:
        odd_chars.append(given_string[i])

print(f'Odd characters: {odd_chars}')
print(f'Even characters: {even_chars}')