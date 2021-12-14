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
bomber = Plane()
hardness = 3
while not finished:
    timer = 100
    bombs = []
    enemies = []
    ground = Ground()
    ground.new_ground(screen.get_width(), screen.get_height(), GROUND_NUMOFPOINTS)
    clock = pygame.time.Clock()
    enemies = ground.add_enemies(hardness, GROUND_NUMOFPOINTS, enemies)
    if lost:
        bomber_menu.show_menu()
        lost = False
        bomber.score = 0
        bomber.health = 1000
        bomber.v = bomber.vstart
        bomber.y = 100
        bomber.x = 100
    endlevel = False
    pygame.mixer.music.load('bombersong.mp3')
    pygame.mixer.music.play(-1)
    while not endlevel and not finished:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True
            elif event.type == pygame.MOUSEBUTTONUP and not lost:
                newbomb = Bomb(bomber.x, bomber.y, bomber.vx, bomber.vy)
                bombs.append(newbomb)
            elif event.type == pygame.MOUSEMOTION and not lost:
                bomber.speed_recalculation(event)
        bomber_rendering.draw_objects_to_screen(bomber, bombs, ground, enemies, screen)
        bomber_physics.flight(bomber, bombs)
        bombs, ground = bomber_physics.bombcheck(bombs, ground)
        bombs, enemies, bomber = bomber_physics.killcheck(enemies, ground, bombs, bomber)
        bomber_rendering.draw_text_to_screen(screen, bomber.health, bomber.score, lost, timer)
        pygame.display.update()
        for enemy in enemies:
            if enemy.cd < 0:
                bombs.append(enemy.fire(bomber))
                enemy.cd = enemy.reloading_time
            else:
                enemy.cd -= 1
        if len(enemies) == 0 or lost:
            timer -= 1
            if timer == 0:
                endlevel = True
                hardness += 2
        if bomber.health < 0:
            bomber.v = 0
            lost = True


pygame.quit()
