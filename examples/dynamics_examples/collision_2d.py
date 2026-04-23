from dymion import Vector, Body
from dymion.dynamics import resolve_collision_2d, RUBBER, STEEL

# Simulate two balls colliding in 2D space
# Ball 1: Steel (heavy and less bouncy)
ball1 = Body(
    mass=10.0, 
    position=Vector(0, 0, 0), 
    velocity=Vector(5, 2, 0),
    material=STEEL
)

# Ball 2: Rubber (lighter and very bouncy)
ball2 = Body(
    mass=2.0, 
    position=Vector(4, 3, 0), 
    velocity=Vector(-2, -1, 0),
    material=RUBBER
)

print("Pre-collision states:")
print(f"Ball 1 (Steel):  Pos={ball1.position}, Vel={ball1.velocity}")
print(f"Ball 2 (Rubber): Pos={ball2.position}, Vel={ball2.velocity}")
print("-" * 50)

# Resolve the collision
resolve_collision_2d(ball1, ball2)

print("Post-collision states:")
print(f"Ball 1 (Steel):  Pos={ball1.position}, Vel={ball1.velocity}")
print(f"Ball 2 (Rubber): Pos={ball2.position}, Vel={ball2.velocity}")
