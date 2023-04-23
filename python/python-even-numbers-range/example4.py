lower = int(input("Enter the lower range: "))
upper = int(input("Enter the upper range: "))

if lower % 2 != 0:
    lower = lower + 1

for i in range(lower, upper + 1, 2):
    print(i)