    #1
    setA = set()
    setB = set()
    #2
    setA_length = int(input(“Enter the size of the first set : “))
    setB_length = int(input(“Enter the size of the second set : “))
    #3
    print(“\n”)
    print(“Enter values for the first set : \n”)
    for i in range(setA_length):
        e = int(input(“Enter value {} : “.format(i+1)))
        setA.add(e)
    #4
    print(“\n”)
    print(“Enter values for the second set : \n”)
    for i in range(setB_length):
        e = int(input(“Enter value {} : “.format(i+1)))
        setB.add(e)
    #5
    print(“\n”)
    print(“First set : {}”.format(setA))
    print(“Second set : {}”.format(setB))
    print(“Difference : {}”.format(setA.difference(setB)))
