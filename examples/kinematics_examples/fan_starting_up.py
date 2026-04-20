from dymion.kinematics import calculate_angular_position, polar_to_cartesian
import math

# Simulating a satellite starting up
# Initial angle: 0
# Initial angular velocity: 0 rad/s
# Angular acceleration: 2.0 rad/s^2
# Radius: 0.5 meters
radius = 0.5
alpha = 2.0

print("Simulating fan blades starting up...")
for t in range(5):
    theta = calculate_angular_position(0, 0, t, alpha)
    pos = polar_to_cartesian(radius, theta)

    # Convert radians to degrees for readability
    degrees = math.degrees(theta) % 360

    print(f"Time {t}s | Angle: {degrees:.1f} | Pos: {pos}")