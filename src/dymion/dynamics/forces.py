from __future__ import annotations
from ..core.vector import Vector
from .body import Body
import math

# --- Constants ---
G_EARTH = 9.80665 # Standard gravity in m/s^2
G_UNIVERSAL = 6.67430e-11 # m^3 kg^-1 s^-2

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

def universal_gravitation(body1: Body, body2: Body) -> Vector:
    """
    Calculates the gravitational force between two bodies:
    F = G * (m1 * m2) / r^2
    The force is returned as a vector acting on body1.
    """
    # Vector from body1 to body2
    r_vector = body2.position - body1.position
    distance = r_vector.magnitude

    if distance == 0:
        return Vector(0, 0, 0)
    
    # Magnitude of the force
    force_mag = G_UNIVERSAL * (body1.mass * body2.mass) / (distance**2)

    # Direction: Unit vector from body1 to body2
    direction = r_vector.normalize()

    return direction * force_mag

def escape_velocity(mass_of_planet: float, radius: float) -> float:
    """
    Calculates the minimum speed needed to escape a planet's gravity.
    v = sqrt(2 * G * M / r)
    """
    return math.sqrt((2 * G_UNIVERSAL * mass_of_planet) / radius)

def centripetal_force(body: Body, omega: float, radius: float) -> Vector:
    """
    Calculates the centripetal force required to keep a body in a circular path.
    F_c = m * omega^2 * r
    """
    # Assuming rotation is in the X-Y plane around the origin
    if body.position.magnitude == 0:
        return Vector(0, 0, 0)

    # Direction is towards the origin
    direction = body.position.normalize() * -1.0
    magnitude = body.mass * (omega**2) * radius
    return direction * magnitude

def centrifugal_force(body: Body, omega: float, radius: float) -> Vector:
    """
    Calculates the centrifugal (fictitious) force experienced in a rotating frame.
    F_f = m * omega^2 * r
    The force vector points away from the center of rotation (along r).
    """
    return centripetal_force(body, omega, radius) * -1.0