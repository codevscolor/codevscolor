def findArmStrongSum(no):
    currentNo = no
    length = len(str(currentNo))
    sum = 0

    while currentNo > 0:
        lastDigit = currentNo % 10
        sum += lastDigit ** length

        currentNo = int(currentNo/10)

    return sum


strongNumList = []

for i in range(0,1000):
    armStrongSum = findArmStrongSum(i)
    if (armStrongSum == i):
        strongNumList.append(i)

for no in strongNumList :
    print (no)
