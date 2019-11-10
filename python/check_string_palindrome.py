# www.codevscolor.com/python-program-to-check-palindrome-python-tutorial/

# method 1
str = "12345"

print(str[1:3:1])

print(str[2:0:-1])

print(str[::1])

print(str[::-1])



# method 2
str1 = "123454321"

if str1 == str1[::-1]:
    print("Palindrome...")
else:
    print("Not palindrome...")
