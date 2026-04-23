from __future__ import annotations
from dataclasses import dataclass

@dataclass(frozen=True)
class Material:
    """
    Represents physical properties of a material
    """
    name: str
    density: float # kg/m^3
    restitution: float # 0 to 1 (bounciness)
    static_friction: float 
    kinetic_friction: float

# --- Professional Presets ---
STEEL = Material("Steel", 7850.0, 0.6, 0.74, 0.57)
WOOD = Material("Wood", 600.0, 0.4, 0.4, 0.2)
ICE = Material("Ice", 917.0, 0.1, 0.1, 0.03)
RUBBER = Material("Rubber", 1100.0, 0.9, 0.9, 0.8)