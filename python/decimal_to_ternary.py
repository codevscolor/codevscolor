def find_ternary(num):  #2
    quotient = num/3    #3
    remainder = num%3
    if quotient == 0:   #4
        return ""
    else:
        return find_ternary(int(quotient)) + str(int(remainder))    #5
number = int(input("Enter a number : ")) #1
print(find_ternary(number)) 
