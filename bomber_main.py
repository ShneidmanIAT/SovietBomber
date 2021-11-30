
import pygame
from bomber_objects import Plane, Ground
from bomber_rendering import *


FPS = 30
WIDTH = 800
HEIGHT = 800


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
bomber = Plane()
bomber.y = 100
bomber.x = 100
bombs = []
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
    draw_to_screen()
pygame.quit()
