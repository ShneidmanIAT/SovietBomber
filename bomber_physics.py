import math
import bomber_objects


def flight(bomber, bombs):
    """starts move functions for bombs and bomber"""
    bomber.move()
    for bomb in bombs:
        bomb.move()


def bombcheck(bombs, ground):
    """checks collisions for array with bombs"""
    todel = []
    bomb_new = []
    for j in range(len(bombs)):
        ground, detonated = bombs[j].groundcheck(ground)
        if detonated:
            todel.append(j)
    for i in range(len(bombs)):
        if i in todel:
            pass
        else:
            bomb_new.append(bombs[i])
    return bomb_new, ground


def killcheck(enemies, ground, bombs, bomber):
    """checks hits"""
    todel_bombs = []
    todel_enemies = []
    enemies_new = []
    bombs_new = []
    for i in range(len(bombs)):
        detonated, bomber = bombs[i].planecheck(bomber)
        if detonated:
            todel_bombs.append(i)
    for i in range(len(enemies)):
        for j in range(len(bombs)):
            detonated, enemies[i] = bombs[j].enemycheck(enemies[i])
            if detonated:
                todel_bombs.append(j)
                bomber.score += 1
                if enemies[i].health < 0:
                    todel_enemies.append(i)
    for i in range(len(enemies)):
        if i in todel_enemies:
            pass
        else:
            enemies_new.append(enemies[i])
    for i in range(len(bombs)):
        if i in todel_bombs:
            pass
        else:
            bombs_new.append(bombs[i])
    for i in range(len(enemies_new)):
        enemies_new[i].moveforward(ground)
    return bombs_new, enemies_new, bomber