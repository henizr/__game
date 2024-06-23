import pygame
import app
import sys
from app import (
    WINDOW_WIDTH,
    WINDOW_HEIGHT,
    BACKGROUND_COLOR
)



FRAMES_PER_SECOND = 30


# Начальные настройки
pygame.init()
window: pygame.Surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Capy, seal and BMS")
clock = pygame.time.Clock()



class Game():
    def __init__(self) -> None:

        self.main_loop()

    def main_loop(self):
        # Main gameloop
        while True:
            # Event loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            

            window.fill(BACKGROUND_COLOR)

            app.draw(window=window)

            pygame.display.update()
            clock.tick(FRAMES_PER_SECOND)



Game()

    