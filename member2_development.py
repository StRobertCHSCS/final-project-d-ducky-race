"""
--------------------------------------------------------------------------------------------------------------------
Name:   member1_development.py
Purpose:    the development of the first member
Author: SOh
Created:
--------------------------------------------------------------------------------------------------------------------
"""
import arcade
import random

WIDTH = 640
HEIGHT = 480


duck_x = 25
duck_y = 48
person_x = 0
jump = False
current_screen = "menu"
difference = 0
counter = 0
first_int = random.randint(1, 9)
second_int = random.randint(1, 9)
score = 0
elapsed_time = 0
timing  = True
high_score = 0


def on_update(delta_time):
    global elapsed_time, score
    if timing == True:
        elapsed_time += delta_time
        elapsed_time = round(elapsed_time, 2)
    elif timing == False:
        if score == 0:
            f = open("high_score", "w+")
            f.write(str(elapsed_time))
            f.close()
            f = open("high_score", "r+")
            if f.mode == "r+":
                score = f.read()
                f.close()
        if elapsed_time < float(score):
            f = open("high_score", "w+")
            f.write(str(elapsed_time))
            f.close()
            f = open("high_score", "r+")
            if f.mode == "r+":
                score = f.read()
                f.close()

def draw_duck(x, y):
    arcade.draw_circle_filled(x, y, 25, arcade.color.YELLOW)
    arcade.draw_circle_filled(x+10, y+38, 15, arcade.color.YELLOW)
    arcade.draw_triangle_filled(x+24, y+40, x+24, y+35, x+30, y+37.5, arcade.color.DARK_RED)
    arcade.draw_circle_filled(x+15, y+45, 3, arcade.color.BLACK)
    arcade.draw_rectangle_filled(x-10,y-32, 3, 15, arcade.color.BROWN)
    arcade.draw_rectangle_filled(x+10,y-32, 3, 15, arcade.color.BROWN)

def draw_person(x):
    arcade.draw_rectangle_filled(610+x, 50, 3, 30, arcade.color.BLACK)
    arcade.draw_circle_filled(610+x, 70, 15, arcade.color.BLACK)
    arcade.draw_rectangle_filled(610+x, 50, 40, 3, arcade.color.BLACK)
    arcade.draw_rectangle_filled(600+x, 25, 30, 3, arcade.color.BLACK, 50)
    arcade.draw_rectangle_filled(620+x, 25, 30, 3, arcade.color.BLACK, 140)

def on_draw(): 
    global duck_x, duck_y, jump, difference, counter, first_int, second_int, person_x

    arcade.start_render()
    score = 0
    
    #does random subtraction problems (1 digit only)
    if current_screen == "menu":
        arcade.set_background_color(arcade.color.PINK_PEARL)
        arcade.draw_text("WELCOME TO D DUCKY RACE!\nPress Any Key to Start!", 100, 300, arcade.color.BLACK, 30)
    if current_screen == "high_score":
        arcade.draw_text(str(high_score), WIDTH / 2, HEIGHT / 2, arcade.color.GUPPIE_GREEN, 80)
    if current_screen == "start":
        arcade.set_background_color(arcade.color.LIGHT_BLUE)
        arcade.draw_text(str(elapsed_time), WIDTH / 2, HEIGHT / 2, arcade.color.GUPPIE_GREEN, 25)
    
        #for i in range(300, 5000, random.randint(1000, 7000)):
        draw_person(person_x)
        person_x -= 10

        counter += 1
        if 10<=counter<40:
            if first_int > second_int:
                difference = first_int-second_int
                arcade.draw_text(str(first_int)+"-"+str(second_int), 300, 400, arcade.color.BLACK, 25)
            if second_int > first_int:
                difference = second_int-first_int
                arcade.draw_text(str(second_int)+"-"+str(first_int), 300, 400, arcade.color.BLACK, 25)
        if counter == 60:
            counter = 0
            first_int = random.randint(1, 9)
            second_int = random.randint(1, 9)
        
        #makes the duck jump
        draw_duck(duck_x, duck_y)
        if jump == True and duck_x <= 105: 
            duck_x += 3
            duck_y = -1.3/24*(duck_x-65)**2 + 150
        elif duck_x > 105:
            while duck_x>25:
                duck_x-=1
                duck_y = 50
            jump = False      
    
    if current_screen == "died":
        arcade.set_background_color(arcade.color.BLACK)

        dead_emoji = arcade.load_texture("Dead emoji.jpg")
        arcade.draw_texture_rectangle(300, 370, 200, 100, dead_emoji, 0)

        arcade.draw_text("You have died.\nYour final score is "+str(score), 100, 200, arcade.color.WHITE, 50)

        arcade.draw_rectangle_filled(300, 130, 150, 100, arcade.color.PINK_LAVENDER)
        arcade.draw_text("PLAY AGAIN", 255, 123, arcade.color.BLACK, 15)


    



def on_key_press(key, modifiers):
    global jump, difference, current_screen, timing

    if current_screen == "menu":
        if key == arcade.key.SPACE:
            current_screen = "start"
        if key == arcade.key.H:
            current_screen = "high_score"
        if current_screen == "high_score":
            f = open("high_score", "r")
            high_score = f.read()
            f.close()
            if key == arcade.key.ESCAPE:
                current_screen = "menu"

    if current_screen == "start":
        if difference == 0 and key == arcade.key.KEY_0:
            jump = True
        if difference == 1 and key == arcade.key.KEY_1:
            jump = True
        if difference == 2 and key == arcade.key.KEY_2:
            jump = True
        if difference == 3 and key == arcade.key.KEY_3:
            jump = True
        if difference == 4 and key == arcade.key.KEY_4:
            jump = Trues
        if difference == 5 and key == arcade.key.KEY_5:
            jump = True
        if difference == 6 and key == arcade.key.KEY_6:
            jump = True
        if difference == 7 and key == arcade.key.KEY_7:
            jump = True
        if difference == 8 and key == arcade.key.KEY_8:
            jump = True
        if key == arcade.key.A:
            timing = False
        if key ==arcade.key.ESCAPE:
            current_screen = "menu"
    

def on_key_release(key, modifiers):
    pass


def on_mouse_press(x, y, button, modifiers):
    global died
    if 235<x<385 and 80<y<180 and died == True:
        died = False


def setup():
    arcade.open_window(WIDTH, HEIGHT, "My Arcade Game")
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
