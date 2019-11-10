# www.codevscolor.com/python-print-date-time-hour-minute/

import datetime

def currentTime():
	print("Current date and time : ")
	today = datetime.datetime.strftime(datetime.datetime.today() , '%d/%m/%Y-%Hh/%Mm')
	print(today)

oneDayLater = datetime.datetime.today() + datetime.timedelta(days = 1)
currentTime()
print("Time after one day : ")
print(datetime.datetime.strftime(oneDayLater , '%d/%m/%Y-%Hh/%Mm'))


fourWeeksLater = datetime.datetime.today() + datetime.timedelta(weeks = 4)
print("")
currentTime()
print("Time after four weeks : ")
print(datetime.datetime.strftime(fourWeeksLater , '%d/%m/%Y-%Hh/%Mm'))


oneHourLater = datetime.datetime.today() + datetime.timedelta(hours = 1)
print("")
currentTime()
print("Time after one hour : ")
print(datetime.datetime.strftime(oneHourLater , '%d/%m/%Y-%Hh/%Mm'))


minutesLater = datetime.datetime.today() + datetime.timedelta(minutes = 15)
print("")
currentTime()
print("Time after 15 minutes : ")
print(datetime.datetime.strftime(minutesLater , '%d/%m/%Y-%Hh/%Mm'))
