import pygame
import random
import sys

pygame.init()

WIDTH = 1280
HEIGHT = 960

clock = pygame.time.Clock()
pygame.mixer.init()

shot_sound = pygame.mixer.Sound("data/vistril.mp3")
explosion_sound = pygame.mixer.Sound("data/popal.mp3")
fon_music = "data/fon.mp3"
game_music = "data/game.mp3"

def play_music(music_file):
    global current_music, music_playing
    if current_music != music_file:  # Если музыка уже играет, не переключаем
        pygame.mixer.music.load(music_file)
        pygame.mixer.music.play(-1)  # Бесконечное воспроизведение
        current_music = music_file
        music_playing = True

# Функция для остановки музыки
def stop_music():
    global music_playing
    pygame.mixer.music.stop()
    music_playing = False

# Функция для паузы музыки
def pause_music():
    global music_playing
    pygame.mixer.music.pause()
    music_playing = False

# Функция для возобновления музыки
def unpause_music():
    global music_playing
    pygame.mixer.music.unpause()
    music_playing = True

background = pygame.image.load("data/fon.jpg")
fon_spaceship = pygame.image.load("data/spaceship.png")
fon_game = pygame.image.load("data/fon_game.jpg")
main_spaceship = pygame.image.load("data/main_spaceship.png")
fire_image = pygame.image.load("data/fire.png")
asteroid_image = pygame.image.load("data/str_1.png")
boom_1_asteroid = pygame.image.load("data/boom_1.png")
boom_2_asteroid = pygame.image.load("data/boom_2.png")

font = pygame.font.Font(None, 100)
text_name = font.render("Spaceship", False, (54, 169, 205))
text_start = font.render("Начать игру", False, (54, 169, 205))
text_quit = font.render("Выйти", False, (54, 169, 205))
text_pause = font.render("Пауза", False, (54, 169, 205))
text_menu = font.render("Меню",  False, (54, 169, 205))
text_continue = font.render("Продолжить", False, (54, 169, 205))
text_game_over = font.render("Game Over", True, (255, 0, 0))

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

def main_menu_func(pos_mouse):
    global main_menu, rect_width_start, rect_height_start, rect_width_quit, rect_height_quit, fon_spaceship_x, fon_spaceship_y
    screen.blit(background, (0, 0))
    screen.blit(text_name, (280, 90))
    screen.blit(fon_spaceship, (fon_spaceship_x, fon_spaceship_y))

    # Кнопка "Начать игру"
    start_button_rect = pygame.Rect(850, 90, rect_width_start, rect_height_start)
    start_hover = start_button_rect.collidepoint(pos_mouse)
    draw_button(screen, "Начать игру", 850, 90, rect_width_start, rect_height_start, start_hover)

    # Кнопка "Выйти"
    quit_button_rect = pygame.Rect(850, 192, rect_width_quit, rect_height_quit)
    quit_hover = quit_button_rect.collidepoint(pos_mouse)
    draw_button(screen, "Выйти", 850, 192, rect_width_quit, rect_height_quit, quit_hover)

    if start_hover:
        if rect_width_start < 425:
            rect_width_start += 1
        if rect_height_start < 82:
            rect_height_start += 1
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            main_menu = False
            play_music(game_music)  # Включаем игровую музыку
    else:
        rect_width_start = 410
        rect_height_start = 72

    if quit_hover:
        if rect_width_quit < 425:
            rect_width_quit += 1
        if rect_height_quit < 82:
            rect_height_quit += 1
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            pygame.quit()
            sys.exit()
    else:
        rect_width_quit = 410
        rect_height_quit = 72

def draw_button(screen, text, x, y, width, height, hover):
    """Рисует кнопку с анимацией при наведении."""
    button_rect = pygame.Rect(x, y, width, height)
    color = HOVER_COLOR if hover else BUTTON_COLOR
    pygame.draw.rect(screen, color, button_rect, border_radius=10)

    text_surface = font.render(text, True, TEXT_COLOR)
    text_rect = text_surface.get_rect(center=button_rect.center)
    screen.blit(text_surface, text_rect)

