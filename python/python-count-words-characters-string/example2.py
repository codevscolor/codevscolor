# https://codevscolor.com/python-count-words-characters-string
word_count = 0
char_count = 0
last_word_space = False

usr_input = input("Enter a string : ")
word_list = usr_input.split()

word_count = len(word_list)
char_count = sum([len(c) for c in word_list])

print("Total words : {}".format(word_count))
print("Total characters : {}".format(char_count))