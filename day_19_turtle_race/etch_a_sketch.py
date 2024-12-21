from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

pace = 10

def move_forwards():
    tim.forward(pace)

def move_backwards():
    tim.backward(pace)

def move_left():
    tim.left(pace)

def move_right():
    tim.right(pace)

def move_left2():
    new_heading = tim.heading() + pace
    tim.setheading(new_heading)

def move_right2():
    new_heading = tim.heading() - pace
    tim.setheading(new_heading)

def reset_drawing():
    tim.reset()

# W = forwards
# S = backwards
# A = counter clockwise (right)
# D = clockwise (left)
# C = clear drawing & re-center turtle

screen.listen()

screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=move_left2)
screen.onkey(key="d", fun=move_right2)
screen.onkey(key="c", fun=reset_drawing)

screen.exitonclick()
