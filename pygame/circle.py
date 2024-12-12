import math
class CircleChecker:
    def __init__(self, radius = 0):
        self.radius = radius
    def area(self):
        
        print(math.ceil(self.radius**2*math.pi))

    def perimeter(self):
        print(math.ceil(2*self.radius*math.pi))


circle = CircleChecker(5)

circle.area()
circle.perimeter()