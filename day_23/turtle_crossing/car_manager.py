from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager:
    
    def __init__(self):
        self.cars = []
        self.speed = STARTING_MOVE_DISTANCE

    def move(self):
        for car in self.cars:
            #car.goto(car.xcor() - self.speed, car.ycor())
            car.backwards(self.speed)

    def speed_up(self):
        self.speed += MOVE_INCREMENT

    def add_car(self):
        random_chance = random.randint(1,6) # 1/6 chance of a new car
        if random_chance == 1:
            new_car = Turtle()
            new_car.penup()
            new_car.shape("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.color(random.choice(COLORS))            # random color
            new_car.goto((300,random.randint(-250,250)))    # random location
            self.cars.append(new_car)