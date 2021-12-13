import math
import random
import pygame


class Plane:
    x = 0
    y = 0
    vx = 1
    vy = 0
    v = 1
    bombs = 1
    force = 1
    hitbox = 10
    health = 1000
    img = pygame.image.load('bomber.png')
    img.set_colorkey((255, 255, 255))
    img = pygame.transform.scale(img, (60, 20))

    def speed_recalculation(self, event):
        self.vx = self.v * math.sin(math.atan2(event.pos[0] - self.x, event.pos[1] - self.y))
        self.vy = self.v * math.cos(math.atan2(event.pos[0] - self.x, event.pos[1] - self.y))

    def get_real_image(self):
        img = pygame.transform.rotate(self.img, -self.vx/math.fabs(self.vx)*180*math.atan2(self.vy, self.vx)/math.pi)
        if self.vx < 0:
            img = pygame.transform.flip(img, False, True)
        return img

class Ground:
    points = []
    color = 'GREEN'


class Bomb:
    def __init__(self, x, y, vx, vy):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
    x = 0
    y = 0
    vx = 0
    vy = 0
    damage = 100
    enemy = False
    img = pygame.image.load('bomb.png')
    img.set_colorkey((255, 255, 255))
    img = pygame.transform.scale(img, (60, 20))

    def groundcheck(self, ground):
        detonated = False
        for i in range(len(ground.points) - 1):
            if ground.points[i][0] < self.x < ground.points[i + 1][0] and (
                    ground.points[i][1] < self.y or ground.points[i + 1][1] < self.y):
                detonated = True
                if ground.points[i][0] - self.x < ground.points[i + 1][0] - self.x:
                    ground.points[i][1] += 5
                else:
                    ground.points[i + 1][1] += 5
        return ground, detonated

    def get_real_image(self):
        img = pygame.transform.rotate(self.img, -self.vx/math.fabs(self.vx)*180*math.atan2(self.vy, self.vx)/math.pi)
        if self.vx < 0:
            img = pygame.transform.flip(img, False, True)
        return img

    def enemycheck(self, enemy):
        detonated = math.hypot(self.x - enemy.x, self.y - enemy.y) < enemy.hitbox and not self.enemy
        if detonated:
            enemy.health -= self.damage
        return detonated, enemy

    def planecheck(self, plane):
        detonated = math.hypot(self.x - plane.x, self.y - plane.y) < plane.hitbox and self.enemy
        if detonated:
            plane.health -= self.damage
        return detonated


class Enemy:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    health = 0
    x = 0
    y = 0
    v = 0
    cd = 10
    hitbox = 0
    img = pygame.image.load('Tank.png')
    img.set_colorkey((255, 255, 255))
    img = pygame.transform.scale(img, (60, 20))

    def moveforward(self, ground):
        if self.x >= ground.points[len(ground.points) - 1][0] - 1 and self.v > 0:
            self.v = -self.v
        if self.x <= ground.points[0][0] + 1 and self.v < 0:
            self.v = -self.v
        v_lasts = self.v
        flag = 0
        if self.v > 0:
            for j in range(len(ground.points)):
                if ground.points[j][0] > self.x and flag == 0:
                    k = v_lasts / math.hypot(ground.points[j][0] - self.x, ground.points[j][1] - self.y)
                    if k < 1:
                        self.x += (ground.points[j][0] - self.x) * k
                        self.y += (ground.points[j][1] - self.y) * math.fabs(k)
                    else:
                        self.x = ground.points[j][0]
                        self.y = ground.points[j][1]
                    flag = 1
        if self.v < 0:
            for j in range(len(ground.points) - 1, 0, -1):
                if ground.points[j][0] < self.x and flag == 0:
                    k = math.fabs(v_lasts / math.hypot(ground.points[j][0] - self.x,
                                                       ground.points[j][1] - self.y))
                    if k < 1:
                        self.x += (ground.points[j][0] - self.x) * k
                        self.y += (ground.points[j][1] - self.y) * k
                    else:
                        self.x = ground.points[j][0]
                        self.y = ground.points[j][1]
                    flag = 1

    def fire(self, plane):
        d = math.hypot(plane.x - self.x, plane.y - self.y)
        shot = Bomb(self.x, self.y, 10*(plane.x - self.x)/d, 10*(plane.y - self.y)/d)
        shot.enemy = True
        return shot

class Tank(Enemy):
    health = 50
    hitbox = 20
    v = 1

