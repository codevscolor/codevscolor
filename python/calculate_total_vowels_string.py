#1
def isVowel(c):
    return (c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u' or c == 'A' or c == 'E' or c == 'I' or c == 'O' or c == 'U')
#2
input_str = input("Enter the string : ")
vowel_count = 0
#3
for ch in input_str:
    #4
    if isVowel(ch):
        vowel_count += 1
#5
print("Total vowel count : {}".format(vowel_count))
