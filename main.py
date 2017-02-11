import os, sys, pygame
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
    window_surface_obj.blit(sprite, (x, y))


# render a variable as text onscreen
def display_data(x, y, data, font, color):
    datatext = font.render("{0}".format(data), True, color)
    window_surface_obj.blit(datatext, (x, y))


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
        pass
    pygame.display.update()
    fps_clock.tick(30)
