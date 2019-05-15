#1
setA = set()
#2
lengthA = int(input("Enter the total elements for the set : "))
#3
for i in range(lengthA):
    e = int(input("Enter value {} : ".format(i + 1)))
    setA.add(e)
#4
print("setA before discard : {}".format(setA))
#5
element = int(input("Enter the element to discard : "))
#5
setA.discard(element)
print("setA after discard : {}".format(setA))
