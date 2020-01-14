"""
--------------------------------------------------------------------------------------------------------------------
Name:   master.py
Purpose:    the final development of the game

Author: SJOh and LMo
Created: 
--------------------------------------------------------------------------------------------------------------------
"""
import arcade
import random

# this defines all the global variables
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

def on_update(delta_time:float):
    """updates the drawing
    
    Arguments:
        delta_time {float} -- the time elapsed
    """
    global elapsed_time, score, current_score
    #This makes the timer go up
    if timing == True:
        elapsed_time += delta_time
        elapsed_time = round(elapsed_time, 2)
    #This ensures that if there is no score present, it will add the score   
    elif timing == False:
        if score == 0:
            f = open("high_score", "w+")
            f.write(str(elapsed_time))
            f.close()
            f = open("high_score", "r+")
            if f.mode == "r+":
                score = f.read()
                current_score = score
                f.close()
        #This will replace the current high score if the score is higher. 
        if elapsed_time > float(score):
            f = open("high_score", "w+")
            f.write(str(elapsed_time))
            f.close()
            f = open("high_score", "r+")
            if f.mode == "r+":
                score = f.read()
                f.close()
            



def draw_duck(x:int, y:int):
    """draws the duck
    
    Arguments:
        x {int} -- the x value of the duck
        y {int} -- the y value of the duck
    """
    #This draws the duck
    arcade.draw_circle_filled(x, y, 25, arcade.color.YELLOW)
    arcade.draw_circle_filled(x+10, y+38, 15, arcade.color.YELLOW)
    arcade.draw_triangle_filled(x+24, y+40, x+24, y+35, x+30, y+37.5, arcade.color.DARK_RED)
    arcade.draw_circle_filled(x+15, y+45, 3, arcade.color.BLACK)
    arcade.draw_rectangle_filled(x-10,y-32, 3, 15, arcade.color.BROWN)
    arcade.draw_rectangle_filled(x+10,y-32, 3, 15, arcade.color.BROWN)

def draw_person(x:int, y:int):
    """draws the first person
    
    Arguments:
        x {int} -- the x value difference in the original position of the human
        y {int} -- the y value differece in the original position of the human
    """
    #This draws the first person
    arcade.draw_rectangle_filled(1210-x, 50-y, 3, 30, arcade.color.BLACK)
    arcade.draw_circle_filled(1210-x, 70-y, 15, arcade.color.BLACK)
    arcade.draw_rectangle_filled(1210-x, 50-y, 40, 3, arcade.color.BLACK)
    arcade.draw_rectangle_filled(1200-x, 25-y, 30, 3, arcade.color.BLACK, 50)
    arcade.draw_rectangle_filled(1220-x, 25-y, 30, 3, arcade.color.BLACK, 140)

def draw_person2(x:int, y:int):
    """draws the second person
    
    Arguments:
        x {int} -- the x value difference in the original position of the human
        y {int} -- the y value differece in the original position of the human
    """
    #This draws the second person
    arcade.draw_rectangle_filled(1010-x, 50-y, 3, 30, arcade.color.BLACK)
    arcade.draw_circle_filled(1010-x, 70-y, 15, arcade.color.BLACK)
    arcade.draw_rectangle_filled(1010-x, 50-y, 40, 3, arcade.color.BLACK)
    arcade.draw_rectangle_filled(1000-x, 25-y, 30, 3, arcade.color.BLACK, 50)
    arcade.draw_rectangle_filled(1020-x, 25-y, 30, 3, arcade.color.BLACK, 140)

def draw_person3(x:int, y:int):
    """draws the third person
    
    Arguments:
        x {int} -- the x value difference in the original position of the human
        y {int} -- the y value differece in the original position of the human
    """
    #This draws the third person
    arcade.draw_rectangle_filled(810-x, 50-y, 3, 30, arcade.color.BLACK)
    arcade.draw_circle_filled(810-x, 70-y, 15, arcade.color.BLACK)
    arcade.draw_rectangle_filled(810-x, 50-y, 40, 3, arcade.color.BLACK)
    arcade.draw_rectangle_filled(800-x, 25-y, 30, 3, arcade.color.BLACK, 50)
    arcade.draw_rectangle_filled(820-x, 25-y, 30, 3, arcade.color.BLACK, 140)

def people_draw():
    """the animation of the people
    """
    global person_x, person_y, person2_x, person2_y, person3_x, person3_y
    #This ensures that the first person will be drawn and move to the left
    if person_x < 1200:
        person_x += 20
        draw_person(person_x, person_y)
    #This ensures that the second person will be drawn and move to the left
    if person2_x < 1000:
        person2_x += 20
        draw_person2(person2_x, person2_y)
    #This ensures that the third person will be drawn and move to the left
    if person3_x < 800:
        person3_x += 20
        draw_person3(person3_x, person3_y)
    #This ensures that the first person will reset it's location once it reaches the end of the screen    
    if person_x >= 1200:
        person_x = 400
        draw_person(person_x, person_y)
    #This ensures that the second person will reset it's location once it reaches the end of the screen
    if person2_x >= 1000:
        person2_x = 400
        draw_person2(person2_x, person2_y)
    #This ensures that the third person will reset it's location once it reaches the end of the screen
    if person3_x > 800:
        person3_x = 400
        draw_person3(person3_x, person3_y)

