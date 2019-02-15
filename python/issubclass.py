class MainClass:
    pass
class ChildClass(MainClass):
    pass
class GrandChildClass(ChildClass):
    pass
print(issubclass(ChildClass, MainClass))
print(issubclass(GrandChildClass, MainClass))
print(issubclass(GrandChildClass, ChildClass))
print(issubclass(ChildClass, GrandChildClass))
print(issubclass(MainClass, MainClass))


#example 2
class MainClass:
    pass
class ChildClass(MainClass):
    pass
class GrandChildClass(ChildClass):
    pass
print(issubclass(ChildClass, (MainClass, GrandChildClass)))
