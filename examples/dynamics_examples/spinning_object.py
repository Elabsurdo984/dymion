from dymion import Vector, Body
from dymion.dynamics import calculate_torque, inertia_cylinder

# Simulating a spinning wheel (cylinder)
# Mass: 2kg, Radius: 0.5m
m, r = 2.0, 0.5
inertia = inertia_cylinder(m, r)

wheel = Body(mass=m, moment_of_inertia=inertia)

# Applying a tangential force to make it spin
# Lever arm: (0.5, 0, 0) -> Force applied at the edge
# Force: (0, 10, 0) -> 10 Newtons upwards
lever = Vector(0.5, 0, 0)
force = Vector(0, 10, 0)

torque = calculate_torque(lever, force)
wheel.apply_torque(torque)

print(f"Initial State: Angular Vel = {wheel.angular_velocity}")
print(f"Applying Torque: {torque}")
print("-" * 40)

# Simulate for 5 seconds
for t in range(1, 6):
    wheel.update(1.0)
    # Torque is applied constantly in this simulation
    
    # Orientation.z is the rotation angle in the 2D plane
    angle_deg = (wheel.orientation.z * 180 / 3.14159) % 360
    
    print(f"Time {t}s | Angle: {angle_deg:>6.1f}° | Ang. Vel: {wheel.angular_velocity.z:.2f} rad/s")
