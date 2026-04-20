from __future__ import annotations
import math
from typing import Union

class Vector:
    """
    A professional 2D/3D Vector class to handle physics coordinates.
    """
    def __init__(self, x: float, y: float, z: float = 0.0):
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)
    
    def __repr__(self) -> str:
        return f"Vector(x={self.x}, y={self.y}, z={self.z})"

    def __add__(self, other: Vector) -> Vector:
        if not isinstance(other, Vector):
            raise TypeError(f"Unsupported operand type for +: 'Vector' and '{type(other).__name__}'")
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other: Vector) -> Vector:
        if not isinstance(other, Vector):
            raise TypeError(f"Unsupported operand type for -: 'Vector' and '{type(other).__name__}'")
        return Vector(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, scalar: Union[float, int]) -> Vector:
        if not isinstance(scalar, (int, float)):
            raise TypeError("Multiplication must be by a scalar (int or float).")
        return Vector(self.x * scalar, self.y * scalar, self.z * scalar)
    
    @property
    def magnitude(self) -> float:
        """Return the Euclidean norm of the vector."""
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)

    def normalize(self) -> Vector:
        """Returns a unit vector in the same direction"""
        mag = self.magnitude
        if mag == 0:
            return Vector(0, 0, 0)
        return self * (1.0 / mag)