import pytest
from dymion import Vector

def test_vector_creation():
    v = Vector(1, 2, 3)
    assert v.x == 1.0
    assert v.y == 2.0
    assert v.z == 3.0

def test_vector_addition():
    v1 = Vector(1, 2, 3)
    v2 = Vector(4, 5, 6)
    res = v1 + v2
    assert (res.x, res.y, res.z) == (5.0, 7.0, 9.0)

def test_vector_subtraction():
    v1 = Vector(10, 10, 10)
    v2 = Vector(1, 2, 3)
    res = v1 - v2
    assert (res.x, res.y, res.z) == (9.0, 8.0, 7.0)

def test_vector_magnitude():
    v = Vector(3, 4, 0)
    assert v.magnitude == 5.0

def test_vector_normalization():
    v = Vector(10, 0, 0)
    nv = v.normalize()
    assert nv.x == 1.0
    assert nv.magnitude == 1.0
