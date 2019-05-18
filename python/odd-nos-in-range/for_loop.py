#1
lower_limit = int(input("Enter the lower limit : "))
upper_limit = int(input("Enter the upper limit : "))
#2
for i in range(lower_limit,upper_limit + 1):
    #3
    if(i%2 != 0):
        print("{} ".format(i))
