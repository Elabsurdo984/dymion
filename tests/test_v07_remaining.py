import pytest
from dymion import Vector, Body, buoyancy_force, intersect_circles, intersect_aabb, is_static_equilibrium

def test_buoyancy():
    # Water density = 1000, Volume = 0.1, g = 10 -> Fb = 1000 * 0.1 * 10 = 1000
    fb = buoyancy_force(1000, 0.1, g=10.0)
    assert fb.y == 1000.0

def test_collision_circles():
    p1 = Vector(0, 0, 0)
    p2 = Vector(1, 0, 0)
    # R1=0.6, R2=0.6 -> dist=1 < 1.2 (True)
    assert intersect_circles(p1, 0.6, p2, 0.6) == True
    # R1=0.4, R2=0.4 -> dist=1 > 0.8 (False)
    assert intersect_circles(p1, 0.4, p2, 0.4) == False

def test_collision_aabb():
    # Box 1: (0,0,0) to (1,1,1)
    min1, max1 = Vector(0,0,0), Vector(1,1,1)
    # Box 2: (0.5, 0.5, 0.5) to (1.5, 1.5, 1.5)
    min2, max2 = Vector(0.5, 0.5, 0.5), Vector(1.5, 1.5, 1.5)
    assert intersect_aabb(min1, max1, min2, max2) == True
    
    # Box 3: (2,2,2) to (3,3,3)
    min3, max3 = Vector(2,2,2), Vector(3,3,3)
    assert intersect_aabb(min1, max1, min3, max3) == False

def test_static_equilibrium():
    b = Body(mass=10.0)
    # Apply two opposite forces
    b.apply_force(Vector(10, 0, 0))
    b.apply_force(Vector(-10, 0, 0))
    assert is_static_equilibrium(b) == True
    
    # Add a force without balance
    b.apply_force(Vector(0, 5, 0))
    assert is_static_equilibrium(b) == False
