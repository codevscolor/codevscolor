# https://codevscolor.com/python-read-all-numbers-from-file

try:
    sum = 0
    given_file = open("input.txt", "r")

    lines = given_file.readlines()

    for line in lines:
        for c in line:
            if c.isdigit() == True:
                sum += int(c)

    print(f"Sum: {sum}")
    
    given_file.close()
except FileNotFoundError as e:
    print(e)