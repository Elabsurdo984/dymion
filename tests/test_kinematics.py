import pytest
from dymion import Vector, Particle, calculate_position

def test_calculate_position_mru():
    # v=10, t=2 -> pos=20
    pos = calculate_position(Vector(0,0,0), Vector(10,0,0), time=2.0)
    assert pos.x == 20.0

def test_particle_initial_state():
    p = Particle()
    assert p.position.x == 0.0
    assert p.velocity.x == 0.0

def test_particle_update_mrua():
    # a=2, t=1 -> v=2, pos=1 (0.5*a*t^2)
    p = Particle(acceleration=Vector(2, 0, 0))
    p.update(1.0)
    assert p.velocity.x == 2.0
    assert p.position.x == 1.0
