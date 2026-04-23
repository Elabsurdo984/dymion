import pytest
from dymion import Vector, Body
from dymion.dynamics import resolve_collision_2d, STEEL, RUBBER

def test_material_assignment():
    b = Body(mass=5.0, material=STEEL)
    assert b.material.name == "Steel"
    assert b.material.density == 7850.0

def test_collision_2d_momentum_conservation():
    # Two identical bodies colliding head-on
    b1 = Body(mass=1.0, position=Vector(0,0,0), velocity=Vector(10,0,0), material=STEEL)
    b2 = Body(mass=1.0, position=Vector(2,0,0), velocity=Vector(-10,0,0), material=STEEL)
    
    initial_momentum = b1.velocity * b1.mass + b2.velocity * b2.mass
    
    resolve_collision_2d(b1, b2)
    
    final_momentum = b1.velocity * b1.mass + b2.velocity * b2.mass
    
    # Total momentum should be conserved
    assert final_momentum.x == pytest.approx(initial_momentum.x)
    assert final_momentum.y == pytest.approx(initial_momentum.y)

def test_collision_restitution():
    # Steel (restitution 0.6) vs Rubber (restitution 0.9)
    # The collision should use the minimum (0.6)
    b1 = Body(mass=1.0, position=Vector(0,0,0), velocity=Vector(10,0,0), material=STEEL)
    b2 = Body(mass=1.0, position=Vector(1,0,0), velocity=Vector(0,0,0), material=RUBBER)
    
    resolve_collision_2d(b1, b2)
    # B1 should bounce back or slow down significantly
    assert b1.velocity.x < 10.0
