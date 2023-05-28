# https://codevscolor.com/python-print-invert-triangle

height = int(input("Enter the height of the triangle: "))

for i in range(1, height + 1):
    for j in range(1, height - i + 2):
        print(str(j) + " ", end="")
    print()
