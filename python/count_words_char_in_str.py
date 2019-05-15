#1
word_count = 0
char_count = 0
#2
usr_input = input("Enter a string : ")
#3
split_string = usr_input.split()
#4
word_count = len(split_string)
#5
for word in split_string:
    #6
    char_count += len(word)
#7
print("Total words : {}".format(word_count))
print("Total characters : {}".format(char_count))
