# 🪐 Dymion

**Dymion** is a modern, high-performance Python library designed for professional physics simulations, focusing on Kinematics and Dynamics. 

Built with a hybrid approach, it offers both a clean **Object-Oriented API** for complex simulations and a **Functional API** for quick mathematical calculations.

---

## 🚀 Key Features

- **Vector-Centric:** Built-in 2D/3D Vector engine with native math operator support.
- **Kinematics Engine:** Easily simulate linear motion (MRU, MRUA) using the `Particle` class.
- **Dynamics Core:** Implementation of Newton's Laws with the `Body` class, supporting mass and multiple force accumulation.
- **Professional Standards:** Fully type-hinted, follows the `src` layout, and is ready for integration with scientific stacks like NumPy.
- **Scalable Architecture:** Designed to be easily extended with Circular Motion, Work, and Energy modules.

---

## 📦 Installation

To install **Dymion** in development mode, run:

```bash
git clone https://github.com/Elabsurdo984/dymion.git
cd dymion
pip install -e .
```

---

## 💡 Quick Start

### 1. Simple Kinematics (The Functional Way)
If you just need a quick calculation without managing state:

```python
from dymion import Vector, calculate_position

initial_pos = Vector(0, 0, 0)
initial_vel = Vector(0, 20, 0)
gravity = Vector(0, -9.81, 0)

# Calculate position after 2 seconds
final_pos = calculate_position(initial_pos, initial_vel, time=2.0, acceleration=gravity)
print(f"Position at 2s: {final_pos}")
```

### 2. Full Physics Simulation (The OOP Way)
For complex scenarios involving masses and forces:

```python
from dymion import Vector, Body

# Create a 10kg body at rest
crate = Body(mass=10.0, position=Vector(0, 0, 0))

# Apply multiple forces
crate.apply_force(Vector(50, 0, 0))   # A push
crate.apply_force(Vector(0, -98.1, 0)) # Gravity (10kg * 9.81)

# Step the simulation
crate.update(dt=0.1)
print(f"Crate Velocity: {crate.velocity}")
```

---

## 🛠 Project Structure

```text
dymion/
├── src/
│   └── dymion/
│       ├── core/          # Base Vector engine
│       ├── kinematics/    # Motion study (linear, circular)
│       └── dynamics/      # Forces, Mass, and Newton's Laws
├── tests/                 # Unit tests (Pytest)
└── pyproject.toml         # Modern build configuration
```

---

## ⚖ License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

---

**Developed with ❤️ for the physics community.**
