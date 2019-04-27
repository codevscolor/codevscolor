#method 1

PI = 3.14
r = float(input('Enter the radius of the circle :'))
area = PI * r * r

print("Area of the circle is : %.2f" %area)

#method 2

import math

r = float(input('Enter the radius of the circle :'))
area = math.pi * r * r

print("Area of the circle is : %.2f" %area)
