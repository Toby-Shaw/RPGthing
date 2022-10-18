from pickle import TRUE
import tcod
from input_handlers import EventHandler
from engine import Engine
from entity import Entity
from game_map import GameMap

def main():
    s_width = 80
    s_height = 50
    g_width = 80
    g_height = 45

    tileset = tcod.tileset.load_tilesheet("Games/RPGthing/randomimage.png", 32, 8, tcod.tileset.CHARMAP_TCOD)
    event_handler = EventHandler()

    player = Entity(s_width // 2, s_height // 2, '@', (255, 255, 0))
    npc = Entity(s_width//2-5, s_height//2-5, "@", (255, 255, 255))
    entities = {npc, player}

    game_map = GameMap(g_width, g_height)
    engine = Engine(entities = entities, event_handler = event_handler, game_map = game_map, player = player)

    with tcod.context.new_terminal(
        s_width,
        s_height,
        tileset=tileset,
        title = "RPG?",
        vsync=True) as context:
        root_console = tcod.Console(s_width, s_height, order='F')
        while True:
            engine.render(console=root_console, context=context)
            events = tcod.event.wait()
            engine.handle_events(events)
                
if __name__ == '__main__':
    main()