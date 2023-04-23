lower = int(input("Enter the lower range: "))
upper = int(input("Enter the upper range: "))

if lower % 2 != 0:
    lower = lower + 1

while lower <= upper:
    print(lower)
    lower += 2