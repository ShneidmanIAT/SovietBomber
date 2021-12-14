import pygame
import bomber_objects


def draw_objects_to_screen(bomber, bombs, ground, enemies, screen):
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



def draw_text_to_screen(screen, health, score, lost, timer):
    pygame.font.init()
    myfont = pygame.font.SysFont('Comic Sans MS', 30)
    scoresurf = myfont.render('Score:' + str(score), False, (0, 0, 0))
    screen.blit(scoresurf, (0, 0))
    healthsurf = myfont.render('HEALTH:' + str(health), False, 'RED')
    screen.blit(healthsurf, (screen.get_width() - 200, 0))
    if not lost and timer < 99:
        endlevelsurf = myfont.render('Well done!', False, (0, 0, 0))
        screen.blit(endlevelsurf, (screen.get_width()/2 - 50, screen.get_height()/2 - 50))
    if lost:
        deathsurf = myfont.render('You died', False, (0, 0, 0))
        screen.blit(deathsurf, (screen.get_width()/2 - 50, screen.get_height()/2 - 50))