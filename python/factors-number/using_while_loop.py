def print_factors(n):
    i = 1
    while(i < n+1):
        if n % i == 0:
            print(i)
        i = i + 1
number = int(input("Enter a number : "))
print("The factors for {} are : ".format(number))
print_factors(number)
