class Point :
    def __init__(self, x = 0, y = 0) :
        self.x = x
        self.y = y

    def get(self) :
        return "("+str(self.x) + "," + str(self.y) + ")"

    def __add__(self, other) :
        newX = self.x + other.x
        newY = self.y + other.y
        return Point(newX, newY)

p1 = Point(2,3)
p2 = Point(4,7)
p3 = p1 + p2

print(p1.get())
print(p2.get())
print(p3.get())
