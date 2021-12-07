import pygame
import bomber_objects





def draw_to_screen(bomber, bombs, ground, enemies, screen):
    screen.fill('BLUE')
    pygame.draw.circle(screen, 'WHITE', (bomber.x, bomber.y), 10)
    for bomb in bombs:
        pygame.draw.circle(screen, 'RED', (bomb.x, bomb.y), 3)
    pygame.draw.polygon(screen, ground.color, ground.points)
    for enemy in enemies:
        pygame.draw.circle(screen, 'BLACK', (enemy.x, enemy.y), 10)
    pygame.display.update()
