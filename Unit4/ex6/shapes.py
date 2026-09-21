import math

# Base class
class Shape:
    def area(self):
        pass

    def perimeter(self):
        pass


# Circle class
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius * self.radius

    def perimeter(self):
        return 2 * math.pi * self.radius


# Triangle class
class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def area(self):
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def perimeter(self):
        return self.a + self.b + self.c


# Square class
class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side

    def perimeter(self):
        return 4 * self.side


# Create objects
circle = Circle(5)
triangle = Triangle(3, 4, 5)
square = Square(4)

# Display results
print("Circle")
print("Area:", circle.area())
print("Perimeter:", circle.perimeter())

print("\nTriangle")
print("Area:", triangle.area())
print("Perimeter:", triangle.perimeter())

print("\nSquare")
print("Area:", square.area())
print("Perimeter:", square.perimeter())
