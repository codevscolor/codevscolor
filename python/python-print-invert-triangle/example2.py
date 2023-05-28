# https://codevscolor.com/python-print-invert-triangle

height = int(input("Enter the height of the triangle: "))
c = str(input("Enter the character you want to print the triangle: "))

for i in range(0, height):
    for j in range(0, height - i):
        print(c + " ", end="")
    print()
