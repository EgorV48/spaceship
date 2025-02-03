import pygame
import random
import sys

pygame.init()

WIDTH = 1280
HEIGHT = 960

clock = pygame.time.Clock()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("𝕾𝖕𝖆𝖈𝖊𝖘𝖍𝖎𝖕")

while True:
    screen.fill((0, 0 ,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
