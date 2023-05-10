# https://codevscolor.com/python-print-star-hollow-square-pattern
length = int(input("Enter the side of the square: "))

row = 1

while(row <= length):
    column = 1;
    while(column <= length ):
        if(row == 1 or row == length or column == 1 or column == length):
            print('*', end = ' ')
        else:
            print(' ', end = ' ')
        column = column + 1
    row = row + 1
    print()