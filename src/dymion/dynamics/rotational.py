from __future__ import annotations
import math
from ..core.vector import Vector

def calculate_torque(lever_arm: Vector, force: Vector) -> Vector:
    """
    Calculates Torque (tau) = r x F.
    r is the vector from the axis of rotation to the point where force is applied.
    """
    # Cross product
    tx = lever_arm.y * force.z - lever_arm.z * force.y
    ty = lever_arm.z * force.x - lever_arm.x * force.z
    tz = lever_arm.x * force.y - lever_arm.y * force.x
    return Vector(tx, ty, tz)

def inertia_sphere(mass: float, radius: float) -> float:
    """I = 2/5 * m * r^2"""
    return 0.4 * mass * (radius**2)

def inertia_cylinder(mass: float, radius: float) -> float:
    """I = 1/2 * m * r^2"""
    return 0.5 * mass * (radius**2)

def inertia_rod_center(mass: float, length: float) -> float:
    """I = 1/12 * m * L^2"""
    return (1.0/12.0) * mass * (length**2)
