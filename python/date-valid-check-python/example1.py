# https://codevscolor.com/date-valid-check-python

import datetime

inputDate = input("Enter the date in format 'dd/mm/yy' : ")

day, month, year = inputDate.split('/')

isValidDate = True
try:
    datetime.datetime(int(year), int(month), int(day))
except ValueError:
    isValidDate = False

if(isValidDate):
    print("Input date is valid ..")
else:
    print("Input date is not valid..")