# https://codevscolor.com/python-compare-string-with-integer

given_str = "5xx"
given_int = 10

try:
    print(given_int > int(given_str))
except:
    print("Exception thrown on int conversion")
