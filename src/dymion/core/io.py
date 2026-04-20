import json
from typing import List, Dict
from .vector import Vector

def export_to_json(data: List[Dict], filename: str = "simulation.json"):
    """
    Exports a list of simulation steps to a JSON file.
    Example data: [{'time': 0, 'pos': Vector(0,0,0)}, ...]
    """
    # Converts Vectors to dictionaries for JSON compatibility
    processed_data = []
    for step in data:
        step_copy = step.copy()
        for key, value in step_copy.items():
            if isinstance(value, Vector):
                step_copy[key] = {"x": value.x, "y": value.y, "z": value.z}
        processed_data.append(step_copy)
    
    with open(filename, 'w') as f:
        json.dump(processed_data, f, indent=4)
    print(f"Data exported to {filename}")