import pygame
from pygame.draw import *
from random import randint

pygame.init()

FPS = 50
x0 = 1000
y0 = 700
screen = pygame.display.set_mode((x0, y0))
font = pygame.font.SysFont('arial', 30)

BYKVI = (122, 36, 0)
FON = (0, 22, 200)

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]


class Ball:
    def __init__(self):
        self.__color = COLORS[randint(0, len(COLORS) - 1)]
        self.__r = randint(30, 50)
        self.__x = randint(0, x0)
        self.__y = randint(0, y0)
        self.__vx = randint(-10, 10)
        self.__vy = randint(-10, 10)

    def get_color(self):
        return self.__color

    def get_r(self):
        return self.__r

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def get_vx(self):
        return self.__vx

    def get_vy(self):
        return self.__vy

    def set_vx(self, vx):
        self.__vx = vx

    def set_vy(self, vy):
        self.__vy = vy

    def set_x(self, x):
        self.__x = x

    def set_y(self, y):
        self.__y = y

    def poverka1PoX(krug):
        if krug.get_x() > krug.get_r():
            return True
        else:
            return False

    def poverka1PoY(krug):
        if krug.get_y() > krug.get_r():
            return True
        else:
            return False

    def poverka2PoX(krug):
        if (x0 - krug.get_x()) > krug.get_r():
            return True
        else:
            return False

    def poverka2PoY(krug):
        if (y0 - krug.get_y()) > krug.get_r():
            return True
        else:
            return False


def rasvorot(krug):
    if not krug.poverka1PoX():
        krug.set_vx(randint(1, 7))
    if not krug.poverka1PoY():
        krug.set_vy(randint(1, 7))
    if not krug.poverka2PoX():
        krug.set_vx(randint(-7, -1))
    if not krug.poverka2PoY():
        krug.set_vy(randint(-7, -1))


def new_ball(balls):
    while len(balls) < 3:
        a = Ball()
        balls.append(a)
    return balls


def popadanie(sharik):
    if ((event.pos[0] - sharik.get_x()) ** 2
            + (event.pos[1] - sharik.get_y()) ** 2
            <= (sharik.get_r()) ** 2):
        return True


pygame.display.update()
clock = pygame.time.Clock()
finished = False
b = []
result = 0
promach = 0
while not finished:
    clock.tick(FPS)
    new_ball(b)
    for i in range(len(b)):
        b[i].set_x(b[i].get_x() + b[i].get_vx())
        b[i].set_y(b[i].get_y() + b[i].get_vy())
        circle(screen, b[i].get_color(), (b[i].get_x(), b[i].get_y()), b[i].get_r())
        rasvorot(b[i])
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            popal = 0
            for i in range(len(b)):
                if popadanie(b[i]):
                    result += 1
                    popal = i + 1
            if popal == 0:
                promach += 1
            else:
                b.remove(b[popal - 1])
            if promach >= 5:
                finished = True
    nadpis = font.render(f'Счёт:{result}', True, BYKVI, FON)
    screen.blit(nadpis, (0, 0))
    pygame.display.update()
    screen.fill(BLACK)

finished = False
screen.fill(BLACK)

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        else:
            nadpis = font.render(f'Игра закончена. Ваш счёт:{result}', True, BYKVI, FON)
            screen.blit(nadpis, ((x0 - 300) // 2, (y0 - 100) // 2))
    pygame.display.update()

pygame.quit()
