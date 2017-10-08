class circle :
    def __init__(self, radius) :
        self.radius = radius

    def area(self) :
        a = 3.14 * pow(self.radius, 2)
        return a

    def perimeter(self) :
        p = 2 * 3.14 * self.radius
        return p

c1 = circle(5)
c2 = circle(10)


print('c1 area : ', c1.area())
print('c1 perimeter : %.2f' %c1.perimeter())

print('c2 area : ', c2.area())
print('c2 perimeter : %.2f' %c2.perimeter())

