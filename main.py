import os, sys, pygame, math, random
from pygame.locals import *

pygame.init()
fps_clock = pygame.time.Clock()

display_width = 640
display_height = 480

title = 'Snake'
crashed = False

font_obj = pygame.font.SysFont('Times New Roman', 15)
window_surface_obj = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('{0}'.format(title))

red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)
white = pygame.Color(255, 255, 255)
black = pygame.Color(0, 0, 0)


# adds png to sprite dictionary
def update_dict(sprite_name, dict):
    dict[sprite_name] = pygame.image.load('resources/{0}.png'.format(sprite_name))


# just blit rewritten for convenience
def render(x, y, sprite):
    window_surface_obj.blit(sprite, (x * 16, y * 16))


# render a variable as text onscreen
def display_data(x, y, data, font, color):
    datatext = font.render("{0}".format(data), True, color)
    window_surface_obj.blit(datatext, (x, y))


def reseed():
    x = random.randint(0, 39)
    y = random.randint(0, 29)
    for s in snake:
        if [x, y] != s:
            return [x, y]
        else:
            return reseed()


snake = [[19, 15], [20, 15], [20, 15], [20, 15]]
apple = reseed()
direction = 180
score = 0
locations = {}
for x in range(1, len(snake), 1):
    locations[x] = snake[x - 1]
time = 0
turned = 0
# auto fill dictionary with sprites from resources
img_dict = {}
for filename in os.listdir('resources'):
    if filename[-4:] == '.png':
        update_dict(filename[:-4], img_dict)

while not crashed:
    window_surface_obj.fill(black)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    if pygame.key.get_pressed()[pygame.K_UP] != 0:
        if direction != 90 and turned == 0:
            direction = -90
            turned = 1
    if pygame.key.get_pressed()[pygame.K_LEFT] != 0:
        if direction != 0 and turned == 0:
            direction = 180
            turned = 1
    if pygame.key.get_pressed()[pygame.K_RIGHT] != 0:
        if direction != 180 and turned == 0:
            direction = 0
            turned = 1
    if pygame.key.get_pressed()[pygame.K_DOWN] != 0:
        if direction != -90 and turned == 0:
            direction = 90
            turned = 1
    if time % (15 - score) == 0:
        for x in range(0, len(snake), 1):
            locations[x] = [snake[x][0], snake[x][1]]
            if x != 0:
                snake[x] = locations[x - 1]
            else:
                snake[0][0] += math.cos(math.radians(direction))
                snake[0][1] += math.sin(math.radians(direction))
                turned = 0
    render(apple[0], apple[1], img_dict['block'])
    display_data(0, 0, score, font_obj, white)
    for x in range(1, len(snake), 1):
        if snake[0] == snake[x]:
            crashed = True
    if 0 < snake[0][0] < 40 and 0 < snake[0][1] < 30:
        pass
    else:
        crashed = True
    for s in snake:
        render(s[0], s[1], img_dict['block'])
        s[0] = round(s[0])
        s[1] = round(s[1])
    if snake[0] == apple:
        snake.append([snake[len(snake) - 1][0], snake[len(snake) - 1][1]])
        apple = reseed()
        if score < 15:
            score += 1
    pygame.display.update()
    time += 1
    fps_clock.tick(30)