def main_menu_func(pos_mouse):
    global main_menu, rect_width_start, rect_height_start, rect_width_quit, rect_height_quit, fon_spaceship_x, fon_spaceship_y
    screen.blit(background, (0, 0))
    screen.blit(text_name, (280, 90))
    screen.blit(fon_spaceship, (fon_spaceship_x, fon_spaceship_y))

    # Кнопка "Начать игру"
    start_button_rect = pygame.Rect(850, 90, rect_width_start, rect_height_start)
    start_hover = start_button_rect.collidepoint(pos_mouse)
    draw_button(screen, "Начать игру", 850, 90, rect_width_start, rect_height_start, start_hover)

    # Кнопка "Выйти"
    quit_button_rect = pygame.Rect(850, 192, rect_width_quit, rect_height_quit)
    quit_hover = quit_button_rect.collidepoint(pos_mouse)
    draw_button(screen, "Выйти", 850, 192, rect_width_quit, rect_height_quit, quit_hover)

    if start_hover:
        if rect_width_start < 425:
            rect_width_start += 1
        if rect_height_start < 82:
            rect_height_start += 1
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            main_menu = False
            play_music(game_music)  # Включаем игровую музыку
    else:
        rect_width_start = 410
        rect_height_start = 72

    if quit_hover:
        if rect_width_quit < 425:
            rect_width_quit += 1
        if rect_height_quit < 82:
            rect_height_quit += 1
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            pygame.quit()
            sys.exit()
    else:
        rect_width_quit = 410
        rect_height_quit = 72

def pause_game(fl, pos_mouse, event):
    global pause, main_menu, pause_num
    if fl == 0:
        pause = True
        pause_music()  # Приостанавливаем музыку
        # Рисуем полупрозрачный черный фон для меню паузы
        pause_surface = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
        pygame.draw.rect(pause_surface, (0, 0, 0, 150), (0, 0, WIDTH, HEIGHT))
        screen.blit(pause_surface, (0, 0))

        # Координаты и размеры кнопок
        button_width = 450
        button_height = 80
        button_x = (WIDTH - button_width) // 2  # Центрируем по горизонтали
        button_y_continue = (HEIGHT - button_height * 2 - 20) // 2  # Первая кнопка выше
        button_y_menu = button_y_continue + button_height + 20  # Вторая кнопка ниже

        # Надпись "Пауза"
        pause_text = font.render("Пауза", True, (255, 255, 255))
        pause_text_rect = pause_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 150))
        screen.blit(pause_text, pause_text_rect)

        # Кнопка "Продолжить"
        continue_button_rect = pygame.Rect(button_x, button_y_continue, button_width, button_height)
        continue_hover = continue_button_rect.collidepoint(pos_mouse)
        draw_button(screen, "Продолжить", button_x, button_y_continue, button_width, button_height, continue_hover)

        # Кнопка "Меню"
        menu_button_rect = pygame.Rect(button_x, button_y_menu, button_width, button_height)
        menu_hover = menu_button_rect.collidepoint(pos_mouse)
        draw_button(screen, "Меню", button_x, button_y_menu, button_width, button_height, menu_hover)

        # Обработка кликов
        if menu_hover and event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            main_menu = True
            pause = False
            play_music(fon_music)  # Включаем фоновую музыку
        if continue_hover and event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            pause_num = 1 - pause_num
            pause = False
            unpause_music()  # Возобновляем музыку
    elif fl == 1:
        pause = False
        unpause_music()  # Возобновляем музыку

def game_over_screen(pos_mouse):
    global game_over, main_menu, score, asteroids, fires, main_spaceship_x, main_spaceship_y, game_speed

    # Рисуем полупрозрачный черный фон
    overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
    pygame.draw.rect(overlay, (0, 0, 0, 150), (0, 0, WIDTH, HEIGHT))
    screen.blit(overlay, (0, 0))

    # Надпись "Game Over"
    game_over_text = font.render("Game Over", True, (255, 0, 0))
    game_over_rect = game_over_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 100))
    screen.blit(game_over_text, game_over_rect)

    # Кнопка "Начать заново"
    restart_button_rect = pygame.Rect(WIDTH // 2 - 150, HEIGHT // 2, 300, 80)
    restart_hover = restart_button_rect.collidepoint(pos_mouse)
    draw_button(screen, "Начать заново", WIDTH // 2 - 250, HEIGHT // 2, 500, 80, restart_hover)

    # Кнопка "Выйти в меню"
    menu_button_rect = pygame.Rect(WIDTH // 2 - 150, HEIGHT // 2 + 100, 300, 80)
    menu_hover = menu_button_rect.collidepoint(pos_mouse)
    draw_button(screen, "Выйти в меню", WIDTH // 2 - 250, HEIGHT // 2 + 100, 500, 80, menu_hover)

    # Обработка кликов
    if restart_hover and event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
        game_over = False
        score = 0
        asteroids.clear()
        fires.clear()
        explosions.clear()
        main_spaceship_x = 490
        main_spaceship_y = 700
        game_speed = 1.0
        play_music(game_music)  # Включаем игровую музыку
    if menu_hover and event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
        game_over = False
        main_menu = True
        score = 0
        asteroids.clear()
        fires.clear()
        explosions.clear()
        main_spaceship_x = 490
        main_spaceship_y = 700
        game_speed = 1.0
        play_music(fon_music)  # Включаем фоновую музыку

while True:
    screen.fill((0, 0 ,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
