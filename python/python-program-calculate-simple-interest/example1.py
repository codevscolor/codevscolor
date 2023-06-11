# https://codevscolor.com/python-program-calculate-simple-interest

P = float(input("Enter the principal amount: "))
N = float(input("Enter the number of years: "))
R = float(input("Enter the rate of interest: "))

SI = (P * N * R)/100
print("Simple interest : {}".format(SI))