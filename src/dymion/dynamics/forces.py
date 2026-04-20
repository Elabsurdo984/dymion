from __future__ import annotations
from ..core.vector import Vector
from .body import Body

# --- Constants ---
G_EARTH = 9.80665 # Standard gravity in m/s^2

# --- Force Generators ---

def gravity(body: Body, g: float = G_EARTH) -> Vector:
    """
    Calculates the weight force acting on a body: F = m * g
    By default, it uses Earth's gravity pointing downwards (-Y)
    """
    return Vector(0, -body.mass * g, 0)

def friction(body: Body, mu: float, normal_force: float) -> Vector:
    """
    Calculates the kinetic friction force: F_f = mu * N
    The force always opposes the direction of velocity
    """
    if body.velocity.magnitude == 0:
        return Vector(0, 0, 0)
    
    # Direction is opposite to velocity
    direction = body.velocity.normalize() * -1.0
    magnitude = mu * normal_force
    return direction * magnitude

def spring_force(k: float, displacement: Vector) -> Vector:
    """
    Hooke's Law: F = -k * x
    'k' is the spring constant, 'displacement' is the vector from equilibrium.
    """
    return displacement * -k

def air_resistance(body: Body, rho: float, drag_coefficient: float, area: float) -> Vector:
    """
    Drag Equation: F_d = 1/2 * rho * v^2 * C_d * A
    Rho is air density, C_d is drag coefficient, A is cross-sectional area.
    """
    speed = body.velocity.magnitude
    if speed == 0:
        return Vector(0, 0, 0)

    direction = body.velocity.normalize() * -1.0
    magnitude = 0.5 * rho * (speed**2) * drag_coefficient * area
    return direction * magnitude