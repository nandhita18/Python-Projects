import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)


#move turtle
player= Player()
def move():
    player.forward(10)
screen.listen()
screen.onkey(key="Up", fun= move)

#cars
car_manager = CarManager()
scoreboard = Scoreboard()


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_cars()
    car_manager. move_cars()
    # detect collision
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    #detect finishing
    if player.is_on_finish_line():
       player.starting_point()
       car_manager.level_up()
       scoreboard.increase_level()


screen.exitonclick()
