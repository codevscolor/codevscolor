# Python infinity : infinite numbers and how to check infinite numbers
# https://www.codevscolor.com/python-infinite-numbers/

import math 
print(math.inf)
print(-math.inf)


# isfinite example
values = [10, 0.0, -1, math.nan, math.inf, -math.inf]
for item in values:
    print(math.isfinite(item))
    
    
    
# isinf example
values = [10, 0.0, -1, math.nan, math.inf, -math.inf]
for item in values:
    print(math.isinf(item))
