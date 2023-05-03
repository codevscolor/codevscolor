# https://codevscolor.com/python-check-validity-password

import re

while True:
  user_input = input("Enter a password : ")
  is_valid = False

  if (len(user_input)<6 or len(user_input)>12):
    print("Not valid! Total characters should be between 6 and 12")
    continue
  elif not re.search("[A-Z]",user_input):
    print("Not valid! It should contain one letter between [A-Z]")
    continue
  elif not re.search("[a-z]",user_input):
    print("Not valid! It should contain one letter between [a-z]")
    continue
  elif not re.search("[1-9]",user_input):
    print("Not valid! It should contain one digit between [1-9]")
    continue
  elif not re.search("[~!@#$%^&*]",user_input):
    print("Not valid! It should contain at least one letter in [~!@#$%^&*]")
    continue
  elif re.search("[\s]",user_input):
    print("Not valid! It should not contain any space")
    continue
  else:
    is_valid = True
    break

if(is_valid):
  print("Password is valid")