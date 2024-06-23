from main import *
from morkov import *

import random
import time


WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
BACKGROUND_COLOR = "blue"


def draw(window):
    # grass
    Rectangle(surface=window, width=800, height=100, x=0, y=500, color="green")

    # building
    Rectangle(surface=window, width=150, height=200, x=400, y=300, color="purple")

    # window
    Rectangle(surface=window, width=10, height=10, x=420, y=320, color="yellow")

    # window
    Rectangle(surface=window, width=10, height=10, x=450, y=320, color="yellow")

    # window
    Rectangle(surface=window, width=10, height=10, x=480, y=320, color="yellow")

    # window
    Rectangle(surface=window, width=10, height=10, x=510, y=320, color="yellow")


    # window
    Rectangle(surface=window, width=10, height=10, x=420, y=350, color="yellow")

    # window
    Rectangle(surface=window, width=10, height=10, x=450, y=350, color="yellow")

    # window
    Rectangle(surface=window, width=10, height=10, x=480, y=350, color="yellow")

    # window
    Rectangle(surface=window, width=10, height=10, x=510, y=350, color="yellow")

    # sun
    Circle(surface=window, center_x=800, center_y=0, radius=90, color="yellow")

    Capybara(window=window, x = 50, y = 450)

    Seal(window=window, x = 150, y = 450, width=100, height=120)
    
