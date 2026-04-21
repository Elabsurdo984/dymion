from dymion import Vector, Body
from dymion.dynamics import kinetic_energy, gravitational_potential_energy

# A 5kg ball dropped from 100 meters
ball = Body(mass=5.0, position=Vector(0, 100, 0))

print(f"Initial State: Height=100m, Speed=0m/s")
print("-" * 40)

for t in range(5):
    # Calculate energies before update
    ke = kinetic_energy(ball)
    pe = gravitational_potential_energy(ball, ball.position.y)
    total_e = ke + pe

    print(f"Time {t}s | Height: {ball.position.y:>6.2f}m | KE: {ke:>7.2f}J | PE: {pe:>7.2f}J | Total: {total_e:.2f}j")

    # Simple manual update for gravity (g=9.81)
    # v = v0 + a*t, y = y0 + v*t
    ball.velocity += Vector(0, -9.81, 0)
    ball.position += ball.velocity * 1.0 # 1 second steps

    if ball.position.y <= 0:
        print("-" * 40)
        print("Hit the Ground!")
        break