# https://codevscolor.com/date-valid-check-python

from datetime import datetime

inputDate = input("Enter the date in format 'dd/mm/yy' : ")

date_format = "%d/%m/%y"

isValidDate = True
try:
    datetime.strptime(inputDate, date_format)
except ValueError:
    isValidDate = False

if(isValidDate):
    print("Input date is valid ..")
else:
    print("Input date is not valid..")