from .core.vector import Vector
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
    escape_velocity
)

__version__ = "0.1.0"
