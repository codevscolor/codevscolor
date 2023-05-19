 # https://codevscolor.com/python-find-sum-numbers-file

with open('input.txt', 'r') as given_file:
    lines = given_file.readlines()
    sum = 0

    for line in lines:
        for c in line:
            if c.isdigit() == True:
                sum = sum + int(c)

    print(sum)