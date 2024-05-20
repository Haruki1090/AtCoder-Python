import math

def triangle_area(side):
    return (math.sqrt(3) / 4) * (side ** 2)

def prism_volume(side, height):
    base_area = triangle_area(side)
    return base_area * height

def prism_surface_area(side, height):
    base_area = triangle_area(side)
    lateral_area = 3 * side * height
    return 2 * base_area + lateral_area