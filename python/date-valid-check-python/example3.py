# https://codevscolor.com/date-valid-check-python

from dateutil import parser

inputDate = input("Enter the date in any valid format: ")

isValidDate = True
try:
    print(parser.parse(inputDate))
except ValueError:
    isValidDate = False

if(isValidDate):
    print("Input date is valid ..")
else:
    print("Input date is not valid..")