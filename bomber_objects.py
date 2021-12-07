import math
import random


class Plane:
    x = 0
    y = 0
    vx = 0
    vy = 0
    v = 1
    bombs = 1
    force = 1

    def speed_recalculation(self, event):
        self.vx = self.v * math.sin(math.atan2(event.pos[0] - self.x, event.pos[1] - self.y))
        self.vy = self.v * math.cos(math.atan2(event.pos[0] - self.x, event.pos[1] - self.y))
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


class Enemy:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    health = 0
    x = 0
    y = 0
    v = 0
    hitbox = 0


class Tank(Enemy):
    health = 1000
    hitbox = 10
    v = 1
