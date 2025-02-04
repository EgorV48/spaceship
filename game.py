import pygame
import random
import sys

pygame.init()

WIDTH = 1280
HEIGHT = 960

clock = pygame.time.Clock()

shot_sound = pygame.mixer.Sound("data/vistril.mp3")
explosion_sound = pygame.mixer.Sound("data/popal.mp3")
fon_music = "data/fon.mp3"
game_music = "data/game.mp3"

background = pygame.image.load("data/fon.jpg")
fon_spaceship = pygame.image.load("data/spaceship.png")
fon_game = pygame.image.load("data/fon_game.jpg")
main_spaceship = pygame.image.load("data/main_spaceship.png")
fire_image = pygame.image.load("data/fire.png")
asteroid_image = pygame.image.load("data/str_1.png")
boom_1_asteroid = pygame.image.load("data/boom_1.png")
boom_2_asteroid = pygame.image.load("data/boom_2.png")

# Координаты и размеры
rect_width_start = 410
rect_height_start = 72

rect_width_quit = 410
rect_height_quit = 72

fon_spaceship_x = -250
fon_spaceship_y = 400

main_spaceship_x = 490
main_spaceship_y = 700

fon_x = 0
fon_y = 0

BUTTON_COLOR = (30, 30, 30)
HOVER_COLOR = (54, 169, 205)
TEXT_COLOR = (255, 255, 255)

asteroids = []
fires = []
explosions = []

score = 0

game_speed = 1.0

game_over = False

MAX_ASTEROID_SPEED = 10

main_menu = True
pause = False
pause_num = 1

fon_y1 = 0
fon_y2 = -HEIGHT

asteroid_spawn_time = 1000
last_asteroid_spawn = pygame.time.get_ticks()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("𝕾𝖕𝖆𝖈𝖊𝖘𝖍𝖎𝖕")

while True:
    screen.fill((0, 0 ,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
