from __future__ import annotations
from ..core.vector import Vector
from .body import Body

def linear_momentum(body: Body) -> Vector:
    """
    Calculates the linear momentum (p): p = m * v
    """
    return body.velocity * body.mass

def impulse(force: Vector, time_interval: float) -> Vector:
    """
    Calculates the Impulse (J): J = F * Δt
    Impulse is also equal to the change in momentum.
    """
    return force * time_interval

def elastic_collision_1d(m1: float, v1: float, m2: float, v2: float) -> tuple[float, float]:
    """
    Calculates final velocities for a perfect 1D elastic collision.
    Returns (v1_final, v2_final)
    """
    v1_final = ((m1 - m2) * v1 + 2 * m2 * v2) / (m1 + m2)
    v2_final = ((m2 - m1) * v2 + 2 * m1 * v1) / (m1 + m2)
    return v1_final, v2_final

def inelastic_collision_1d(m1: float, v1: float, m2: float, v2: float) -> float:
    """
    Calculates the final velocity for a perfectly inelastic collision (objects stick together).
    v_final = (m1*v1 + m2*v2) / (m1 + m2)
    """
    return (m1 * v1 + m2 * v2) / (m1 + m2)

def resolve_collision_2d(body1: Body, body2: Body):
    """
    Resolves a 2D elastic collision between two bodies.
    Updates their velocities based on conservation of momentum and energy.
    """
    # Vector between centers
    collision_vector = body2.position - body1.position
    distance = collision_vector.magnitude

    if distance == 0: return # Avoid division by zero

    # Normal and Tangent unit vectors
    normal = collision_vector.normalize()
    tangent = Vector(-normal.y, normal.x, 0)

    # Project velocities onto normal and tangent vectors
    v1n = (body1.velocity.x * normal.x) + (body1.velocity.y * normal.y)
    v1t = (body1.velocity.x * tangent.x) + (body1.velocity.y * tangent.y)
    v2n = (body2.velocity.x * normal.x) + (body2.velocity.y * normal.y)
    v2t = (body2.velocity.x * tangent.x) + (body2.velocity.y * tangent.y)

    # Use 1D elastic collision formula for normal components
    # We use a simplified average restitution for now
    e = min(body1.material.restitution, body2.material.restitution)

    v1n_final = (e * body2.mass * (v2n - v1n) + body1.mass * v1n + body2.mass * v2n) / (body1.mass + body2.mass)
    v2n_final = (e * body1.mass * (v1n - v2n) + body1.mass * v1n + body2.mass * v2n) / (body1.mass + body2.mass)

    # Tangential velocities remain the same (frictionless model)
    # Convert back to Cartesian coordinates
    body1.velocity = (normal.v1n_final) + (tangent * v1t)
    body2.velocity = (normal.v2n_final) + (tangent * v2t)