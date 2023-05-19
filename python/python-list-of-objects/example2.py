class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Subject:
    def __init__(self, name):
        self.subjectName = name

data = []
data.append(Student("Alex", 20))
data.append(Subject("Subject-A"))
data.append(Student("Bob", 21))
data.append(Subject("Subject-B"))
data.append(Student("Ira", 15))

for item in data:
    if(isinstance(item, Student)):
        print('Name : {}, Age : {}'.format(item.name, item.age))
    else:
        print('Subject : {}'.format(item.subjectName))