# https://codevscolor.com/python-find-largest-divisor-number

num = int(input("Enter a number: "))
largest_divisor = next(i for i in range(int(num / 2 + 1), 0, -1) if num % i == 0)

print("Largest divisor of {} is {}".format(num, largest_divisor))
