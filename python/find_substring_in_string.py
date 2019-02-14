given_str = "The quick brown fox jumps over the lazy dog"

print(given_str)

sub_string = input("Enter a sub-string to find in the above string : ")

if(given_str.find(sub_string) == -1):
    print("The substring doesn't contain in the string")
else:
    print("The substring is found on position : ",given_str.find(sub_string))
