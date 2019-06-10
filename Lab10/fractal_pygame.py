import random
import sys
import pygame

SCREEN_WIDTH, SCREEN_HEIGHT = 800, 700
mode = 0
restart = False

# X = [0]
# Y = [0]

f_1_f = [0, 0, 0, 0, 0.16, 0]
f_2_f = [0.85, 0.04, 0, -0.04, 0.85, 1.6]
f_3_f = [0.2, -0.26, 0, 0.23, 0.22, 1.6]
f_4_f = [-0.15, 0.28, 0, 0.26, 0.24, 0.44]

f_1_t = [0.05, 0, 0, 0, 0.6, 0]
f_2_t = [0.05, 0, 0, 0, -0.5, 1]
f_3_t = [0.46, -0.321, 0, 0.386, 0.383, 0.6]
f_4_t = [0.47, -0.154, 0, 0.171, 0.423, 1.1]
f_5_t = [0.433, 0.275, 0, -0.25, 0.476, 0.16]
f_6_t = [0.421, 0.257, 0, -0.353, 0.306, 0.7]

f_1_t2 = [0.01, 0, 0, 0, 0.45, 0]
f_2_t2 = [-0.01, 0, 0, 0, -0.45, 0.4]
f_3_t2 = [0.42, -0.42, 0, 0.42, 0.42, 0.4]
f_4_t2 = [0.42, 0.42, 0, -0.42, 0.42, 0.4]


def get_f_fern():
    p = random.uniform(0, 100)
    if p < 1.0:
        return f_1_f
    elif p < 86.0:
        return f_2_f
    elif p < 93.0:
        return f_3_f
    else:
        return f_4_f


def get_f_tree():
    p = random.uniform(0, 100)
    if p < 17.0:
        return f_1_t
    elif p < 34.0:
        return f_2_t
    elif p < 51.0:
        return f_3_t
    elif p < 68.0:
        return f_4_t
    elif p < 84.0:
        return f_5_t
    else:
        return f_6_t


def get_f_tree2():
    p = random.uniform(0, 100)
    if p < 25.0:
        return f_1_t2
    elif p < 50.0:
        return f_2_t2
    elif p < 75.0:
        return f_3_t2
    else:
        return f_4_t2


def iterate(x, y, mode):
    if mode == 1:
        for t in range(100):
            f = get_f_fern()
            x1 = f[0] * x[t-1] + f[1] * y[t-1] + f[2]
            y1 = f[3] * x[t-1] + f[4] * y[t-1] + f[5]
            x.append(x1)
            y.append(y1)
    elif mode == 2:
        for t in range(100):
            f = get_f_tree2()
            x1 = f[0] * x[t-1] + f[1] * y[t-1] + f[2]
            y1 = f[3] * x[t-1] + f[4] * y[t-1] + f[5]
            x.append(x1)
            y.append(y1)
    elif mode == 3:
        for t in range(100):
            f = get_f_tree()
            x1 = f[0] * x[t-1] + f[1] * y[t-1] + f[2]
            y1 = f[3] * x[t-1] + f[4] * y[t-1] + f[5]
            x.append(x1)
            y.append(y1)


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
        global restart
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            if self.isOverButton(pos):
                self.active = not self.active
                if self.active:
                    mode = self.value
                else:
                    restart = True
            else:
                self.active = False
            self.color = (255, 218, 185) if self.active else (255, 182, 193)


def main():

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("IFS")
    font = pygame.font.SysFont('Consolas', 16)
    screen.fill((255, 250, 240))
    running = True

    button_1 = Button(200, 600, 100, 50, font, 1, "mode")
    button_2 = Button(350, 600, 100, 50, font, 2, "mode")
    button_3 = Button(500, 600, 100, 50, font, 3, "mode")
    buttons = [button_1, button_2, button_3]

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
            for b in buttons:
                b.handleEvent(event)
                b.draw(screen, font)

        # if restart:
        #     screen.fill((255, 250, 240))
        pygame.display.update()

        if mode == 1:
            X = [0]
            Y = [0]
            iterate(X, Y, mode)
            color = (60, 179, 113)
            for i in range(len(X)):
                pygame.draw.circle(screen, color, (int(X[i]*50 + 400), int(-Y[i]*50 + 550)), 1)
        elif mode == 2:
            X = [0]
            Y = [0]
            iterate(X, Y, mode)
            color = (0, 206, 209)
            for i in range(len(X)):
                pygame.draw.circle(screen, color, (int(X[i]*500 + 400), int(-Y[i]*500 + 550)), 1)
        else:
            X = [0]
            Y = [0]
            iterate(X, Y, mode)
            color = (238, 130, 238)
            for i in range(len(X)):
                pygame.draw.circle(screen, color, (int(X[i]*300 + 400), int(-Y[i]*300 + 550)), 1)
        pygame.display.update()
        # if restart:
        #     screen.fill((255, 250, 240))
        # pygame.display.flip()
        # pygame.time.delay(1000)
        # running = False


if __name__ == '__main__':
    main()
