# https://codevscolor.com/python-find-largest-divisor-number

num = int(input("Enter a number: "))
largest_divisor = 0

for i in range(2, num):
    if num % i == 0:
        largest_divisor = i

print("Largest divisor of {} is {}".format(num,largest_divisor))