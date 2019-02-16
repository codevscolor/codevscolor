#1
num = int(input("Enter a number : "))

#2
if(num > 9 and num < 100):
    print("It is a two digit number")
else:
    print("It is not a two digit number")

#3
if(num%2 == 0 or num%3 == 0):
    print("It is divisible by either 2 or 3")
else:
    print("It is not divisible by 2 and 3")

#4
if(not num%5 == 0):
    print("It is not divisible by 5")
else:
    print("It is divisible by 5")
