#1
import cmath
import math 
#2
a = float(input("Enter the value of a : "))
b = float(input("Enter the value of b : "))
c = float(input("Enter the value of c : "))
#3
d = b**2 - 4*a*c 
#4
if d < 0 :
    sol_1 = (-b + cmath.sqrt(d))/2*a
    sol_2 = (-b - cmath.sqrt(d))/2*a
else :
    sol_1 = (-b + math.sqrt(d))/2*a
    sol_2 = (-b - math.sqrt(d))/2*a
#5
print("The value of x are {} and {}".format(sol_1,sol_2))
