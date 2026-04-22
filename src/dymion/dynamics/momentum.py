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
