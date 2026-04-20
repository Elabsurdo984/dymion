from dymion import Vector, Particle

# Create a particle
# Initial position: (0, 0, 0)
# Initial velocity: (0, 20, 0) m/s (upwards)
# Acceleration: (0, -9.81, 0) m/s^2 (gravity)
ball = Particle(
    position=Vector(0, 0, 0),
    velocity=Vector(0, 20, 0),
    acceleration=Vector(0, -9.81, 0)
)

print(f"Starting simulation: {ball}")

# Simulate 3 seconds in steps of 1 second
for t in range(1, 4):
    ball.update(1.0) # Move 1 second forward
    print(f"Time {t}s: {ball}")


