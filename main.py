import turtle
import random
import time

# Setup
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Space Invaders")
screen.setup(width=800, height=600)
screen.tracer(0)

player = turtle.Turtle()
player.shape("square")
player.color("blue")
player.penup()
player.goto(0, -250)
player_speed = 20

def move_left():
    player.setx(max(player.xcor() - player_speed, -350))

def move_right():
    player.setx(min(player.xcor() + player_speed, 350))

bullet = turtle.Turtle()
bullet.shape("triangle")
bullet.color("yellow")
bullet.penup()
bullet.hideturtle()
bullet_speed = 20
bullet_state = "ready"

def fire_bullet():
    global bullet_state
    if bullet_state == "ready":
        bullet_state = "fired"
        bullet.goto(player.xcor(), player.ycor() + 10)
        bullet.showturtle()

aliens = [turtle.Turtle() for _ in range(5)]
for alien in aliens:
    alien.shape("circle")
    alien.color("red")
    alien.penup()
    alien.goto(random.randint(-300, 300), random.randint(100, 250))

screen.listen()
screen.onkeypress(move_left, "Left")
screen.onkeypress(move_right, "Right")
screen.onkeypress(fire_bullet, "space")

running = True
while running:
    screen.update()

    if bullet_state == "fired":
        bullet.sety(bullet.ycor() + bullet_speed)
        if bullet.ycor() > 300:
            bullet.hideturtle()
            bullet_state = "ready"

    for alien in aliens:
        alien.sety(alien.ycor() - 2)
        if alien.ycor() < -300 or alien.distance(player) < 20:
            print("Game Over")
            running = False
        if bullet_state == "fired" and bullet.distance(alien) < 20:
            bullet.hideturtle()
            bullet_state = "ready"
            alien.goto(random.randint(-300, 300), random.randint(100, 250))

    time.sleep(0.02)

screen.mainloop()
