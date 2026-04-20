import pytest
import math
from dymion import Vector
from dymion.kinematics import (
    calculate_angular_position,
    calculate_angular_velocity,
    get_tangential_velocity,
    get_centripetal_acceleration,
    polar_to_cartesian
)

def test_angular_position_mcu():
    theta = calculate_angular_position(theta0=0, omega0=10, t=2.0, alpha=0)
    assert theta == 20.0

def test_angular_position_mcua():
    theta = calculate_angular_position(theta0=0, omega0=0, t=2.0, alpha=2.0)
    assert theta == 4.0

def test_angular_velocity():
    omega = calculate_angular_velocity(omega0=5, alpha=2, t=3.0)
    assert omega == 11.0

def test_tangential_and_centripetal():
    assert get_tangential_velocity(omega=2, radius=5) == 10.0
    assert get_centripetal_acceleration(omega=2, radius=3) == 12.0

def test_polar_to_cartesian():
    pos = polar_to_cartesian(radius=1.0, theta=math.pi / 2)
    assert pos.x == pytest.approx(0.0, abs=1e-9)
    assert pos.y == pytest.approx(1.0, abs=1e-9)