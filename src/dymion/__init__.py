from .core.vector import Vector
from .core.io import export_to_json
from .kinematics import (
    Particle, 
    calculate_position, 
    calculate_velocity,
    calculate_angular_position,
    calculate_angular_velocity,
    get_tangential_velocity,
    get_centripetal_acceleration,
    polar_to_cartesian
)
from .dynamics import (
    Body, 
    gravity, 
    friction, 
    spring_force, 
    air_resistance, 
    universal_gravitation,
    escape_velocity,
    centripetal_force,
    centrifugal_force
)

__version__ = "0.2.0"
