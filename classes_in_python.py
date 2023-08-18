# to define a class - we need to wite class then name of class
# We have to be causious while writing name of classes - We need to follow Pascal Naming convention
# Where each word needs to start with capital letter
#we can use class to define all the functions or methods which belong to a certain type


# we can create object to access methods/functions of a class
# an object is an instance of a class



# to create object of an class - we need to write name of class and then paranthesis
# point1 = Point()
#here point1 is a object or a instance

class Point:
    def draw(self):
        print("draw")
    def move(self):
        print("move")

point1=Point()
point1.x=10;
print(point1.x)


point2=Point()
point2.x=40
print(point2.x)
point2.draw()




