import pygame
import bomber_objects


def draw_to_screen(bomber, bombs, ground, enemies, screen):
    screen.fill('BLUE')
    screen.blit(bomber.get_real_image(), (bomber.x - bomber.get_real_image().get_width()/2,
                                          bomber.y - bomber.get_real_image().get_height()/2))
    for bomb in bombs:
        if not bomb.enemy:
            screen.blit(bomb.get_real_image(), (bomb.x - bomb.get_real_image().get_width() / 2,
                                                bomb.y - bomb.get_real_image().get_height() / 2))
        else:
            pygame.draw.circle(screen, 'RED', (bomb.x, bomb.y), 2)

    pygame.draw.polygon(screen, ground.color, ground.points)
    for enemy in enemies:
        screen.blit(enemy.img, (enemy.x - enemy.img.get_width() / 2,
                                enemy.y - enemy.img.get_height()))
    pygame.display.update()
