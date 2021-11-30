import pygame
from bomber_objects import *
from bomber_main import *

WIDTH = 800
HEIGHT = 800

screen = pygame.display.set_mode((WIDTH, HEIGHT))


def draw_to_screen():
    screen.fill('BLUE')
    pygame.draw.circle(screen, 'WHITE', (bomber.x, bomber.y), 10)
    pygame.display.update()
