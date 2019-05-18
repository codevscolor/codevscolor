class Student:
    rank = 73
    def __index__(self):
        return self.rank
    def __int__(self):
        return self.rank
student = Student()
print("oct value of \'student\' is", oct(student))
