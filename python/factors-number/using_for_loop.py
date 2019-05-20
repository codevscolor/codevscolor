#1
def print_factors(n):
    #2
    for i in range(1, n+1):
        #3
        if n % i == 0:
            print(i)
#4
number = int(input("Enter a number : "))
#5
print("The factors for {} are : ".format(number))
print_factors(number)
