import pygame
import random
import sys

pygame.init()

WIDTH = 1280
HEIGHT = 960

clock = pygame.time.Clock()

shot_sound = pygame.mixer.Sound("data/vistril.mp3")  # Звук выстрела
explosion_sound = pygame.mixer.Sound("data/popal.mp3")  # Звук взрыва
fon_music = "data/fon.mp3"
game_music = "data/game.mp3"

background = pygame.image.load("data/fon.jpg")
fon_spaceship = pygame.image.load("data/spaceship.png")
fon_game = pygame.image.load("data/fon_game.jpg")  # Твой фон
main_spaceship = pygame.image.load("data/main_spaceship.png")
fire_image = pygame.image.load("data/fire.png")  # Огонь для стрельбы
asteroid_image = pygame.image.load("data/str_1.png")  # Загрузи изображение астероида
boom_1_asteroid = pygame.image.load("data/boom_1.png")
boom_2_asteroid = pygame.image.load("data/boom_2.png")


screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("𝕾𝖕𝖆𝖈𝖊𝖘𝖍𝖎𝖕")

while True:
    screen.fill((0, 0 ,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
