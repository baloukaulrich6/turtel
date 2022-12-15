import random
from turtle import *

tinny_the_turtel = Turtle()
colormode(255)


# def draw_shape(run_side):
#     angle = 360 / run_side
#     for _ in range(run_side):
#         tinny_the_turtel.forward(100)
#         tinny_the_turtel.right(angle)
# for shape_side_n in range(3, 11):
#     draw_shape(shape_side_n )
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color

# direction = [0, 90, 180, 270]
# tinny_the_turtel.pensize(15)
tinny_the_turtel.speed("fastest")
def draw_spirograph(size_of_gap):
    for _ in range(int(360/size_of_gap)):
        tinny_the_turtel.color(random_color())
        tinny_the_turtel.circle(100)
        tinny_the_turtel.setheading(tinny_the_turtel.heading() + 10)

draw_spirograph(5)

# for _ in range(280):
#     tinny_the_turtel.color(random_color())
#     tinny_the_turtel.forward(30)
#     tinny_the_turtel.setheading(random.choice(direction))

# les coin de chaque pentagone on 72 degre
# for _ in range(15):
#     tinny_the_turtel.forward(10)
#     tinny_the_turtel.penup()
#     tinny_the_turtel.forward(10)
#     tinny_the_turtel.pendown()

screen = Screen()
screen.exitonclick()