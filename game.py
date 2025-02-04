import pygame
import sys
import random

pygame.init()

WIDTH = 1280
HEIGHT = 960

clock = pygame.time.Clock()
pygame.mixer.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("𝕾𝖕𝖆𝖈𝖊𝖘𝖍𝖎𝖕")


fon_music = "data/fon.mp3"
game_music = "data/game.mp3"
current_music = None
music_playing = False

def play_music(music_file):
    global current_music, music_playing
    if current_music != music_file:
        pygame.mixer.music.load(music_file)
        pygame.mixer.music.play(-1)
        current_music = music_file
        music_playing = True

def stop_music():
    global music_playing
    pygame.mixer.music.stop()
    music_playing = False

def pause_music():
    global music_playing
    pygame.mixer.music.pause()
    music_playing = False

def unpause_music():
    global music_playing
    pygame.mixer.music.unpause()
    music_playing = True

background = pygame.image.load("data/fon.jpg")
fon_spaceship = pygame.image.load("data/spaceship.png")
fon_game = pygame.image.load("data/fon_game.jpg")  # Твой фон
main_spaceship = pygame.image.load("data/main_spaceship.png")
fire_image = pygame.image.load("data/fire.png")  # Огонь для стрельбы
asteroid_image = pygame.image.load("data/str_1.png")  # Загрузи изображение астероида
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

class Asteroid:
    def __init__(self):
        self.x = random.randint(0, WIDTH - 77)
        self.y = -50
        self.speed = random.randint(3, 5)
        self.image = asteroid_image
        self.rect = self.image.get_rect(topleft=(self.x, self.y))

    def move(self):
        self.y += self.speed
        self.rect.topleft = (self.x, self.y)

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def is_off_screen(self):
        return self.y > HEIGHT

class Fire:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 10
        self.image = fire_image
        self.rect = self.image.get_rect(center=(self.x, self.y))

    def move(self):
        self.y -= self.speed
        self.rect.center = (self.x, self.y)

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def is_off_screen(self):
        return self.y < 0

class Explosion:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.frames = [boom_1_asteroid, boom_2_asteroid]
        self.current_frame = 0
        self.frame_duration = 100
        self.last_frame_time = pygame.time.get_ticks()

    def update(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_frame_time > self.frame_duration:
            self.current_frame += 1
            self.last_frame_time = current_time

    def draw(self, screen):
        if self.current_frame < len(self.frames):
            screen.blit(self.frames[self.current_frame], (self.x, self.y))

    def is_finished(self):
        return self.current_frame >= len(self.frames)

asteroids = []
fires = []
explosions = []

score = 0

game_speed = 1.0

game_over = False

MAX_ASTEROID_SPEED = 10

def draw_button(screen, text, x, y, width, height, hover):
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

    start_button_rect = pygame.Rect(850, 90, rect_width_start, rect_height_start)
    start_hover = start_button_rect.collidepoint(pos_mouse)
    draw_button(screen, "Начать игру", 850, 90, rect_width_start, rect_height_start, start_hover)

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
            play_music(game_music)
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
        pause_music()
        pause_surface = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
        pygame.draw.rect(pause_surface, (0, 0, 0, 150), (0, 0, WIDTH, HEIGHT))
        screen.blit(pause_surface, (0, 0))

        button_width = 450
        button_height = 80
        button_x = (WIDTH - button_width) // 2  # Центрируем по горизонтали
        button_y_continue = (HEIGHT - button_height * 2 - 20) // 2  # Первая кнопка выше
        button_y_menu = button_y_continue + button_height + 20  # Вторая кнопка ниже

        pause_text = font.render("Пауза", True, (255, 255, 255))
        pause_text_rect = pause_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 150))
        screen.blit(pause_text, pause_text_rect)

        continue_button_rect = pygame.Rect(button_x, button_y_continue, button_width, button_height)
        continue_hover = continue_button_rect.collidepoint(pos_mouse)
        draw_button(screen, "Продолжить", button_x, button_y_continue, button_width, button_height, continue_hover)

        menu_button_rect = pygame.Rect(button_x, button_y_menu, button_width, button_height)
        menu_hover = menu_button_rect.collidepoint(pos_mouse)
        draw_button(screen, "Меню", button_x, button_y_menu, button_width, button_height, menu_hover)

        if menu_hover and event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            main_menu = True
            pause = False
            play_music(fon_music)
        if continue_hover and event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            pause_num = 1 - pause_num
            pause = False
            unpause_music()
    elif fl == 1:
        pause = False
        unpause_music()

