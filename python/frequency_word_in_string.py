#1
input_line = input("Enter a string : ")

#2
words_dict = {}

#3
for word in input_line.split():
		words_dict[word] = words_dict.get(word,0) + 1

#4
for key in sorted(words_dict):
	print("{} : {}".format(key,words_dict[key])) 
