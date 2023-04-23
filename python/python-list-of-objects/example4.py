class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age


l = []
l.insert(0, Student("Alex", 20))
l.insert(1, Student("Bob", 21))
l.insert(2, Student("Ira", 15))

for item in l:
    print("Name : {}, Age : {}".format(item.name, item.age))