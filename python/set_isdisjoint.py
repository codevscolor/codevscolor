#1
setA = set()
setB = set()
#2
lengthA = int(input("Enter the size of the first set : "))
lengthB = int(input("Enter the size of the second set : "))
#3
print("\n")
print("For the first set : \n")
for i in range(lengthA):
    e = int(input("Enter value {} : ".format(i+1)))
    setA.add(e)
#4
print("\n")
print("Enter values for the second set one by one : \n")
for i in range(lengthB):
    e = int(input("Enter value {} : ".format(i+1)))
    setB.add(e)
#5
print("\nYou have entered : ")
print("setA : {} ".format(setA))
print("setB : {} ".format(setB))
#6
if(setA.isdisjoint(setB)):
    print("setA and setB are disjoint set")
else:
    print("setA and setB are not disjoint set")
