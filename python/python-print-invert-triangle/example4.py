# https://codevscolor.com/python-print-invert-triangle

height = int(input("Enter the height of the triangle: "))

count = 1

for i in range(1, height + 1):
    for j in range(1, height - i + 2):
        print("{:4s}".format(str(count)), end="")
        count += 1
    print()
