import arcade
import random

WIDTH = 640
HEIGHT = 480


duck_x = 25
duck_y = 50
jump = False
counter = 0

def on_update(delta_time):
    pass

def draw_duck(x, y):
    arcade.draw_circle_filled(x, y, 25, arcade.color.YELLOW)
    arcade.draw_circle_filled(x+10, y+38, 15, arcade.color.YELLOW)
    arcade.draw_triangle_filled(x+24, y+40, x+24, y+35, x+30, y+37.5, arcade.color.DARK_RED)
    arcade.draw_circle_filled(x+15, y+45, 3, arcade.color.BLACK)
    arcade.draw_rectangle_filled(x-10,y-32, 3, 15, arcade.color.BROWN)
    arcade.draw_rectangle_filled(x+10,y-32, 3, 15, arcade.color.BROWN)

def draw_title():
    arcade.draw_text("D DUCKY RACE", 50, 500, arcade.color.BLACK, 30)

def on_draw():
    global duck_x
    global duck_y
    global jump
    global counter
    arcade.start_render()

    draw_duck(duck_x, duck_y)

    counter += 1
    if 10<counter:
        x = random.randint(1, 9)
        y = random.randint(1, 9)
        if x > y:
            arcade.draw_text(str(x)+"-"+str(y), 200, 400, arcade.color.BLACK, 25)
        if y > x:
            arcade.draw_text(str(y)+"-"+str(x), 200, 400, arcade.color.BLACK, 25)
    if counter == 40:
        counter = 0
        

    if jump == True and duck_x < 104: 
        duck_x += 3
        duck_y = -1/10*(duck_x-65)**2 + 130
    elif duck_x >= 105:
        while duck_x>25:
            duck_x-=2
            duck_y = 50
        jump = False
    



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
    arcade.set_background_color(arcade.color.LIGHT_BLUE)
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
