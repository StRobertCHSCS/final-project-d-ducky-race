import arcade
import random



WIDTH = 640
HEIGHT = 480
x = 25
y = 50
jump = False
counter = 0
died = False
difference = 0
first_int = random.randint(1, 9)
second_int = random.randint(1, 9)

current_screen = "menu"



def update(delta_time):
    pass

def on_draw():
    global duck_x, duck_y, jump, counter, difference, first_int, second_int
    arcade.start_render()
    if current_screen == "menu":
        arcade.draw_text("D DUCKY RACE", WIDTH/2 - 200, HEIGHT/2, arcade.color.WHITE, 30)
        arcade.draw_text('Press Space to Play', WIDTH/2 - 200, HEIGHT/2 - 50, arcade.color.WHITE, 30)
    if current_screen == "start":
        arcade.draw_circle_filled(x, y, 25, arcade.color.YELLOW)
        arcade.draw_circle_filled(x+10, y+38, 15, arcade.color.YELLOW)
        arcade.draw_triangle_filled(x+24, y+40, x+24, y+35, x+30, y+37.5, arcade.color.DARK_RED)
        arcade.draw_circle_filled(x+15, y+45, 3, arcade.color.BLACK)
        arcade.draw_rectangle_filled(x-10,y-32, 3, 15, arcade.color.BROWN)
        arcade.draw_rectangle_filled(x+10,y-32, 3, 15, arcade.color.BROWN)
        counter += 1
        if counter >= 10 and counter <= 30:
            if first_int > second_int:
                difference = first_int-second_int
                arcade.draw_text(str(first_int)+"-"+str(second_int), 200, 400, arcade.color.BLACK, 25)
            if second_int > first_int:
                difference = second_int-first_int
                arcade.draw_text(str(second_int)+"-"+str(first_int), 200, 400, arcade.color.BLACK, 25)
        if counter == 30:
            counter = 0
            first_int = random.randint(1, 9)
            second_int = random.randint(1, 9)

def on_key_press(key, modifiers):
    global current_screen
    if current_screen == "menu":
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




if __name__ == '__main__':
    setup()
