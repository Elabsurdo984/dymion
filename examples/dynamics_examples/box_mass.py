from dymion import Vector, Body

box = Body(mass=10.0, position=Vector(0, 0, 0))

push_force = Vector(50, 0, 0)
box.apply_force(push_force)

print(f"Initial state: {box}")

# Simulate 5 seconds
for t in range(1, 6):
    box.update(1.0)
    print(f"Time {t}s | Pos: {box.position} | Vel: {box.velocity} | Acceleration: {box.acceleration}")
