#===============================================================================
# DAY 19: Turtle Race
#===============================================================================
import random
from turtle import Turtle, Screen

NUM_RACERS = 10
COLORS = [
    "red",
    "orange",
    "yellow",
    "green",
    "blue",
    "indigo",
    "violet"
]
MAX_X = 300
MIN_X = -300
Y_SPACING = 30
MAX_Y = (NUM_RACERS // 2) * Y_SPACING
MIN_Y = -MAX_Y
MAX_RUN_DIST = 10


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


# Main
mscn = Screen()
mscn.title("TURTLE RACE TODAY!!!")
mscn.setup(width=800, height=600)
mscn.bgcolor("black")

y = MAX_Y
racers = []
r = 1
for i in range(NUM_RACERS):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(get_random_color())
    new_turtle.speed("fast")
    new_turtle.goto(x=MIN_X-10, y=y)
    new_turtle.clear()
    new_turtle.write(r, move=True, align="left")
    new_turtle.forward(10)
    racers.append(new_turtle)
    y -= Y_SPACING
    r += 1

user_bet = 10000
while user_bet == 10000:
    try:
        input_str = "Select turtle number (1 - Top; %s - Bottom) :" % (NUM_RACERS)
        user_bet = int(mscn.textinput("Place your bet!", input_str))
        if user_bet > NUM_RACERS or user_bet < 1:
            user_bet = 10000
    except:
        user_bet = 10000

is_race_on = True

while is_race_on:
    try:
        r = 1
        for racer in racers:
            run_dist = random.randint(1, MAX_RUN_DIST)
            racer.forward(run_dist)
            racer_x = racer.xcor()
            if racer_x >= MAX_X:
                if r == user_bet:
                    racer.write("Winner!", move=True)
                else:
                    racer.write("You lose! :P", move=True)
                is_race_on = False
                break
            r += 1
    except:
        is_race_on = False

# Loop until window gets closed
mscn.mainloop()
