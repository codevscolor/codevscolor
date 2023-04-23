class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age


l = []
data = [Student("Alex", 20), Student("Bob", 21), Student("Ira", 15)]
l.extend(data)

for item in l:
    print("Name : {}, Age : {}".format(item.name, item.age))