import math

def circle_area(radius):
    """Calculates the area of a circle given its radius."""
    if radius < 0:
        raise ValueError("Radius cannot be negative.")
    return math.pi * radius**2

def rectangle_area(length, width):
    """Calculates the area of a rectangle given its length and width."""
    if length < 0 or width < 0:
        raise ValueError("Length and width cannot be negative.")
    return length * width