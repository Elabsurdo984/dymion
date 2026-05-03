import pytest
from dymion import Vector, Body, calculate_center_of_mass, calculate_total_momentum

def test_center_of_mass_simple():
    # Two identical bodies at (0,0,0) and (10,0,0)
    # Center of mass should be at (5,0,0)
    b1 = Body(mass=1.0, position=Vector(0, 0, 0))
    b2 = Body(mass=1.0, position=Vector(10, 0, 0))
    
    com = calculate_center_of_mass([b1, b2])
    assert com.x == 5.0
    assert com.y == 0.0

def test_center_of_mass_weighted():
    # m1=1 at (0,0,0), m2=3 at (4,0,0)
    # R = (1*0 + 3*4) / (1+3) = 12 / 4 = 3
    b1 = Body(mass=1.0, position=Vector(0, 0, 0))
    b2 = Body(mass=3.0, position=Vector(4, 0, 0))
    
    com = calculate_center_of_mass([b1, b2])
    assert com.x == 3.0

def test_total_momentum():
    b1 = Body(mass=2.0, velocity=Vector(5, 0, 0))
    b2 = Body(mass=1.0, velocity=Vector(-10, 0, 0))
    # P = 2*5 + 1*(-10) = 0
    p = calculate_total_momentum([b1, b2])
    assert p.x == 0.0

def test_center_of_mass_empty():
    assert calculate_center_of_mass([]).magnitude == 0
