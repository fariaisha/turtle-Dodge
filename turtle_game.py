import turtle
import random
import time
import os

# --- 1. File Handling for High Score ---
HIGH_SCORE_FILE = "highscore.txt"

def get_high_score():
    if os.path.exists(HIGH_SCORE_FILE):
        with open(HIGH_SCORE_FILE, "r") as file:
            try:
                return int(file.read().strip())
            except ValueError:
                return 0
    return 0

def save_high_score(new_high):
    with open(HIGH_SCORE_FILE, "w") as file:
        file.write(str(new_high))

# --- 2. Game Setup ---
screen = turtle.Screen()
screen.title("Ultimate Turtle Dodge")
screen.bgcolor("skyblue")
screen.setup(width=600, height=600)
screen.tracer(0)

# --- 3. Game State Variables ---
score = 0
high_score = get_high_score()
level = 1
enemy_speed = 15     # Starting speed of falling objects
spawn_rate = 12       # Lower means more frequent spawns
enemies = []
game_state = "START"  # Status tracking: START, PLAYING, GAME_OVER

# --- 4. Game Objects ---
player = turtle.Turtle()
player.shape("turtle")
player.color("green")
player.penup()
player.goto(0, -250)
player.hideturtle()  # Hide until game starts

# UI Text Drawer
ui = turtle.Turtle()
ui.hideturtle()
ui.penup()
ui.color("black")

# --- 5. Movement Logic ---
def move_left():
    if game_state == "PLAYING":
        x = player.xcor()
        if x > -280:
            player.setx(x - 25)

def move_right():
    if game_state == "PLAYING":
        x = player.xcor()
        if x < 280:
            player.setx(x + 25)

def start_game():
    global game_state
    if game_state == "START" or game_state == "GAME_OVER":
        reset_game()
        game_state = "PLAYING"

# --- 6. Controls ---
screen.listen()
screen.onkey(move_left, "Left")
screen.onkey(move_right, "Right")
screen.onkey(start_game, "space")

# --- 7. Screen Render Functions ---
def draw_ui():
    ui.clear()
    if game_state == "START":
        ui.goto(0, 80)
        ui.write("TURTLE DODGE", align="center", font=("Courier", 32, "bold"))
        ui.goto(0, 0)
        ui.write("Avoid the falling red meteors!", align="center", font=("Courier", 14, "italic"))
        ui.goto(0, -80)
        ui.write("Press [SPACEBAR] to Start", align="center", font=("Courier", 16, "bold"))
        ui.goto(0, -150)
        ui.write(f"Current High Score: {high_score}", align="center", font=("Courier", 12, "normal"))
        
    elif game_state == "PLAYING":
        # Live scoreboard top left
        ui.goto(-280, 260)
        ui.write(f"Score: {score}  Level: {level}", align="left", font=("Courier", 14, "bold"))
        # Live high score top right
        ui.goto(280, 260)
        ui.write(f"High Score: {high_score}", align="right", font=("Courier", 14, "bold"))
        
    elif game_state == "GAME_OVER":
        ui.goto(0, 50)
        ui.write("GAME OVER", align="center", font=("Courier", 36, "bold"))
        ui.goto(0, -10)
        ui.write(f"Your Score: {score}", align="center", font=("Courier", 18, "normal"))
        ui.goto(0, -70)
        ui.write("Press [SPACEBAR] to Play Again", align="center", font=("Courier", 14, "bold"))

def reset_game():
    global score, level, enemy_speed, spawn_rate, enemies
    score = 0
    level = 1
    enemy_speed = 15
    spawn_rate = 12
    # Clear out any old enemies left on screen
    for enemy in enemies:
        enemy.hideturtle()
    enemies.clear()
    player.goto(0, -250)
    player.showturtle()

# --- 8. Core Loop Logic ---
while True:
    time.sleep(0.05)  # Controls frame update interval
    draw_ui()
    
    if game_state == "PLAYING":
        # 1. Procedural Difficulty Spawning
        if random.randint(1, spawn_rate) == 1:
            enemy = turtle.Turtle()
            enemy.shape("circle")
            enemy.color("red")
            enemy.penup()
            enemy.goto(random.randint(-280, 280), 280)
            enemies.append(enemy)

        # 2. Update and check enemies
        for enemy in list(enemies):  # Safe list iterating
            enemy.sety(enemy.ycor() - enemy_speed)

            # Hitbox registration
            if enemy.distance(player) < 22:
                game_state = "GAME_OVER"
                player.hideturtle()
                if score > high_score:
                    high_score = score
                    save_high_score(high_score)

            # Score clearing & Difficulty scaling
            if enemy.ycor() < -300:
                enemy.hideturtle()
                if enemy in enemies:
                    enemies.remove(enemy)
                score += 1
                
                # Advance level and scale mechanics every 10 points
                if score % 10 == 0:
                    level += 1
                    enemy_speed += 3      # Falling acceleration
                    if spawn_rate > 4:
                        spawn_rate -= 1    # Increased object frequency

    screen.update()
