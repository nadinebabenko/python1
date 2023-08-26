import math

class Circle:
    def __init__(self, radius=None, diameter=None):
        if radius is not None:
            self.radius = radius
        elif diameter is not None:
            self.radius = diameter / 2
        else:
            raise ValueError("Either radius or diameter must be specified")
    
    @property
    def diameter(self):
        return self.radius * 2
    
    @diameter.setter
    def diameter(self, value):
        self.radius = value / 2
    
    @property
    def area(self):
        return math.pi * self.radius ** 2
    
    def __str__(self):
        return f"Circle with radius {self.radius}"
    
    def __repr__(self):
        return f"Circle({self.radius})"
    
    def __add__(self, other):
        return Circle(self.radius + other.radius)
    
    def __lt__(self, other):
        return self.radius < other.radius
    
    def __eq__(self, other):
        return self.radius == other.radius
    
    def __gt__(self, other):
        return self.radius > other.radius
    
circles = [Circle(3), Circle(1), Circle(2)]
circles.sort()
print(circles)