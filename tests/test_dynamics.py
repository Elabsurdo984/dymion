import pytest
from dymion import Vector, Body

def test_body_mass_validation():
    with pytest.raises(ValueError):
        Body(mass=-1.0)

def test_body_force_application():
    # m=10, F=50 -> a=5
    b = Body(mass=10.0)
    b.apply_force(Vector(50, 0, 0))
    b.update(1.0)
    assert b.acceleration.x == 5.0
    assert b.velocity.x == 5.0
    assert b.position.x == 2.5 # 0.5 * a * t^2 = 0.5 * 5 * 1^2
