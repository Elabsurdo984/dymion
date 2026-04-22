import pytest
from dymion import Vector, Body
from dymion.dynamics import linear_momentum, elastic_collision_1d

def test_linear_momentum():
    b = Body(mass=5.0, velocity=Vector(10, 0, 0))
    p = linear_momentum(b)
    assert p.x == 50.0

def test_elastic_collision_swap():
    v1, v2 = elastic_collision_1d(m1=1.0, v1=10.0, m2=1.0, v2=0.0)
    assert v1 == 0.0
    assert v2 == 10.0