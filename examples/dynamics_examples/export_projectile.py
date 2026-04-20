from dymion import Vector, Body, export_to_json
from dymion.dynamics import gravity

# 1. Setup the simulation
# A 2kg projectile launched at 45 degrees
projectile = Body(mass=2.0, position=Vector(0, 0, 0))
projectile.velocity = Vector(15, 15, 0) # Initial velocity vector

# This list will store every stem of our simulation
simulation_history = []

print("Simulating projectile with JSON export...")

# 2. Run the simulation loop
dt = 0.05 # 50ms steps for high precision
for i in range(200): # Max 10 seconds of simulation
    time_elapsed = i * dt

    # Apply forces
    projectile.apply_force(gravity(projectile))

    # Update state
    projectile.update(dt)
    projectile.clear_forces()

    # Record current state for export
    simulation_history.append({
        "step": i,
        "time_s": round(time_elapsed, 3),
        "position": projectile.position, # Vector will be auto-processed
        "velocity": projectile.velocity,
        "speed_ms": round(projectile.velocity.magnitude, 2)
    })

    # Stop if is hits the ground
    if projectile.position.y < 0:
        print(f"Hit the ground at {time_elapsed:.2f}s")
        break

# 3. Export to JSON
export_to_json(simulation_history, "examples/dynamics_examples/projectile_data.json")
     