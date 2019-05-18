#1
num = int(input("Enter a number : "))
#2
for i in range(2, num+1):
    #3
    if num % i == 0:
        print ("The smallest divisor for {} is {}".format(num, i))
        break
