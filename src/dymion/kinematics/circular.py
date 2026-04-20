from __future__ import annotations
import math
from ..core.vector import Vector 

def calculate_angular_position(
    theta0: float,
    omega0: float,
    t: float,
    alpha: float = 0.0       
) -> float:
    """Calculates final angle (radians) using theta = theta 0 + omega0*t + 0.5*alpha*t^2"""
    return theta0 + (omega0 * t) + (0.5 * alpha * (t**2))

def calculate_angular_velocity(
    omega0: float,
    alpha: float,
    t: float      
) -> float:
    """Calculates final angular velocity (rad/s): omega = omega0 + alpha*t"""
    return omega0 + (alpha * t)

def get_tangential_velocity(omega: float, radius: float) -> float:
    """v = omega * r"""
    return omega * radius

def get_centripetal_acceleration(omega: float, radius: float) -> float:
    """a_c = omega^2 * r"""
    return (omega**2) * radius

def polar_to_cartesian(radius: float, theta: float) -> Vector:
    """Converts polar coordinates (r, theta) to a 2D Vector(x, y)."""
    return Vector(
        radius * math.cos(theta),
        radius * math.sin(theta),
        0.0
    )
