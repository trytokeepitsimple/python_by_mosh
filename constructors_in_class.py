# constructor
# a constructor is method that gets called at the time of creation of an object.

# self is reference to the current object

# def __init__(self) for creating constructor


# class Point:
#     def __init__(self, x, y):
#         self.x=x
#         self.y=y
#     # above defined is the constructor , it gets executed as soon as object is created
#     # self is reference of current object through which methods or function gets executed
#     def draw(self):
#         print("draw")
#     def move(self):
#         print("move")
#
# point = Point(100,20)
# print(point.x)



class Person:
    def __init__(self, name):
        self.name= name
    def talk(self):
        print(f"{self.name} please talk")

person1= Person("Devesh")
person1.talk()