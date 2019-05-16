#1
def isAnagram(str1,str2):
    return sorted(str1) == sorted(str2)
#2
str1 = input("Enter the string 1 : ")
str2 = input("Enter the string 2 : ")
#3
if isAnagram(str1,str2):
    print("Strings are anagram")
else:
    print("Strings are not anagram")
