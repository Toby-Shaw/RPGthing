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
        ('light', graphic_dt),
        ('dim', graphic_dt)
    ]
)

def new_tile(
    *, walkable: int, transparent: int, dark: Tuple[int, Tuple[int, int, int], Tuple[int, int, int]],
    light: Tuple[int, Tuple[int, int, int], Tuple[int, int, int]], dim: Tuple[int, Tuple[int, int, int],
    Tuple[int, int, int]]
    ) -> np.ndarray:
    """Helper Function to make a tile with associated attributes"""
    return np.array((walkable, transparent, dark, light, dim), dtype=tile_dt)

SHROUD = np.array((ord(' '), (255, 255, 255), (0, 0, 0)), dtype=graphic_dt)

floor = new_tile(
    walkable=True, 
    transparent=True, 
    dark=(ord(' '), (60, 60, 160), (50, 50, 150)),
    light=(ord('^'), (230, 200, 80), (200, 180, 50)),
    dim=(ord('`'), (170, 150, 50), (150, 130, 20))
)
wall = new_tile(
    walkable=False, 
    transparent=False, 
    dark=(ord(' '), (255, 255, 255), (0, 0, 100)),
    light=(ord(' '), (255, 255, 255), (130, 110, 50)),
    dim=(ord(' '), (255, 255, 255), (80, 60, 20))
)