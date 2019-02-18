#1
first_string = input("Enter the first string : ")
second_string = input("Enter the second string : ")

length1 = 0
length2 = 0

#2
for i in first_string:
    length1 = length1 + 1

#3
for i in second_string:
    length2 = length2 + 1

#4
if length1 > length2 :
    print("First string is larger than the second")
else :
    print("Second string is larger than the first")
