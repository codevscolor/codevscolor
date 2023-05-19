lower = int(input("Enter the lower range: "))
upper = int(input("Enter the upper range: "))

while lower <= upper:
    if lower % 2 == 0:
        print(lower)
    lower += 1