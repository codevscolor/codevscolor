#  Print a random float

import random

print(random.random())


#  Print a random float in range

import random

print(random.uniform(1,10))


# Print a random integer
import random

print(random.randrange(10))

# Print an integer number within a range 
import random

print("Random number using randrange : ");
print(random.randrange(2,10))

print("Random number using randint : ");
print(random.randint(2,10))

# Print only even random number in a range
import random

print("Even Random number : ")
print(random.randrange(2,10,2))

print("Random number Divisible by 5 : ")
print(random.randrange(0,100,5))


# Print a random element in a sequence
import random

days = ["sun","mon","tue","wed","thu","fri","sat"]
print(random.choice(days))


# Shuffle a list
import random

days = ["sun","mon","tue","wed","thu","fri","sat"]

for x in range(5):
    print("shuffling..")
    random.shuffle(days)
    print(days)
