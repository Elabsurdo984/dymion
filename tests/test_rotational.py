import pytest
from dymion import Vector, Body
from dymion.dynamics import calculate_torque, inertia_sphere

def test_torque_calculation():
    # Force at (1, 0, 0) of (0, 10, 0) should give torque on Z axis
    lever = Vector(1, 0, 0)
    force = Vector(0, 10, 0)
    torque = calculate_torque(lever, force)
    assert torque.z == 10.0
    assert torque.x == 0.0
    assert torque.y == 0.0

def test_angular_acceleration():
    # Tau = I * alpha -> alpha = Tau / I
    # If Tau=10 and I=2, then alpha=5
    b = Body(moment_of_inertia=2.0)
    b.apply_torque(Vector(0, 0, 10))
    b.update(1.0)
    assert b.angular_acceleration.z == 5.0
    assert b.angular_velocity.z == 5.0

def test_inertia_sphere():
    # I = 2/5 * m * r^2 -> 0.4 * 10 * 1^2 = 4
    assert inertia_sphere(10.0, 1.0) == 4.0
