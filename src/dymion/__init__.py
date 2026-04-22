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
    Body, gravity, friction, spring_force, air_resistance, 
    universal_gravitation, escape_velocity,
    centripetal_force, centrifugal_force,
    kinetic_energy, gravitational_potential_energy,
    elastic_potential_energy, mechanical_energy,
    work, power, linear_momentum, impulse, elastic_collision_1d,
    inelastic_collision_1d
)

__version__ = "0.4.0"
