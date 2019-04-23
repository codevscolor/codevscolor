def findArmStrongSum(no):
    currentNo = no
    length = len(str(currentNo))
    sum = 0

    while currentNo > 0:
        lastDigit = currentNo % 10
        sum += lastDigit ** length

        currentNo = int(currentNo/10)

    return sum

no = int(input("Enter a positive number :"))

if(no>0):
    armStrongSum = findArmStrongSum(no)
    if(armStrongSum == no):
        print ("Given number is an Armstrong Number")
    else:
        print ("Number is not an Armstrong Number”)
else:
    print ("Please enter a valid number")
