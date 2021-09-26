import time
from turtle import Screen
import car_manager
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.up, "w")

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    car = CarManager()
    car.create_car()
    car.move()

screen.exitonclick()
