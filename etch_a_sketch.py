#===============================================================================
# Etch-a-Sketch using Turtle class
# Author: Michael Sumaya
#===============================================================================
# Controls:
# 'w' = Forward
# 's' = Backward
# 'a' = Counter-Clockwise
# 'd' = Clockwise
# 'c' = Reset position and clear screen
#===============================================================================
import random
from turtle import Turtle

# BINDINGS
KEY_FORWARD = "w"
KEY_BACKWARD = "s"
KEY_LEFT = "a"
KEY_RIGHT = "d"
KEY_CLEAR = "c"
DISTANCE = 10
ANGLE = 5


# Functions
def rgb_to_hex(red, green, blue):
    return '#{:02X}{:02X}{:02X}'.format(red, green, blue)


def get_random_color():
    COLOR_MAX = 255
    random_color = rgb_to_hex(
        random.randint(0, COLOR_MAX),
        random.randint(0, COLOR_MAX),
        random.randint(0, COLOR_MAX)
    )
    return random_color


def forward():
    turt.color(get_random_color())
    turt.forward(DISTANCE)


def backward():
    turt.color(get_random_color())
    turt.back(DISTANCE)


def counter_clockwise():
    turt.color(get_random_color())
    turt.left(ANGLE)


def clockwise():
    turt.color(get_random_color())
    turt.right(ANGLE)


def clear():
    turt.home()
    turt.setheading(0)
    turt.clear()


random.seed()

# Setup Turtle and Screen
turt = Turtle()
turt.speed("fastest")
scr = turt.getscreen()
scr.title(titlestring="My Turtle Painter")

# Main
scr.listen()
scr.onkeypress(key=KEY_FORWARD, fun=forward)
scr.onkeypress(key=KEY_BACKWARD, fun=backward)
scr.onkeypress(key=KEY_LEFT, fun=counter_clockwise)
scr.onkeypress(key=KEY_RIGHT, fun=clockwise)
scr.onkeypress(key=KEY_CLEAR, fun=clear)

# End of code
scr.mainloop()
