from typing import Tuple
import numpy as np

graphic_dt = np.dtype(
    [   
        ("ch", np.int32),  #Unicode
        ("fg", "3B"),   #Foreground
        ('bg', "3B"),   #Background
    ]
)

tile_dt = np.dtype(
    [
        ('walkable', np.bool), # True to walk
        ('transparent', np.bool),  #True if it doesn't block FOV
        ('dark', graphic_dt),  # Graphics when not in FOV
    ]
)

def new_tile(
    *, walkable: int, transparent: int, dark: Tuple[int, Tuple[int, int, int], Tuple[int, int, int]],
    ) -> np.ndarray:
    """Helper Function to make a tile with associated attributes"""
    return np.array((walkable, transparent, dark), dtype=tile_dt)

floor = new_tile(
    walkable=True, transparent=True, dark=(ord(' '), (255, 255, 255), (50, 50, 150))
)
wall = new_tile(
    walkable=False, transparent=False, dark=(ord(' '), (255, 255, 255), (0, 0, 100))
)