def on_draw():
    """the main function where everything is drawn
    """
    global duck_x, duck_y, current_screen, counter, first_int, second_int, jump, difference, person_x, person_y, person2_x, person2_y, person3_x, person3_y, timing, x
    arcade.start_render()
    #draws the text, resets timing, changes the background color to pink and draws the green rectangle in the menu
    if current_screen == "menu":
        timing = False
        arcade.set_background_color(arcade.color.PINK_PEARL)
        arcade.draw_text("WELCOME TO D DUCKY RACE!", 100, 320, arcade.color.BLACK, 30)
        arcade.draw_text("Press space to play", 100, 270, arcade.color.BLACK, 30)
        arcade.draw_text("Click H for high score", 100, 100, arcade.color.BLACK, 30)
        arcade.draw_text("Click I for instructions", 100, 140, arcade.color.BLACK, 30)
        arcade.draw_text("Press esc to return to menu", 100, 60, arcade.color.BLACK, 30)
        for num in range(10):
            x += 8
            arcade.draw_rectangle_filled(0, 225, 1 - x, 60, arcade.color.GREEN)
    #draws the high score in the high score screen
    if current_screen == "high_score":
        arcade.draw_text(str(high_score), 240, 200, arcade.color.GUPPIE_GREEN, 80)
    #draws the instruction screen
    if current_screen == "instructions":
        arcade.draw_text("click the right difference to jump ", 50, 320, arcade.color.BLACK, 30)
        arcade.draw_text("for example...", 50, 280, arcade.color.BLACK, 30)
        arcade.draw_text("9 - 7 = 2", 70, 220, arcade.color.BLACK, 30)
        arcade.draw_text("click 2 to jump", 70, 160, arcade.color.BLACK, 30)
        arcade.draw_text("to float, press difference repeatedly ", 50, 120, arcade.color.BLACK, 30) 

    #sets the background color to light blue, draws the people and timer
    if current_screen == "start":
        arcade.set_background_color(arcade.color.LIGHT_BLUE)
        arcade.draw_text(str(elapsed_time), WIDTH / 2, HEIGHT / 2, arcade.color.GUPPIE_GREEN, 25)

        people_draw()
        #does random subtraction problems (1 digit only)
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
            people_draw()
        if (duck_x-25<1010-person2_x<duck_x+25 and duck_y-25<70-person2_y<duck_y+25) or (duck_x-5<1010-person2_x<duck_x+25 and duck_y+13<70-person_y<duck_y+43):
            current_screen = "died"
            timing = False
            people_draw()
        if (duck_x-25<810-person3_x<duck_x+25 and duck_y-25<70-person3_y<duck_y+25) or (duck_x-5<8510-person3_x<duck_x+25 and duck_y+13<70-person3_y<duck_y+43):
            current_screen = "died"
            timing = False
            people_draw()  

        
    #draws the dead emoji and the text when the current screen is died
    if current_screen == "died":
        arcade.set_background_color(arcade.color.BLACK)

        dead_emoji = arcade.load_texture("Dead emoji.jpg")
        arcade.draw_texture_rectangle(300, 370, 200, 100, dead_emoji, 0)

        arcade.draw_text("You have died.\nYour final score is "+str(elapsed_time), 50, 200, arcade.color.WHITE, 40)

        arcade.draw_rectangle_filled(300, 130, 150, 100, arcade.color.PINK_LAVENDER)
        arcade.draw_text("PLAY AGAIN", 255, 123, arcade.color.BLACK, 15)

def on_key_press(key, modifiers):
    """what happens if a certain key is pressed at a certain time
    
    Arguments:
        key {key} -- the key being pressed
        modifiers {} -- [description]
    """
    global jump, difference, current_screen, timing, high_score, elapsed_time
    if current_screen == "menu":
    #pressing space will switch the screen to "start" and also resets elapsed_time and timing
        if key == arcade.key.SPACE:
            current_screen = "start"
            elapsed_time = 0
            timing = True
    #pressing H will switch the screen to high score and opens the high score file
        if key == arcade.key.H:
            current_screen = "high_score"
            f = open("high_score", "r")
            high_score = f.read()
            f.close()
    #pressing I will switch to the instruction screen
        if key == arcade.key.I:
            current_screen = "instructions"
    #pressing escape will make the current screen menu
    if key == arcade.key.ESCAPE:
        current_screen = "menu"
    #this ensures that the duck will jump if the correct difference is clicked 
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

def on_key_release(key, modifiers):
    pass


def on_mouse_press(x:float, y:float, button, modifiers):
    """what happens if the mouse is pressed
    
    Arguments:
        x {float} -- the x value of the mouse press
        y {float} -- the y value of the mouse press
        button {int} -- the button
        modifiers {[type]} -- [description]
    """
    global current_screen, timing
    #this ensures that if the user clicks "play again", it will make the current screen menu and set timing to True
    if 235<x<385 and 80<y<180 and current_screen == "died":
        current_screen = "menu"
        timing = True


def setup():
    """the setup of the code
    """
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