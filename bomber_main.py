import random

import pygame
from bomber_objects import Plane, Ground, Bomb, Tank
import bomber_rendering
import bomber_physics
import bomber_menu


FPS = 30
WIDTH = 600
HEIGHT = 600
GROUND_NUMOFPOINTS = 40


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
bomber = Plane()
bomber.y = 100
bomber.x = 100
bombs = []
enemies = []
ground = Ground()
ground.points.append([0, screen.get_height()])
print(ground.points)
for i in range(GROUND_NUMOFPOINTS):
    ground.points.append([screen.get_width()*i/(GROUND_NUMOFPOINTS - 1), 600 - random.randint(75, 100)])
ground.points.append([screen.get_width(), screen.get_height()])
print(ground.points)
clock = pygame.time.Clock()
finished = False
hardness = 3
for i in range(hardness):
    pos = random.randint(3, GROUND_NUMOFPOINTS - 3)
    newTank = Tank(ground.points[pos][0], ground.points[pos][1])
    enemies.append(newTank)
bomber_menu.show_menu()
pygame.mixer.music.load('bombersong.mp3')
pygame.mixer.music.play(-1)
while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONUP:
            newbomb = Bomb(bomber.x, bomber.y, bomber.vx, bomber.vy)
            bombs.append(newbomb)
        elif event.type == pygame.MOUSEMOTION:
            bomber.speed_recalculation(event)
    bomber_rendering.draw_to_screen(bomber, bombs, ground, enemies, screen)
    bomber_physics.flight(bomber, bombs)
    bombs, ground = bomber_physics.bombcheck(bombs, ground)
    bombs, enemies = bomber_physics.enemy_move(enemies, ground, bombs, bomber)
    for enemy in enemies:
        if enemy.cd < 0:
            bombs.append(enemy.fire(bomber))
            enemy.cd = enemy.reloading_time
        else:
            enemy.cd -= 1
pygame.quit()
