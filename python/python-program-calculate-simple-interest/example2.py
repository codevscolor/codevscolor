# https://codevscolor.com/python-program-calculate-simple-interest

def get_simple_interest(p, n, r):
    return (P * N * R) / 100

if __name__ == "__main__":
    P = float(input("Enter the principal amount: "))
    N = float(input("Enter the number of years: "))
    R = float(input("Enter the rate of interest: "))

    SI = get_simple_interest(P, N, R)
    print("Simple interest : {}".format(SI))
