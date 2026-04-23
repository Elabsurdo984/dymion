from __future__ import annotations
from typing import Optional, List
from ..core.vector import Vector
from ..kinematics.linear import Particle
from .materials import Material, STEEL

class Body(Particle):
    """
    A Body is a particle with mass, allowing for dynamic interactions (forces).
    Inherits from Particle to keep kinematic properties (pos, vel, acc).
    """
    def __init__(
            self, 
            mass: float = 1.0,
            material: Material = STEEL, 
            position: Optional[Vector] = None, 
            velocity: Optional[Vector] = None, 
            acceleration: Optional[Vector] = None
    ):
        super().__init__(position, velocity, acceleration)
        if mass <= 0:
            raise ValueError("Mass must be greater than zero.")
        self.mass = float(mass)
        self.material = material 
        self._forces: List[Vector] = [] # List of forces acting on the body

    def apply_force(self, force: Vector):
        """Adds a force vector to the body"""
        self._forces.append(force)
    
    def clear_forces(self):
        """Clears all forces acting on the body"""
        self._forces = []
    
    def update(self, dt: float):
        """
        Calculates the net acceleration based on Newton's Second Law (a = F/m)
        and then updates position and velocity
        """
        # Sum of all the forces (Net Force)
        net_force = Vector(0, 0, 0)
        for f in self._forces:
            net_force += f
        
        # Newton's Second Law: a = F / m
        self.acceleration = net_force * (1.0 / self.mass)

        # Use the kinematic update for particle
        super().update(dt)