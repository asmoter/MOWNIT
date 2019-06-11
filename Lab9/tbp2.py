import pygame
import sys
from pygame.locals import *
from numpy import *

SCREEN_WIDTH, SCREEN_HEIGHT = 800, 700
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
mode = 3

G = 6.673e-1  # stala grawitacyjna

# Tablice przechowujace parametry poszczegolnych cial

pos = []  # pozycje
v = []  # predkosci
m = []  # masy
r = []  # promienie
c = []  # kolor

sun_r = 5000
sun_m = 100000000
earth_r = 1000
earth_m = 100000000
mars_r = 1000
mars_m = 1000000

sun_x = 0
sun_y = 0
sun_dx = -15
sun_dy = 0

earth_x = 0
earth_y = 100000
earth_dx = 15
earth_dy = 0

mars_x = 0
mars_y = 250000
mars_dx = 30
mars_dy = 0


def create_object(x, y, dx, dy, radius, mass, color):
    pos.append([x, y])
    v.append([dx, dy])  # predkosc
    r.append(radius)
    m.append(mass)
    c.append(color)


class Button:
    def __init__(self, x, y, width, height, font, value, text='mode = '):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = (255, 182, 193)
        self.text = text + str(value)
        self.value = value
        self.font = font
        self.active = False

    def draw(self, screen, font):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height), 0)
        text = font.render(self.text, 1, (0, 0, 0), self.color)
        screen.blit(text, (self.x + (self.width / 2 - text.get_width() / 2), self.y + (self.height / 2 - text.get_height() / 2)))

    def isOverButton(self, pos):
        if self.x < pos[0] < self.x + self.width:
            if self.y < pos[1] < self.y + self.height:
                return True

        return False

    def handleEvent(self, event):
        global mode
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            position = pygame.mouse.get_pos()
            if self.isOverButton(position):
                self.active = not self.active
                SCREEN.fill((0, 0, 50))
                pygame.display.flip()
                if self.active:
                    mode = self.value
                    print("Mode: ", mode)
            else:
                self.active = False
            self.color = (255, 218, 185) if self.active else (255, 182, 193)


def main():
    global mode, sun_x, sun_y, sun_dx, sun_dy, pos

    pygame.init()
    font = pygame.font.SysFont('Consolas', 16)
    pygame.display.set_caption('Three body problem')
    running = True
    objs = 0

    button_1 = Button(200, 600, 100, 50, font, 1, "mode")
    button_2 = Button(350, 600, 100, 50, font, 2, "mode")
    button_3 = Button(500, 600, 100, 50, font, 3, "mode")
    buttons = [button_1, button_2, button_3]

    SCREEN.fill((0, 0, 50))
    #
    # if mode == 1:
    #     sun_dx = -15
    # elif mode == 2:
    #     sun_dx = -30
    # else:
    #     sun_dx = -10

    objs += 3

    while running:

        if mode == 1:
            sun_dx = -15
        elif mode == 2:
            sun_dx = -30
        else:
            sun_dx = -10

        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
            for b in buttons:
                b.handleEvent(event)

        create_object(sun_x, sun_y, sun_dx, sun_dy, sun_r, sun_m, (255, 215, 0))  # sun
        create_object(earth_x, earth_y, earth_dx, earth_dy, earth_r, earth_m, (0, 206, 209))  # earth
        create_object(mars_x, mars_y, mars_dx, mars_dy, mars_r, mars_m, (255, 69, 0))  # mars

        for n in range(250):
            for i in range(objs):
                pos[i][0] += v[i][0]
                pos[i][1] += v[i][1]
                for j in range(objs):
                    if i != j:
                        dist = ((pos[i][0] - pos[j][0]) ** 2 + (pos[i][1] - pos[j][1]) ** 2) ** 0.5
                        dist -= r[i] + r[j]
                        if dist < 0:
                            pass
                        else:
                            alpha = arcsin((pos[i][0] - pos[j][0]) / (dist + r[i] + r[j]))
                            F = G * (m[i] * m[j]) / dist ** 2
                            F /= m[i]
                            v_x = F * sin(alpha)
                            v_y = F * cos(alpha)
                            if pos[i][1] > pos[j][1]:
                                v[i][1] -= v_y
                            else:
                                v[i][1] += v_y
                            v[i][0] -= v_x
                        # print(pos[i])

        SCREEN.fill((0, 0, 50))
        for i in range(objs):
            pygame.draw.circle(SCREEN, c[i],
                               (int(pos[i][0] / 1000) + 400, int(pos[i][1] / 1000) + 300), int(r[i] / 500) + 3, 0)

        for b in buttons:
            b.draw(SCREEN, font)

        pygame.display.update()


if __name__ == '__main__':
    main()