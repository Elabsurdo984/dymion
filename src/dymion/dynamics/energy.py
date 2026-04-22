from __future__ import annotations
from ..core.vector import Vector
from .body import Body
from .forces import G_EARTH


def kinetic_energy(body: Body) -> float:
    """
    Calculate the kinetic energy of a body.
    
    Kinetic energy is the energy possessed by an object due to its motion.
    Formula: Ek = 1/2 * m * v^2
    
    Parameters
    ----------
    body : Body
        The body object containing mass and velocity information.
    
    Returns
    -------
    float
        The kinetic energy of the body in joules (J).
    
    Examples
    --------
    >>> body = Body(mass=10.0, velocity=Vector(2.0, 0.0, 0.0))
    >>> kinetic_energy(body)
    20.0
    """
    speed = body.velocity.magnitude
    return 0.5 * body.mass * (speed**2)

def gravitational_potential_energy(body: Body, height: float, g: float = G_EARTH) -> float:
    """
    Calculate the gravitational potential energy of a body.
    
    Gravitational potential energy is the energy an object possesses
    due to its position in a gravitational field.
    Formula: Ep = m * g * h
    
    Parameters
    ----------
    body : Body
        The body object containing mass information.
    height : float
        The height of the body above the reference point in meters (m).
    g : float, optional
        The acceleration due to gravity in m/s^2. Default is G_EARTH (9.81 m/s^2).
    
    Returns
    -------
    float
        The gravitational potential energy of the body in joules (J).
    
    Examples
    --------
    >>> body = Body(mass=5.0, velocity=Vector(0.0, 0.0, 0.0))
    >>> gravitational_potential_energy(body, height=10.0)
    490.5
    """
    return body.mass * g * height

def elastic_potential_energy(k: float, displacement_magnitude: float) -> float:
    """
    Calculate the elastic potential energy stored in a spring.
    
    Elastic potential energy is the energy stored as a result of
    deforming an elastic object, such as a spring.
    Formula: Ee = 1/2 * k * x^2
    
    Parameters
    ----------
    k : float
        The spring constant (stiffness) in newtons per meter (N/m).
    displacement_magnitude : float
        The magnitude of displacement from the equilibrium position in meters (m).
    
    Returns
    -------
    float
        The elastic potential energy in joules (J).
    
    Examples
    --------
    >>> elastic_potential_energy(k=100.0, displacement_magnitude=0.1)
    0.5
    """
    return 0.5 * k * (displacement_magnitude**2)

def mechanical_energy(body: Body, height: float, g: float = G_EARTH) -> float:
    """
    Calculate the total mechanical energy of a body.
    
    Mechanical energy is the sum of kinetic energy and potential energy
    in a system.
    Formula: E_mech = Ek + Ep
    
    Parameters
    ----------
    body : Body
        The body object containing mass and velocity information.
    height : float
        The height of the body above the reference point in meters (m).
    g : float, optional
        The acceleration due to gravity in m/s^2. Default is G_EARTH (9.81 m/s^2).
    
    Returns
    -------
    float
        The total mechanical energy of the body in joules (J).
    
    Examples
    --------
    >>> body = Body(mass=10.0, velocity=Vector(3.0, 0.0, 0.0))
    >>> mechanical_energy(body, height=5.0)
    740.5
    """
    return kinetic_energy(body) + gravitational_potential_energy(body, height, g)

def work(force: Vector, displacement: Vector) -> float:
    """
    Calculate the work done by a force on an object.
    
    Work is the dot product of force and displacement vectors.
    Formula: W = F · d = |F| * |d| * cos(θ)
    
    Parameters
    ----------
    force : Vector
        The force vector acting on the object in newtons (N).
    displacement : Vector
        The displacement vector in meters (m).
    
    Returns
    -------
    float
        The work done in joules (J).
    
    Examples
    --------
    >>> F = Vector(10.0, 0.0, 0.0)
    >>> d = Vector(5.0, 0.0, 0.0)
    >>> work(F, d)
    50.0
    """
    return (force.x * displacement.x) + (force.y * displacement.y) + (force.z * displacement.z)

def power(work_done: float, time: float) -> float:
    """
    Calculate the power when work is done over a time interval.
    
    Power is the rate at which work is done or energy is transferred.
    Formula: P = W / t
    
    Parameters
    ----------
    work_done : float
        The work done in joules (J).
    time : float
        The time interval in seconds (s). Must be positive.
    
    Returns
    -------
    float
        The power in watts (W). Returns 0.0 if time is zero or negative.
    
    Examples
    --------
    >>> power(work_done=100.0, time=10.0)
    10.0
    """
    if time <= 0:
        return 0.0
    return work_done / time
