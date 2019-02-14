#example 1

user_input_str = input("Enter a string : ")
old_char = input("Enter a character to replace in this string : ")
new_char = input("Enter the new character : ")
new_str = user_input_str.replace(old_char,new_char)
print("New string is : ",new_str)

#example 2
user_input_str = input("Enter a string : ")
old_sub_str = input("Enter a substring to replace in this string : ")
new_sub_str = input("Enter the new substring : ")
new_str = user_input_str.replace(old_sub_str,new_sub_str)
print("New string is : ",new_str)

#example 3
user_input_str = input("Enter a string : ")
old_sub_str = input("Enter a substring to replace in this string : ")
new_sub_str = input("Enter the new substring : ")
str_count = int(input("Enter number of replacement : "))
new_str = user_input_str.replace(old_sub_str,new_sub_str,str_count)
print("New string is : ",new_str)

#example 4
user_input_str = input("Enter a string : ")
old_char = []
new_char = []
total_char = int(input("How many charcters you want to replace : "))
for i in range(total_char):
    old_char.append(input("Enter a character you want to replace : "))
    new_char.append(input("Enter new value for this chracter : "))
for i in range(total_char):
    user_input_str = user_input_str.replace(old_char[i],new_char[i])
print("New string is : ",user_input_str)
