def findLcm(a,b):
    large_no = 0
    
    if(a>b):
        large_no = a
    else :
        large_no = b
        
    multiplier = 1
    lcm = large_no
    
    while(lcm < (a*b)):
        print ("checking for ",lcm)
        if(lcm % a == 0 and lcm % b ==0):
            break
            
        multiplier += 1
        lcm = large_no * multiplier
    
    print ("lcm is ",lcm)
    

num1 = 31
num2 = 15

findLcm(num1,num2)
