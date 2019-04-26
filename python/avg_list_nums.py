#Normal Method 

numberList = []
print ("Enter all numbers with ',' as separator")
numberList = [int(i) for i in input().split(',')]
print ("Average = ",sum(numberList)/len(numberList))




#Statistics module

from statistics import mean
numberList = []
print ("Enter all numbers with ',' as separator")
numberList = [int(i) for i in input().split(',')]
print ("Average = ",mean(numberList))



#using reduce

from functools import reduce
numberList = []
print ("Enter all numbers with ',' as separator")
numberList = [int(i) for i in input().split(',')]
print ("Average = ",reduce(lambda x,y:x+y, numberList)/len(numberList))
