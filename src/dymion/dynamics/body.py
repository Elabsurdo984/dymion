from __future__ import annotations
from typing import Optional, List
from ..core.vector import Vector
from ..kinematics.linear import Particle
from .materials import Material, STEEL

class Body(Particle):
    """
    A Body is a Particle with mass and moment of inertia, 
    allowing for both linear (forces) and rotational (torques) dynamics.
    """
    def __init__(
        self, 
        mass: float = 1.0,
        material: Material = STEEL,
        moment_of_inertia: float = 1.0,
        position: Optional[Vector] = None, 
        velocity: Optional[Vector] = None,
        acceleration: Optional[Vector] = None
    ):
        super().__init__(position, velocity, acceleration)
        if mass <= 0:
            raise ValueError("Mass must be greater than zero.")
        if moment_of_inertia <= 0:
            raise ValueError("Moment of inertia must be greater than zero.")
            
        self.mass = float(mass)
        self.material = material
        self.inertia = float(moment_of_inertia)
        
        # Rotational state (3D angles, angular velocity and acceleration)
        self.orientation = Vector(0, 0, 0)
        self.angular_velocity = Vector(0, 0, 0)
        self.angular_acceleration = Vector(0, 0, 0)
        
        self._forces: List[Vector] = []
        self._torques: List[Vector] = []

    def apply_force(self, force: Vector):
        """Adds a force vector to the body."""
        self._forces.append(force)

    def apply_torque(self, torque: Vector):
        """Adds a torque (rotational force) to the body."""
        self._torques.append(torque)

    def clear_forces(self):
        """Clears all linear forces acting on the body."""
        self._forces = []
        
    def clear_torques(self):
        """Clears all rotational torques acting on the body."""
        self._torques = []

    def update(self, dt: float):
        """
        Updates both linear and rotational state based on Newton's Laws.
        """
        # --- Linear Dynamics (F = m * a) ---
        net_force = Vector(0, 0, 0)
        for f in self._forces:
            net_force += f
        self.acceleration = net_force * (1.0 / self.mass)
        super().update(dt) # Updates position and velocity
        
        # --- Rotational Dynamics (Tau = I * alpha) ---
        net_torque = Vector(0, 0, 0)
        for t in self._torques:
            net_torque += t
        
        # Angular Acceleration = Net Torque / Inertia
        self.angular_acceleration = net_torque * (1.0 / self.inertia)
        
        # Euler Integration for rotation
        self.angular_velocity += self.angular_acceleration * dt
        self.orientation += self.angular_velocity * dt
