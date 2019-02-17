#example 1:
#1
def calculateSumFor(first,second):
  return int(first) + int(second)
#2
firstNumber = "100"
secondNumber = "200"
#3
print(calculateSumFor(firstNumber,secondNumber))

#example 2:
def calculateSumFor(first,second):
  try:
    return int(first) + int(second)
  except ValueError:
    return -1
firstNumber = "hello"
secondNumber = "200"
sum = calculateSumFor(firstNumber,secondNumber)
if sum == -1:
  print("Conversion failed.")
else:
  print(sum)
