def printLeapYear():
	print("Inpur Year is a Leap Year")

def printNotLeapYear():
	print("Inpur Year is not a Leap Year")


input_year = int(input("Enter a Year : "))

if input_year % 4 == 0:
	if input_year % 100 == 0 :
		if input_year % 400 == 0 :
			printLeapYear()
		else :
			printNotLeapYear()
	else :
		printLeapYear()
else :
	printNotLeapYear()
