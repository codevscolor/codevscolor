# https://codevscolor.com/python-read-all-numbers-from-file

given_file = open("input.txt", "r")

lines = given_file.readlines()

for line in lines:
    for c in line:
        if c.isdigit() == True:
            print(f"Integer found : {c}")

given_file.close()