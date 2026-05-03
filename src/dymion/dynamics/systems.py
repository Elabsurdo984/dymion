from __future__ import annotations
from typing import List
from ..core.vector import Vector
from .body import Body

def calculate_center_of_mass(bodies: List[Body]) -> Vector:
    """
    Calculates the center of mass for a system of multiple bodies.
    R = (sum(m_i * r_i)) / sum(m_i)
    """
    if not bodies:
        return Vector(0, 0, 0)
        
    total_mass = sum(b.mass for b in bodies)
    if total_mass == 0:
        return Vector(0, 0, 0)
        
    weighted_position_sum = Vector(0, 0, 0)
    for b in bodies:
        weighted_position_sum += b.position * b.mass
        
    return weighted_position_sum * (1.0 / total_mass)

def calculate_total_momentum(bodies: List[Body]) -> Vector:
    """
    Calculates the total linear momentum of a system of bodies.
    P = sum(m_i * v_i)
    """
    total_p = Vector(0, 0, 0)
    for b in bodies:
        total_p += b.velocity * b.mass
    return total_p
