# Method 1 : using for loop 

def factorialUsingForLoop(n):
    fact = 1
    for i in range(1,n+1):
        fact=fact*i

    print('Factorial of the number %d is %d'%(n,fact))

if __name__== "__main__":
    factorialUsingForLoop(4)
    
    
    
    
#Method 2 : using while loop

def factorialUsingWhileLoop(n):
    fact = 1
    while(n>1):
        fact = fact*n
        n = n - 1

    print('Factorial is %d'%(fact))

if __name__== "__main__":
    factorialUsingWhileLoop(4)
    
    
    
    
#Method 3 : using recursion

def factorialUsingRecursion(n):
    if (n == 1):
        return 1
    else :
        return n* factorialUsingRecursion(n-1)

if __name__== "__main__":
    print("factorial is ",factorialUsingRecursion(4))
