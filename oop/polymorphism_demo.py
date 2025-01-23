import math

class Shape:
    """Base class for all shapes."""
    def area(self):
        """Calculate the area of the shape. Must be overridden in subclasses."""
        raise NotImplementedError("The area method must be overridden in subclasses.")


class Rectangle(Shape):
    """A rectangle shape."""
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        """Calculate the area of the rectangle."""
        return self.length * self.width


class Circle(Shape):
    """A circle shape."""
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        """Calculate the area of the circle."""
        return math.pi * (self.radius ** 2)

