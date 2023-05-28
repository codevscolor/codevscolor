# https://codevscolor.com/python-print-invert-triangle

height = int(input("Enter the height of the triangle: "))

for i in range(0, height):
    for j in range(height - i, 0, -1):
        print(str(j) + " ", end="")
    print()
