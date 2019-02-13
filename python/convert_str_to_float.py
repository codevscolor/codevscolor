num_list = ["1.11","2.22","3.33"]

sum = 0

for x in num_list :
    sum += float(x)

print(sum)

#example 2
num_list = ["1.11","2.22","3.33"]

float_list = [ float(x) for x in num_list]

print(num_list)
print(float_list)
