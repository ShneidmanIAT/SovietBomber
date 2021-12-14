import random

import pygame
from bomber_objects import Plane, Ground, Bomb, Tank
import bomber_rendering
import bomber_physics
import bomber_menu


FPS = 30
WIDTH = 900
HEIGHT = 476
GROUND_NUMOFPOINTS = 40


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
lost = True
finished = False
endlevel = False
while not finished:
    timer = 100
    bomber = Plane()
    bomber.y = 100
    bomber.x = 100
    bombs = []
    enemies = []
    ground = Ground()
    ground.new_ground(screen.get_width(), screen.get_height(), GROUND_NUMOFPOINTS)
    clock = pygame.time.Clock()
    hardness = 3
    enemies = ground.add_enemies(hardness, GROUND_NUMOFPOINTS, enemies)
    if lost:
        bomber_menu.show_menu()
        lost = False
    endlevel = False
    pygame.mixer.music.load('bombersong.mp3')
    pygame.mixer.music.play(-1)
    while not endlevel and not finished:
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
        if len(enemies) == 0:
            timer -= 1
            if timer == 0:
                endlevel = True

pygame.quit()
