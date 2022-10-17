from pickle import TRUE
import tcod
from input_handlers import EventHandler
from actions import EscapeAction, MovementAction

def main():
    s_width = 80
    s_height = 50
    play_x = s_width // 2
    play_y = s_height // 2

    tileset = tcod.tileset.load_tilesheet("Games/RPGthing/randomimage.png", 32, 8, tcod.tileset.CHARMAP_TCOD)
    event_handler = EventHandler()

    with tcod.context.new_terminal(
        s_width,
        s_height,
        tileset=tileset,
        title = "RPG?",
        vsync=True) as context:
        root_console = tcod.Console(s_width, s_height, order='F')
        while True:
            root_console.print(x=play_x, y=play_y, string='@')
            context.present(root_console)
            root_console.clear()
            for event in tcod.event.wait():
                action = event_handler.dispatch(event)
                if action is None: continue
                elif isinstance(action, MovementAction):
                    play_x += action.dx
                    play_y += action.dy
                elif isinstance(action, EscapeAction):
                    raise SystemExit
                
if __name__ == '__main__':
    main()