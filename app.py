from main import *
from morkov import *

import random
import time


WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
BACKGROUND_COLOR = "blue"


def draw(window):
    # grass
    Rectangle(surface=window, width=80, height=10, x=0, y=0, color="green")

    # building
    Rectangle(surface=window, width=50, height=80, x=400, y=300, color="purple")

    # window
    Rectangle(surface=window, width=10, height=10, x=420, y=320, color="yellow")

    # sun
    Circle(surface=window, center_x=300, center_y=600, radius=90, color="yellow")

    Capybara(window=window, x = 0, y = 0)

    Bms(window=window, x =600, y = 0, width=110, height=130)

    Seal(window=window, x = 750, y = 450, width=100, height=120)
    
