from __future__ import annotations
from .body import Body
from ..core.vector import Vector

def is_static_equilibrium(body: Body, tolerance: float = 1e-6) -> bool:
    """
    Checks if a body is in static equilibrium (Net Force ≈ 0 and Net Torque ≈ 0).
    """
    net_force = Vector(0, 0, 0)
    for f in body._forces:
        net_force += f
        
    net_torque = Vector(0, 0, 0)
    for t in body._torques:
        net_torque += t
        
    return net_force.magnitude < tolerance and net_torque.magnitude < tolerance
