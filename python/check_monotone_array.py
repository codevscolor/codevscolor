#1
user_array = list()
#2
def is_monotonic(arr):
    #3
    if all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1)): return "monotone increasing" elif all(arr[i] >= arr[i + 1] for i in range(len(arr) - 1)):
        return "monotone decreasing"
    return "not monotonic array"
#4
size = int(input("Enter the size of the array : "))
#5
for i in range(size):
    n = int(input("Enter value for position {} : ".format(i)))
    user_array.append(n)
#6
print("Input array is "+is_monotonic(user_array))
