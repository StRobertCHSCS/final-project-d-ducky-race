import arcade



WIDTH = 1360
HEIGHT = 710
score = 0

current_screen = "menu"
high_score = 0


def update(delta_time):
    pass

def on_draw():
    arcade.start_render()
    if current_screen == "menu":
        arcade.draw_text('Menu Screen', WIDTH/2 - 400, HEIGHT/2, arcade.color.WHITE, 80)
        arcade.draw_text('Press Space to Play', WIDTH/2 - 400 , HEIGHT/2 - 100, arcade.color.WHITE, 80)

def on_key_press(key, modifiers):
    if key == arcade.key.SPACE:
            current_screen = "start"
    elif current_screen == "start":
        if key == arcade.key.ESCAPE:
                current_screen = "menu"


def on_key_release(key, modifiers):
    pass


def on_mouse_press(x, y, button, modifiers):
    pass


def setup():
    arcade.open_window(WIDTH, HEIGHT, "My Arcade Game")
    arcade.set_background_color(arcade.color.BANGLADESH_GREEN)
    arcade.schedule(update, 1/60)

    window = arcade.get_window()
    window.on_draw = on_draw
    window.on_key_press = on_key_press
    window.on_key_release = on_key_release
    window.on_mouse_press = on_mouse_press

    arcade.run()


def draw_menu():
    pass


def draw_high_score():
    pass

def draw_timer():
    pass




if __name__ == '__main__':
    setup()
