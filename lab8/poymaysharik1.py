import pygame
from pygame.draw import *
from random import randint
pygame.init()

FPS = 1
screen = pygame.display.set_mode((1200, 900))

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]


class ball:
    def __init__(self):
        self.color = COLORS[randint(0, len(COLORS)-1)]
        self.r = randint(2, 10)
        self.x = randint(0, xx)
        self.vx = randint(-5, 5)
        self.vy = randint(-5, 5)

    def color(self):
        return self.color

    def r(self):
        return self.r

    def x(self):
        return self.x

    def y(self):
        return y

def poverka1PoX(krug):
    if krug.x()>krug.r():
        return True
    else:
        return False

def poverka1PoY(krug):
    if krug.y() > krug.r():
        return True
    else:
        return False

def poverka2PoX(krug):
    if x0-krug.x() < krug.r():
        return True
    else:
        return False

def poverka2PoY(krug):
    if y0-krug.y() > krug.r():
        return True
    else:
        return False

def rasvorot(krug):
    if not krug.poverka1PoX():
        krug.vx=randint(1,5)
    if not krug.poverka1PoY():
        krug.vy=randint(1,5)
    if not krug.poverka2PoX():
        krug.vx=randint(-5,-1)
    if not krug.poverka2PoY():
        krug.vy=randint(-5,-1)




def new_ball():
        '''рисует новый шарик '''
        x = randint(100, 1100)
        y = randint(100, 900)
        r = randint(10, 100)
        circle(screen, color(), (x(), y()), r())

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print('Click!')
    new_ball()
    pygame.display.update()
    screen.fill(BLACK)

pygame.quit()
