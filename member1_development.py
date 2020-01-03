import arcade


WIDTH = 640
HEIGHT = 480


duck_x = 50
duck_y = 100
jump = False

def on_update(delta_time):
    pass

def draw_duck(x, y):
    arcade.draw_circle_filled(x, y, 25, arcade.color.YELLOW)
    arcade.draw_circle_filled(x+10, y+38, 15, arcade.color.YELLOW)
    arcade.draw_triangle_filled(x+24, y+40, x+24, y+35, x+30, y+37.5, arcade.color.DARK_RED)
    arcade.draw_circle_filled(x+15, y+45, 3, arcade.color.BLACK)
    arcade.draw_rectangle_filled(x-10,y-32, 3, 15, arcade.color.BROWN)
    arcade.draw_rectangle_filled(x+10,y-32, 3, 15, arcade.color.BROWN)


def on_draw():
    global duck_x
    global duck_y
    global jump
    arcade.start_render()

    draw_duck(duck_x, duck_y)

    if jump == True:
        duck_x += 1
        duck_y = -1/400*duck_x*(duck_y - 800)

    



def on_key_press(key, modifiers):
    global jump
    jump = True

def on_key_release(key, modifiers):
    global jump
    jump = True


def on_mouse_press(x, y, button, modifiers):
    pass


def setup():
    arcade.open_window(WIDTH, HEIGHT, "My Arcade Game")
    arcade.set_background_color(arcade.color.WHITE)
    arcade.schedule(on_update, 1/60)

    # Override arcade window methods
    window = arcade.get_window()
    window.on_draw = on_draw
    window.on_key_press = on_key_press
    window.on_key_release = on_key_release
    window.on_mouse_press = on_mouse_press

    arcade.run()


if __name__ == '__main__':
    setup()
