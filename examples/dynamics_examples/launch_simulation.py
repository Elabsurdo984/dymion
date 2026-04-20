from dymion import Vector, Body
from dymion.dynamics import gravity, friction

# 10kg on a floor
box = Body(mass=10.0)

# Constants
MU_KINETIC = 0.3 # Wood on wood friction
NORMAL_FORCE = 10.0 * 9.81 # mass * gravity

# Initial Push
box.velocity = Vector(20, 0, 0) # Moving at 20 m/s

print("Simulation: A box sliding on a floor with friction.")
for t in range(10):
    # Apply friction (opposes motion)
    f_friction = friction(box, MU_KINETIC, NORMAL_FORCE)
    box.apply_force(f_friction)

    box.update(0.1) # Step of 0.1 seconds
    box.clear_forces() # Important: reset forces for next step

    print(f"Time {t*0.1:.1f}s | Speed: {box.velocity.x:.2f} m/s | Pos: {box.position.x:.2f}m")
    
    if box.velocity.x <= 0:
        print("The box has stopped.")
        break
