str_1 = "HelloWorld"

str_2 = "Hello World"

str_3 = "one\ntwo\rthree\r\nfour\vfive\x0bsix\fseven\x0ceight\x1cnine\x1dten\x1eeleven\x85twelve\u2028thirteen\u2029"

print("str_1 : ")
print(str_1.splitlines())
print(str_1.splitlines(keepends = True))

print("str_2 : ")
print(str_2.splitlines())
print(str_2.splitlines(keepends = True))

print("str_3 : ")
print(str_3.splitlines())
print(str_3.splitlines(keepends = True))


# example 2

str_1 = ""

print("str_1 : ")
print(str_1.split('\n'))
print(str_1.splitlines())
print(str_1.splitlines(keepends = True))

# example 3
str_1 = "Hello\n"

print("str_1 : ")
print(str_1.split('\n'))
print(str_1.splitlines())
print(str_1.splitlines(keepends = True))
