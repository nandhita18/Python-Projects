COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
from turtle import Turtle
import random
class CarManager():
    def __init__(self):
        self.all_cars = []
        self.speed = STARTING_MOVE_DISTANCE
      
    def create_cars(self):
        choice = random.randint(1,6)
        if choice ==1:
            car = Turtle()
            car.shape("square")
            car.penup()
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.color(random.choice(COLORS))
            random_y = random.randint(-250, 250)
            car.goto(300, random_y)
            self.all_cars.append(car)


    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.speed)

    def level_up(self):
        self.speed += MOVE_INCREMENT




