# https://codevscolor.com/count-number-digits-number-python
count = 0
number = int(input("Enter a number: "))

for _ in str(number):
    count = count + 1

print(f"Total number of digits: {count}")
