import random


class Plane:
    x = 0
    y = 0
    vx = 0
    vy = 0
    bombs = 1
    force = 1


class Ground:
    points = [random.randint(50, 150)]*30
    color = 'GREEN'
