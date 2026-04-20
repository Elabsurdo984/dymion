from dymion import Vector, Body
from dymion.dynamics import universal_gravitation

# Sun at center (very massive)
sun = Body(mass=1.989e30, position=Vector(0, 0, 0))

# Earth at 1 AU (149.6 million km)
# Initial velocity for a circular orbit is ~29,780 m/s
earth = Body(
    mass=5.972e24,
    position=Vector(1.496e11, 0, 0),
    velocity=Vector(0, 29780, 0)
)

print("Simulating Earth's orbit for 10 days...")
# Simulate 10 days in steps of 1 day (86400 seconds)
dt = 86400
for day in range(1, 11):
    f_gravity = universal_gravitation(earth, sun)
    earth.apply_force(f_gravity)
    earth.update(dt)
    earth.clear_forces()

    dist = earth.position.magnitude / 1e9 # in millions of km
    print(f"Day {day}: Distance to sun = {dist:.2f}M km | Pos: {earth.position}")