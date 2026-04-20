from __future__ import annotations
from typing import Optional
from ..core.vector import Vector

# --- Functional API (Pure Math) ---

def calculate_position(
    initial_position: Vector,
    initial_velocity: Vector,
    time: float,
    acceleration: Vector = Vector(0, 0, 0)  
) -> Vector:
    """
    Calculates the final position using the SUVAR equation:
    r = r0 + v0*t + 0.5*a*t^2
    """
    displacement = (initial_velocity * time) + (acceleration * (0.5 * time**2))
    return initial_position + displacement

def calculate_velocity(
    initial_velocity: Vector,
    acceleration: Vector,
    time: float
) -> Vector:
    """
    Calculates the final velocity:
    v = v0 + a*t
    """
    return initial_velocity + (acceleration * time)

# --- Object-Oriented API (Stateful) ---

class Particle:
    """
    Represents a point mass in space with kinematic properties.
    """
    def __init__(
        self,
        position: Optional[Vector] = None,
        velocity: Optional[Vector] = None,
        acceleration: Optional[Vector] = None
    ):
        self.position = position or Vector(0, 0, 0)
        self.velocity = velocity or Vector(0, 0, 0)
        self.acceleration = acceleration or Vector(0, 0, 0)
    
    def __repr__(self) -> str:
        return(f"Particle(pos={self.position}, vel={self.velocity}) "
               f"acc={self.acceleration})")
    
    def update(self, dt: float):
        """
        Updates the particle's state (position and velocity) after a time interval 'dt'.
        This uses Euler integration, the standart for simple physics engines.
        """
        # Update position: r = r0 + v*dt
        self.position = calculate_position(self.position, self.velocity, dt, self.acceleration)

        # Update velocity: v = v0 + a*dt
        self.velocity = calculate_velocity(self.velocity, self.acceleration, dt)