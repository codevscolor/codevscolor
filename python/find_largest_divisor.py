#1
num = int(input("Enter a number : "))
largest_divisor = 0
#2
for i in range(2, num):
    #3
    if num % i == 0:
        #4
        largest_divisor = i 
#5
print("Largest divisor of {} is {}".format(num,largest_divisor))
