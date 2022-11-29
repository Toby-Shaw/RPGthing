from __future__ import annotations
import numpy as np
from tcod.console import Console

import tile_types

from typing import Iterable
from entity import Entity

class GameMap:
    def __init__(self, width:int, height:int, entities: Iterable[Entity] = ()):
        self.width, self.height = width, height
        self.entities = set(entities)
        self.tiles = np.full((width, height), fill_value=tile_types.wall, order="F")
        self.visible = np.full((width, height), fill_value=False, order='F')
        self.dim = np.full((width, height), fill_value=False, order='F')
        self.explored = np.full((width, height), fill_value=False, order='F')

    def in_bounds(self, x:int, y:int) -> bool:
        return(0<=x<self.width and 0<=y<self.height)

    def render(self, console: Console) -> None:
        """If a tile is visible, draw with "light" colors, if explored but not visible
        draw with "dark" colors, otherwise draw with SHROUD"""
        console.tiles_rgb[0:self.width, 0:self.height] = np.select(
            condlist = [self.visible, self.dim, self.explored],
            choicelist = [self.tiles['light'], self.tiles['dim'], self.tiles['dark']],
            default = tile_types.SHROUD
        )
        for entity in self.entities:
            if self.dim[entity.x, entity.y] or self.game_map.visible[entity.x, entity.y]:
                console.print(entity.x, entity.y, entity.char, fg=entity.color)

