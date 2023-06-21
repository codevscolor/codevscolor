# https://codevscolor.com/python-find-change-percentage-two-numbers

first_number = int(input("Enter your first number: "))
second_number = int(input("Enter your second number: "))

if second_number < first_number:
    print("Please enter a valid number")
else:
    percent_diff = ((second_number - first_number) / first_number) * 100

    print("Difference in percentage is: {:.2f}%".format(percent_diff))
