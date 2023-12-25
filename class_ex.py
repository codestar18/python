"""Why we need classes?
it's a collection of functions
new types with methods
 while naming classes capitalize first letter of each word
 we don't use underscore
 Constructor gets called automatically when an object is created
 """


class Point:
    def __init__(self,x, y):
        self.x = x
        self.y = y
    def move(self): #python automatically adds self keyword
        print("move")
    def draw(self):
        print("draw")


point1 =Point(10,20) #creating object
point1.move()