def game_over_screen(pos_mouse):
    global game_over, main_menu, score, asteroids, fires, main_spaceship_x, main_spaceship_y, game_speed

    overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
    pygame.draw.rect(overlay, (0, 0, 0, 150), (0, 0, WIDTH, HEIGHT))
    screen.blit(overlay, (0, 0))

    game_over_text = font.render("Game Over", True, (255, 0, 0))
    game_over_rect = game_over_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 100))
    screen.blit(game_over_text, game_over_rect)

    restart_button_rect = pygame.Rect(WIDTH // 2 - 150, HEIGHT // 2, 300, 80)
    restart_hover = restart_button_rect.collidepoint(pos_mouse)
    draw_button(screen, "Начать заново", WIDTH // 2 - 250, HEIGHT // 2, 500, 80, restart_hover)

    menu_button_rect = pygame.Rect(WIDTH // 2 - 150, HEIGHT // 2 + 100, 300, 80)
    menu_hover = menu_button_rect.collidepoint(pos_mouse)
    draw_button(screen, "Выйти в меню", WIDTH // 2 - 250, HEIGHT // 2 + 100, 500, 80, menu_hover)

    if restart_hover and event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
        game_over = False
        score = 0
        asteroids.clear()
        fires.clear()
        explosions.clear()
        main_spaceship_x = 490
        main_spaceship_y = 700
        game_speed = 1.0
        play_music(game_music)
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
        play_music(fon_music)

main_menu = True
pause = False
pause_num = 1

fon_y1 = 0
fon_y2 = -HEIGHT

asteroid_spawn_time = 1000
last_asteroid_spawn = pygame.time.get_ticks()

play_music(fon_music)

while True:
    screen.fill((0, 0, 0))

    if fon_spaceship_x == 1530:
        fon_spaceship_x = -400
    else:
        fon_spaceship_x += 0.5

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pause_num = 1 - pause_num
                mause_pos = pygame.mouse.get_pos()
                pause_game(pause_num, mause_pos, event)
            if event.key == pygame.K_SPACE and not pause and not game_over:
                if len(fires) < 2:
                    fires.append(Fire(main_spaceship_x + main_spaceship.get_width() // 2, main_spaceship_y))

    keys = pygame.key.get_pressed()
    if keys[pygame.K_a] and not pause and not game_over:
        if main_spaceship_x > -50:
            main_spaceship_x -= 12
    if keys[pygame.K_d] and not pause and not game_over:
        if main_spaceship_x < 1030:
            main_spaceship_x += 12

    if not pause and not game_over:
        fon_y1 += 6 * game_speed
        fon_y2 += 6 * game_speed

        if fon_y1 >= HEIGHT:
            fon_y1 = -HEIGHT
        if fon_y2 >= HEIGHT:
            fon_y2 = -HEIGHT

        screen.blit(fon_game, (fon_x, fon_y1))
        screen.blit(fon_game, (fon_x, fon_y2))

        screen.blit(main_spaceship, (main_spaceship_x, main_spaceship_y))

        current_time = pygame.time.get_ticks()
        if current_time - last_asteroid_spawn > asteroid_spawn_time:
            asteroids.append(Asteroid())
            last_asteroid_spawn = current_time

        for asteroid in asteroids:
            asteroid.move()
            asteroid.draw(screen)

        for fire in fires:
            fire.move()
            fire.draw(screen)

        asteroids = [asteroid for asteroid in asteroids if not asteroid.is_off_screen()]
        fires = [fire for fire in fires if not fire.is_off_screen()]

        for fire in fires[:]:
            for asteroid in asteroids[:]:
                if fire.rect.colliderect(asteroid.rect):
                    fires.remove(fire)
                    asteroids.remove(asteroid)
                    score += 1
                    explosions.append(Explosion(asteroid.x, asteroid.y))
                    break

        for explosion in explosions[:]:
            explosion.update()
            explosion.draw(screen)
            if explosion.is_finished():
                explosions.remove(explosion)

        ship_rect = main_spaceship.get_rect(topleft=(main_spaceship_x, main_spaceship_y))
        for asteroid in asteroids:
            if ship_rect.colliderect(asteroid.rect):
                game_over = True
                play_music(fon_music)

        if score % 5 == 0 and score > 0:
            game_speed += 0.01
            for asteroid in asteroids:
                if asteroid.speed < MAX_ASTEROID_SPEED:
                    asteroid.speed += 0.1

            if asteroid_spawn_time > 300:
                asteroid_spawn_time -= 50

        score_text = font.render(f"Счет: {score}", True, (255, 255, 255))
        screen.blit(score_text, (10, 10))

    if game_over:
        mause_pos = pygame.mouse.get_pos()
        game_over_screen(mause_pos)

    if main_menu:
        mause_pos = pygame.mouse.get_pos()
        main_menu_func(mause_pos)
    elif pause:
        mause_pos = pygame.mouse.get_pos()
        pause_game(pause_num, mause_pos, event)

    pygame.display.flip()
    clock.tick(60)