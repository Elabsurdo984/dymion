from dymion import Vector, Body
from dymion.dynamics import gravity, friction

def test_gravity_force():
    b = Body(mass=10.0)
    f_g = gravity(b, g=10.0)
    assert f_g.y == -100.0 # 10kg * 10m/s^2

def test_friction_opposes_motion():
    b = Body(mass=1.0)
    b.velocity = Vector(10, 0, 0) # Moving right
    f_f = friction(b, mu=0.5, normal_force=10.0)
    assert f_f.x < 0 # Friction must point left