import math

class Circle():
    def __init__(self,radious):
        self.radious=radious

    def getArea(self):
        Area=math.pi*(self.radious)*self.radious
        return Area

    def getPerimeter(self):
        Perimeter=math.pi*2*self.radious
        return Perimeter


a=Circle(7)

print(a.getArea())
print(a.getPerimeter())