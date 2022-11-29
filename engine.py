from typing import Iterable, Any

from tcod.context import Context
from tcod.console import Console
from tcod.map import compute_fov

from entity import Entity
from input_handlers import EventHandler
from game_map import GameMap
import time
from random import choice, uniform, choices

class Engine:
    def __init__(self, event_handler: EventHandler, game_map: GameMap, player: Entity):
        self.event_handler, self.game_map, self.player = event_handler, game_map, player
        self.radius = 8
        self.wait_time = 0.5
        self.update_fov()
        self.start_time = int(time.time())

    def handle_events(self, events: Iterable[Any]) -> None:
        for event in events:
            action = self.event_handler.dispatch(event)
            if action is None: continue
            action.perform(self, self.player)
        self.fluctuate_fov()
        self.update_fov()

    def update_fov(self) -> None:
        self.game_map.dim[:] = compute_fov(
            self.game_map.tiles['transparent'], 
            (self.player.x, self.player.y), radius=self.radius)
        self.game_map.visible[:] = compute_fov(
            self.game_map.tiles['transparent'], 
            (self.player.x, self.player.y), radius=3)
        self.game_map.explored |= self.game_map.dim

    def fluctuate_fov(self):
        if time.time()-self.start_time>self.wait_time:
            self.start_time = time.time()
            self.wait_time = uniform(0.3, 0.8)
            past = self.radius
            change = choices([-1, 1], (past, 13-past))[0]
            self.radius = past+change

    def render(self, console: Console, context: Context):
        self.game_map.render(console)

        context.present(console)
        console.clear()