from __future__ import annotations
from ..core.vector import Vector

def intersect_circles(pos1: Vector, radius1: float, pos2: Vector, radius2: float) -> bool:
    """
    Checks if two circles/spheres intersect.
    """
    distance = (pos2 - pos1).magnitude
    return distance <= (radius1 + radius2)

def intersect_aabb(min1: Vector, max1: Vector, min2: Vector, max2: Vector) -> bool:
    """
    Checks if two Axis-Aligned Bounding Boxes (AABB) intersect.
    """
    return (
        min1.x <= max2.x and max1.x >= min2.x and
        min1.y <= max2.y and max1.y >= min2.y and
        min1.z <= max2.z and max1.z >= min2.z
    )
