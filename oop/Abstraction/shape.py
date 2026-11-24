from abc import ABC,abstractmethod
from math import pi

class Shape(ABC):
    
    @abstractmethod
    def calculate_area(self):
        pass
    
    @abstractmethod
    def calculate_parameter(self):
        pass
    
class Rectangle(Shape):
    def __init__(self,length,width):
        self.length =length
        self.width = width
    
    def calculate_area(self):
        return self.length * self.width
    
    def calculate_parameter(self):
        return 2*(self.length  + self.width)
    
class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius
        
    def calculate_area(self):
        return pi * self.radius**2
    
    def calculate_parameter(self):
        return 2 *pi *self.radius
    
A1 =Rectangle(4,2)
A2 =Circle(5)
print(f"Area of a rectangle: {A1.calculate_area()}")
print(f"Area of a Circle {A2.calculate_area()}")
print(f"parameter of a rectangle: {A1.calculate_parameter()}")
print(f"parameter of a Circle {A2.calculate_parameter()}")

        