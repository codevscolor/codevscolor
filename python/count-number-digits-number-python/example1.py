# https://codevscolor.com/count-number-digits-number-python
count = 0
number = int(input("Enter a number: "))

while number > 0:
    number = number // 10
    count = count + 1

print(f"Total number of digits: {count}")
