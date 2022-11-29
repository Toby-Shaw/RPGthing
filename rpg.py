from pickle import TRUE
import tcod
from input_handlers import EventHandler
from engine import Engine
from entity import Entity
from procgen import generate_dungeon

def main():
    s_width = 80
    s_height = 50
    g_width = 80
    g_height = 45

    max_rooms = 30
    room_max_size = 10
    room_min_size = 6
    max_room_monsters = 2

    tileset = tcod.tileset.load_tilesheet("Games/RPGthing/randomimage.png", 32, 8, tcod.tileset.CHARMAP_TCOD)
    event_handler = EventHandler()

    player = Entity(s_width // 2, s_height // 2, '@', (255, 255, 0))

    game_map = generate_dungeon(max_rooms=max_rooms, room_min_size = room_min_size,
    room_max_size=room_max_size, map_width=g_width, map_height=g_height, 
    player=player, max_room_monsters = max_room_monsters)

    engine = Engine(event_handler = event_handler, game_map = game_map, player = player)

    with tcod.context.new_terminal(
        s_width,
        s_height,
        tileset=tileset,
        title = "RPG?",
        vsync=True) as context:
        root_console = tcod.Console(s_width, s_height, order='F')
        while True:
            engine.render(console=root_console, context=context)
            events = tcod.event.get()
            engine.handle_events(events)
                
if __name__ == '__main__':
    main()