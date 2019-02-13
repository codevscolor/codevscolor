given_str = "The quick brown fox jumps over the lazy dog"
table = str.maketrans("abcde","12345")
print("Given string : ",given_str)
print("String after replacing the characters : ",given_str.translate(table))

#example 2
given_str = "The quick brown fox jumps over the lazy dog"
table = str.maketrans("abcde","")
print("Given string : ",given_str)
print("String after replacing the characters : ",given_str.translate(table))
