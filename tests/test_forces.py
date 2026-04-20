from dymion import Vector, Body
from dymion.dynamics import gravity, friction
from dymion.dynamics import universal_gravitation, G_UNIVERSAL
import pytest

def test_gravity_force():
    b = Body(mass=10.0)
    f_g = gravity(b, g=10.0)
    assert f_g.y == -100.0 # 10kg * 10m/s^2

def test_friction_opposes_motion():
    b = Body(mass=1.0)
    b.velocity = Vector(10, 0, 0) # Moving right
    f_f = friction(b, mu=0.5, normal_force=10.0)
    assert f_f.x < 0 # Friction must point left

def test_universal_gravitation():
    # Two bodies of 1e10 kg separated by 100 meters
    b1 = Body(mass=1e10, position=Vector(0, 0, 0))
    b2 = Body(mass=1e10, position=Vector(100, 0, 0))

    f = universal_gravitation(b1, b2)

    # Expected magnitude: G * (1e10 * 1e10) / 100^2
    expected_mag = G_UNIVERSAL * (1e20) / 10000
    assert f.x == pytest.approx(expected_mag)
    assert f.y == 0
    