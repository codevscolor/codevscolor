def sortAllWords(given_string):
    words_list = given_string.split()
    words_list.sort()

    print ("Sorted string words are : ")

    for word in words_list:
        print(word," ")


user_string = input("Enter input string : ")
sortAllWords(user_string)
