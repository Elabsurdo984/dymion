import pytest
from dymion import Vector, Body
from dymion.dynamics import (
    kinetic_energy,
    gravitational_potential_energy,
    elastic_potential_energy,
    work,
    power
)

def test_kinetic_energy():
    b = Body(mass=10.0)
    b.velocity = Vector(2, 0, 0)
    assert kinetic_energy(b) == 20.0

def test_gravitational_potential_energy():
    b = Body(mass=2.0)
    ep = gravitational_potential_energy(b, height=10.0)
    assert ep == pytest.approx(196.133, abs=1e-3)

def test_elastic_potential_energy():
    assert elastic_potential_energy(k=100.0, displacement_magnitude=2.0) == 200.0

def test_work_dot_product():
    f = Vector(10, 0, 0)
    d = Vector(5, 0, 0)
    assert work(f, d) == 50.0

    f_perp = Vector(0, 10, 0)
    assert work(f_perp, d) == 0.0

def test_power_calculation():
    assert power(work_done=100.0, time=2.0) == 50.0
    assert power(work_done=100.0, time=0.0) == 0.0