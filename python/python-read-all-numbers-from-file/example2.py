# https://codevscolor.com/python-read-all-numbers-from-file

try:
    given_file = open("inputs.txt", "r")

    lines = given_file.readlines()

    for line in lines:
        for c in line:
            if c.isdigit() == True:
                print(f"Integer found : {c}")

    given_file.close()
except FileNotFoundError as e:
    print(e)