from turtle import Screen
from player import Player
from cars import Cars
from scoreboard import ScoreBoard
import time
import random

cars_list = []

my_screen = Screen()
my_screen.setup(width=600, height=600)
my_screen.title('Turtle Crossing Game')
my_screen.colormode(255)
my_screen.tracer(0)

player = Player()
scoreboard = ScoreBoard()

my_screen.listen()
my_screen.onkey(key='Up', fun=player.move)

is_game_on = True

while is_game_on:
    time.sleep(scoreboard.move_speed)
    random_chance = random.randint(1, 10)
    if random_chance == 1:
        cars_list.append(Cars())
    my_screen.update()
    for car in cars_list:
        car.car_move()

        if player.distance(car) < 26:
            scoreboard.game_over()
            is_game_on = False

    if player.ycor() > 300:
        player.goto(x=0, y=-280)
        scoreboard.next_level()

my_screen.exitonclick()
