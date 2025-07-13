from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius ** 2

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

class Pizza(Shape): 
    def __init__(self, topping, radius):
        self.topping = topping
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius ** 2

shapes = [Circle(4), Square(5), Triangle(6, 7), Pizza("pepperoni", 15)]

for shape in shapes:
    print(f"{shape.__class__.__name__} area: {shape.area():.2f} cm^2")
