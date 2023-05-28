# https://codevscolor.com/python-print-invert-triangle

height = int(input("Enter the height of the triangle: "))
c = str(input("Enter the character you want to print the triangle: "))

i = 0

while i < height:
    j = 0
    while j < height - i:
        print(c + " ", end="")
        j += 1
    print()
    i += 1
