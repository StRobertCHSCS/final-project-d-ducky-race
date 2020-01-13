"""
--------------------------------------------------------------------------------------------------------------------
Name:   member1_development.py
Purpose:    the development of the first member
Author: LMo
Created: 
--------------------------------------------------------------------------------------------------------------------
"""
import arcade
import random

WIDTH = 640
HEIGHT = 480

duck_x = 280
duck_y = 48
jump = False
current_screen = "menu"
difference = 0
counter = 0
first_int = random.randint(1, 9)
second_int = random.randint(1, 9)
elapsed_time = 0
timing  = True
score = 0
high_score = 0
person_x = 0
person_y = 0
person2_x = 0
person2_y = 0
person3_x = 0
person3_y = 0
x = 0

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
        if elapsed_time > float(score):
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

def draw_person(x, y):
    arcade.draw_rectangle_filled(1210-x, 50-y, 3, 30, arcade.color.BLACK)
    arcade.draw_circle_filled(1210-x, 70-y, 15, arcade.color.BLACK)
    arcade.draw_rectangle_filled(1210-x, 50-y, 40, 3, arcade.color.BLACK)
    arcade.draw_rectangle_filled(1200-x, 25-y, 30, 3, arcade.color.BLACK, 50)
    arcade.draw_rectangle_filled(1220-x, 25-y, 30, 3, arcade.color.BLACK, 140)

def draw_person2(x, y):
    arcade.draw_rectangle_filled(1010-x, 50-y, 3, 30, arcade.color.BLACK)
    arcade.draw_circle_filled(1010-x, 70-y, 15, arcade.color.BLACK)
    arcade.draw_rectangle_filled(1010-x, 50-y, 40, 3, arcade.color.BLACK)
    arcade.draw_rectangle_filled(1000-x, 25-y, 30, 3, arcade.color.BLACK, 50)
    arcade.draw_rectangle_filled(1020-x, 25-y, 30, 3, arcade.color.BLACK, 140)

def draw_person3(x, y):
    arcade.draw_rectangle_filled(810-x, 50-y, 3, 30, arcade.color.BLACK)
    arcade.draw_circle_filled(810-x, 70-y, 15, arcade.color.BLACK)
    arcade.draw_rectangle_filled(810-x, 50-y, 40, 3, arcade.color.BLACK)
    arcade.draw_rectangle_filled(800-x, 25-y, 30, 3, arcade.color.BLACK, 50)
    arcade.draw_rectangle_filled(820-x, 25-y, 30, 3, arcade.color.BLACK, 140)

def on_draw(): 
    global duck_x, duck_y, current_screen, counter, first_int, second_int, jump, difference, person_x, person_y, person2_x, person2_y, person3_x, person3_y, timing, x
    arcade.start_render()
    #does random subtraction problems (1 digit only)
    if current_screen == "menu":
        arcade.set_background_color(arcade.color.PINK_PEARL)
        arcade.draw_text("WELCOME TO D DUCKY RACE!\nPress Any Key to Start!", 100, 300, arcade.color.BLACK, 30)
        arcade.draw_text("Click H for high score", 100, 100, arcade.color.BLACK, 30)
        for num in range(10):
            x += 8
            arcade.draw_rectangle_filled(0, 225, 1 - x, 60, arcade.color.GREEN)
    if current_screen == "high_score":
        arcade.draw_text(str(high_score), WIDTH / 2, HEIGHT / 2, arcade.color.GUPPIE_GREEN, 80)
    if current_screen == "start":
        arcade.set_background_color(arcade.color.LIGHT_BLUE)
        arcade.draw_text(str(elapsed_time), WIDTH / 2, HEIGHT / 2, arcade.color.GUPPIE_GREEN, 25)

        if person_x < 1200:
            person_x += 20
            draw_person(person_x, person_y)
        if person2_x < 1000:
            person2_x += 20
            draw_person2(person2_x, person2_y)
        if person3_x < 800:
            person3_x += 20
            draw_person3(person3_x, person3_y)
        if person_x >= 1200:
            person_x = 400
            draw_person(person_x, person_y)
        if person2_x >= 1000:
            person2_x = 400
            draw_person2(person2_x, person2_y)
        if person3_x > 800:
            person3_x = 400
            draw_person3(person3_x, person3_y)

        counter += 1
        if 10<=counter<40:
            if first_int > second_int:
                difference = first_int-second_int
                arcade.draw_text(str(first_int)+"-"+str(second_int), 300, 400, arcade.color.BLACK, 25)
            if second_int > first_int:
                difference = second_int-first_int
                arcade.draw_text(str(second_int)+"-"+str(first_int), 300, 400, arcade.color.BLACK, 25)
        if counter == 40:
            counter = 0
            first_int = random.randint(1, 9)
            second_int = random.randint(1, 9)
        
        #makes the duck jump
        draw_duck(duck_x, duck_y)
        if jump == True and duck_y < 192: 
            duck_y += 24

        if jump == True and duck_y >= 192:      
            jump = False
            duck_y -= 24
        
        if jump == False and duck_y > 48:
            duck_y -= 24

        #collision detection
        if (duck_x-25<1210-person_x<duck_x+25 and duck_y-25<70-person_y<duck_y+25) or (duck_x-5<1210-person_x<duck_x+25 and duck_y+13<70-person_y<duck_y+43):
            current_screen = "died"
            timing = False
        if (duck_x-25<1010-person2_x<duck_x+25 and duck_y-25<70-person2_y<duck_y+25) or (duck_x-5<1010-person2_x<duck_x+25 and duck_y+13<70-person_y<duck_y+43):
            current_screen = "died"
            timing = False
        if (duck_x-25<810-person3_x<duck_x+25 and duck_y-25<70-person3_y<duck_y+25) or (duck_x-5<8510-person3_x<duck_x+25 and duck_y+13<70-person3_y<duck_y+43):
            current_screen = "died"
            timing = False
        

        

    if current_screen == "died":
        arcade.set_background_color(arcade.color.BLACK)

        dead_emoji = arcade.load_texture("Dead emoji.jpg")
        arcade.draw_texture_rectangle(300, 370, 200, 100, dead_emoji, 0)

        arcade.draw_text("You have died.\nYour final score is "+str(score), 50, 200, arcade.color.WHITE, 50)

        arcade.draw_rectangle_filled(300, 130, 150, 100, arcade.color.PINK_LAVENDER)
        arcade.draw_text("PLAY AGAIN", 255, 123, arcade.color.BLACK, 15)

def on_key_press(key, modifiers):
    global jump, difference, current_screen, timing, high_score, elapsed_time

    if current_screen == "menu":       
        if key == arcade.key.SPACE:
            current_screen = "start"
            elapsed_time = 0
            timing = True
        if key == arcade.key.H:
            current_screen = "high_score"
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
            jump = True
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
    global current_screen, timing
    if 235<x<385 and 80<y<180 and current_screen == "died":
        current_screen = "menu"
        timing = True


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
