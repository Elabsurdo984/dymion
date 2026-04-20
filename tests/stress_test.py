import pytest
import math
from dymion import Vector, Body, Particle
from dymion.dynamics import universal_gravitation, gravity, friction

def test_vector_division_by_zero():
    """BUG HUNT: What happens when normalizing a Zero Vector?"""
    v = Vector(0, 0, 0)
    # This should not raise ZeroDivisionError, it should return (0,0,0) safely
    res = v.normalize()
    assert res.x == 0 and res.y == 0 and res.z == 0

def test_gravitation_at_zero_distance():
    """BUG HUNT: What happens when two bodies are at the exact same point?"""
    b1 = Body(mass=100, position=Vector(0,0,0))
    b2 = Body(mass=100, position=Vector(0,0,0))
    # This might raise ZeroDivisionError in the current implementation
    f = universal_gravitation(b1, b2)
    assert f.magnitude == 0

def test_invalid_vector_additions():
    """BUG HUNT: What happens when adding a scalar to a Vector?"""
    v = Vector(1, 1, 1)
    with pytest.raises(TypeError):
        # We expect a clear TypeError, not an AttributeError like 'int has no x'
        res = v + 5

def test_negative_mass_prevention():
    """BUG HUNT: Can we create a body with negative mass?"""
    with pytest.raises(ValueError):
        Body(mass=-10.0)

def test_immense_values_stability():
    """BUG HUNT: Stability with astronomical values."""
    p = Particle(acceleration=Vector(1e20, 1e20, 1e20))
    p.update(1e20)
    # Should not crash, just return huge floats
    assert p.velocity.magnitude > 0

def test_friction_at_rest():
    """BUG HUNT: Does friction move a static object?"""
    b = Body(mass=10, position=Vector(0,0,0))
    b.velocity = Vector(0,0,0)
    f = friction(b, mu=0.5, normal_force=100.0)
    # Friction should be zero if velocity is zero
    assert f.magnitude == 0
