import math

def calculate_area(shape, **dimensions):
    if shape == "square":
        side = dimensions.get("side")
        return side ** 2
    elif shape == "rectangle":
        length = dimensions.get("length")
        width = dimensions.get("width")
        return length * width
    elif shape == "circle":
        radius = dimensions.get("radius")
        return 3.14 * (radius ** 2)
    else:
        return None

def calculate_perimeter(shape, **dimensions):
    if shape == "square":
        side = dimensions.get("side")
        return 4 * side
    elif shape == "rectangle":
        length = dimensions.get("length")
        width = dimensions.get("width")
        return 2 * (length + width)
    elif shape == "circle":
        radius = dimensions.get("radius")
        return 2 * 3.14 * radius
    else:
        return None

def cylinder_volume(radius, height):
    """Calculate the volume of a cylinder given its radius and height."""
    return math.pi * radius**2 * height

def sphere_volume(radius):
    """Calculate the volume of a sphere given its radius."""
    return (4/3) * math.pi * radius**3