#physics model for bomber
import math

import bomber_objects


def flight(bomber, bombs):
    bomber.x += bomber.vx
    bomber.y += bomber.vy
    for bomb in bombs:
        bomb.y += bomb.vy
        bomb.x += bomb.vx
        bomb.vy += 0.1


def bombcheck(bombs, ground):
    todel = []
    bomb_new = []
    for j in range(len(bombs)):
        for i in range(len(ground.points) - 1):
            if ground.points[i][0] < bombs[j].x and ground.points[i+1][0] > bombs[j].x and (ground.points[i][1] < bombs[j].y or ground.points[i + 1][1] < bombs[j].y):
                print(i)
                if ground.points[i][0] - bombs[j].x < ground.points[i + 1][0] - bombs[j].x:
                    ground.points[i][1] += 5
                else:
                    ground.points[i + 1][1] += 5
                todel.append(j)

    for i in range(len(bombs)):
        if i in todel:
            pass
        else:
            bomb_new.append(bombs[i])
    return bomb_new, ground


def enemy_move(enemies, ground, bombs):
    todel_bombs = []
    todel_enemies= []
    enemies_new = []
    bombs_new = []
    for i in range(len(enemies)):
        for j in range(len(bombs)):
            if math.hypot(bombs[j].x - enemies[i].x, bombs[j].y - enemies[i].y) < enemies[i].hitbox:
                todel_enemies.append(i)
                todel_bombs.append(j)
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
            print(enemies_new)
    for i in range(len(enemies_new)):
        if enemies[i].x >= ground.points[len(ground.points) - 1][0] - 1 and enemies[i].v > 0:
            enemies[i].v = -enemies[i].v
        if enemies[i].x <= ground.points[0][0] + 1 and enemies[i].v < 0:
            enemies[i].v = -enemies[i].v
        v_lasts = enemies_new[i].v
        flag = 0
        if enemies_new[i].v > 0:
            for j in range(len(ground.points)):
                if ground.points[j][0] > enemies_new[i].x and flag == 0:
                    k = v_lasts / math.hypot(ground.points[j][0] - enemies_new[i].x, ground.points[j][1] - enemies_new[i].y)
                    if k < 1:
                        enemies_new[i].x += (ground.points[j][0] - enemies_new[i].x) * k
                        enemies_new[i].y += (ground.points[j][1] - enemies_new[i].y) * math.fabs(k)
                    else:
                        enemies_new[i].x = ground.points[j][0]
                        enemies_new[i].y = ground.points[j][1]
                    flag = 1
        if enemies_new[i].v < 0:
            for j in range(len(ground.points) - 1, 0, -1):
                if ground.points[j][0] < enemies_new[i].x and flag == 0:
                    k = math.fabs(v_lasts / math.hypot(ground.points[j][0] - enemies_new[i].x, ground.points[j][1] - enemies_new[i].y))
                    if k < 1:
                        enemies_new[i].x += (ground.points[j][0] - enemies_new[i].x) * k
                        enemies_new[i].y += (ground.points[j][1] - enemies_new[i].y) * k
                    else:
                        enemies_new[i].x = ground.points[j][0]
                        enemies_new[i].y = ground.points[j][1]
                    flag = 1
    return bombs_new, enemies_new