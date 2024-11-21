class Rectangle:
    def __init__ (self,length,width):
        self.length = length
        self.width = width
        
    def calculated_area(self):
        area = self.length * self.width
        print(f"Rectangle area = {self.length} x {self.width}\n")
        print(f"Rectangle area = {area} cm2\n")

class Circle:
    def __init__(self,phi, radius):
        self.phi = phi
        self.radius = radius
    
    def calculate_area(self):
        area = self.phi * self.radius **2
        print(f"Circle area = {self.phi} x {self.radius} squared cm \n")
        print(f"Circle area = {area} cm2")

rectangleArea = Rectangle(5,6)
circleArea = Circle(3.14,9)

rectangleArea.calculated_area()
circleArea.calculate_area()