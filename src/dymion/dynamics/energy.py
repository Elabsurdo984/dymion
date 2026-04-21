from __future__ import annotations
from ..core.vector import Vector
from .body import Body
from .forces import G_EARTH

def kinetic_energy(body: Body) -> float:
    """
    Calculates the Kinetic Energy (Ek): 1/2 * m * v^2
    """
    speed = body.velocity.magnitude
    return 0.5 * body.mass * (speed**2)

def gravitational_potential_energy(body: Body, height: float, g: float = G_EARTH):
    """
    Calculates the Gravitational Potential Energy (Ep): m * g * h
    """
    return body.mass * g * height

def elastic_potential_energy(k: float, displacement_magnitude: float) -> float:
    """
    Calculates the Elastic Potential Energy: 1/2 * k * x^2
    """
    return 0.5 * k * (displacement_magnitude**2)

def mechanical_energy(body: Body, height: float, g: float = G_EARTH) -> float:
    """
    Total Mechanical Energy: Ek + Ep
    """
    return kinetic_energy(body) + gravitational_potential_energy(body, height, g)

def work(force: Vector, displacement: Vector) -> float:
    """
    Calculates Work (W): Force dot Displacement
    W = F * d * cos(theta) (Calculated via dot product)
    """
    return (force.x * displacement.x) + (force.y * displacement.y) + (force.z * displacement.z)

def power(work_done: float, time: float) -> float:
    """
    Calculates Power (P): Work / Time
    """
    if time <= 0:
        return 0.0
    return work_done / time
