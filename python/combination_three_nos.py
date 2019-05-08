#1
num1 = int(input("Enter the first number : "))
num2 = int(input("Enter the second number : "))
num3 = int(input("Enter the third number : "))

#2
num_list = []
num_list.append(num1)
num_list.append(num2)
num_list.append(num3)

#3
for i in range(0, 3):
    for j in range(0, 3):
        for k in range(0, 3):
            if(i != j & j != k & k != i):
                print("[{} {} {}]".format(
                    num_list[i], num_list[j], num_list[k]))
