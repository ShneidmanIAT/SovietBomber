import pygame
import bomber_objects


def draw_to_screen(bomber, bombs, ground, enemies, screen):
    screen.fill('BLUE')
    screen.blit(bomber.get_real_image(), (bomber.x - bomber.get_real_image().get_width()/2, bomber.y - bomber.get_real_image().get_height()/2))
    for bomb in bombs:
        pygame.draw.circle(screen, 'RED', (bomb.x, bomb.y), 3)
    pygame.draw.polygon(screen, ground.color, ground.points)
    for enemy in enemies:
        pygame.draw.circle(screen, 'BLACK', (enemy.x, enemy.y), 10)
    pygame.display.update()
