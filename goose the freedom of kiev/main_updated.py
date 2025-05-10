import pygame
import sys
import random
import os
from pygame.constants import QUIT, K_DOWN, K_UP, K_LEFT, K_RIGHT

pygame.init()

story_lines = [
        "Коли темні хмари нависли над Києвом і вороги заполонили небо,",
        "простий гусак на ім’я Шусак з лівого берега став на захист свободи.",
        "",
        "Він був не просто птахом — він бачив несправедливість, чув крики людей,",
        "і коли ворог намагався стерти культуру, мову й дух столиці —",
        "Шусак розправив крила.",
        "",
        "Озброєний хоробрістю, гумором та відром сміливості,",
        "він вирушає у свою найважливішу місію:",
        "",
        "Звільнити Київ. І знищити Капітана Зрадокрила.",
        "",
        "Натисни будь-яку клавішу, щоб продовжити..."
    ]

HEIGHT = 800
WIDTH = 1200
FONT = pygame.font.SysFont('Verdana', 20)
BIG_FONT = pygame.font.SysFont("arial", 40)

COLOR_WHITE = (255, 255, 255)
COLOR_BLACK = (0, 0, 0)
COLOR_LIGHT = (200, 200, 200)
COLOR_DARK = (100, 100, 100)
COLOR_VICTORY = (200, 255, 200)
COLOR_DEFEAT = (255, 200, 200)

main_display = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Гусь за свободу Київа")
pygame.display.set_icon(pygame.image.load('icon.png'))
background = pygame.image.load("bg.png")
background = pygame.transform.scale(background, (WIDTH, HEIGHT))
main_display.blit(background, (0, 0))

pygame.mixer.init()
pygame.mixer.music.load('background_music.mp3')
pygame.mixer.music.set_volume(0.1)
pygame.mixer.music.play(-1)

clock = pygame.time.Clock()
bg = pygame.transform.scale(pygame.image.load('background.png'), (WIDTH, HEIGHT))
bg_X1 = 0
bg_X2 = bg.get_width()
bg_move = 3
IMAGE_PATH = "Goose"
PLAYER_IMAGES = os.listdir(IMAGE_PATH)

def draw_button(text, x, y, w, h, active):
    color = COLOR_DARK if active else COLOR_LIGHT
    pygame.draw.rect(main_display, color, (x, y, w, h))
    label = BIG_FONT.render(text, True, COLOR_BLACK)
    main_display.blit(label, (x + (w - label.get_width()) // 2, y + (h - label.get_height()) // 2))

def show_victory_ending():
    pygame.mixer.music.stop()
    pygame.mixer.music.load('victory_music.wav')
    pygame.mixer.music.play()

    lines = [
        "Тепер все зло знищено.",
        "Шусак вирішив піти на пенсію",
        "та жити спокійним життям.",
        "",
        "Кінець.",
        "Натисни будь-яку клавішу, щоб повернутись у меню."
    ]
    waiting = True
    while waiting:
        main_display.fill(COLOR_VICTORY)
        for i, line in enumerate(lines):
            label = FONT.render(line, True, COLOR_BLACK)
            main_display.blit(label, (WIDTH // 2 - label.get_width() // 2, 150 + i * 40))
        for event in pygame.event.get():
            if event.type == pygame.QUIT: pygame.quit(); sys.exit()
            if event.type == pygame.KEYDOWN: waiting = False
        pygame.display.flip()
        clock.tick(60)

    pygame.mixer.music.stop()
    pygame.mixer.music.load('background_music.mp3')
    pygame.mixer.music.play(-1)
    main_menu()

def show_defeat_ending():
    pygame.mixer.music.stop()
    pygame.mixer.music.load('defeeat_music.wav')
    pygame.mixer.music.play()

    lines = [
        "Після перемоги над Шусаком,",
        "Зрадокрил став головним у Києві",
        "та створив власну армію.",
        "",
        "Ніхто вже не сміє йому перечити...",
        "",
        "Натисни будь-яку клавішу, щоб повернутись у меню."
    ]
    waiting = True
    while waiting:
        main_display.fill(COLOR_DEFEAT)
        for i, line in enumerate(lines):
            label = FONT.render(line, True, COLOR_BLACK)
            main_display.blit(label, (WIDTH // 2 - label.get_width() // 2, 150 + i * 40))
        for event in pygame.event.get():
            if event.type == pygame.QUIT: pygame.quit(); sys.exit()
            if event.type == pygame.KEYDOWN: waiting = False
        pygame.display.flip()
        clock.tick(60)

    pygame.mixer.music.stop()
    pygame.mixer.music.load('background_music.mp3')
    pygame.mixer.music.play(-1)

pygame.init()

HEIGHT = 800
WIDTH = 1200
FONT = pygame.font.SysFont('Verdana', 20)
BIG_FONT = pygame.font.SysFont("arial", 40)

COLOR_WHITE = (255, 255, 255)
COLOR_BLACK = (0, 0, 0)
COLOR_LIGHT = (200, 200, 200)
COLOR_DARK = (100, 100, 100)

main_display = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Гусь за свободу Київа")
pygame.display.set_icon(pygame.image.load('icon.png'))
background = pygame.image.load("bg.png")
background = pygame.transform.scale(background, (WIDTH, HEIGHT))
main_display.blit(background, (0, 0))

pygame.mixer.init()
pygame.mixer.music.load('background_music.mp3')
pygame.mixer.music.set_volume(0.1)
pygame.mixer.music.play(-1)

clock = pygame.time.Clock()
bg = pygame.transform.scale(pygame.image.load('background.png'), (WIDTH, HEIGHT)) 
bg_X1 = 0
bg_X2 = bg.get_width()
bg_move = 3
IMAGE_PATH = "Goose"
PLAYER_IMAGES = os.listdir(IMAGE_PATH)

def draw_button(text, x, y, w, h, active):
    color = COLOR_DARK if active else COLOR_LIGHT
    pygame.draw.rect(main_display, color, (x, y, w, h))
    label = BIG_FONT.render(text, True, COLOR_BLACK)
    main_display.blit(label, (x + (w - label.get_width()) // 2, y + (h - label.get_height()) // 2))

def show_rules():
    waiting = True
    rules_lines = [
        "Правила гри:",
        "- Керуй гусаком стрілками на клавіатурі.",
        "- Уникай ворогів (літаки).",
        "- Збирай бонуси, щоб отримати очки.",
        "- Набери 10 очок, щоб зустрітись із босом.",
        "- Натискай 'Пробіл', щоб стріляти в бою з босом.",
        "",
        "Натисни будь-яку клавішу, щоб повернутись до меню."
    ]

    bg_image = pygame.image.load("bg.png")
    bg_image = pygame.transform.scale(bg_image, (WIDTH, HEIGHT))

    while waiting:
        main_display.blit(bg_image, (0, 0))
        overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
        overlay.fill((255, 255, 255, 200))
        main_display.blit(overlay, (0, 0))

        for i, line in enumerate(rules_lines):
            label = FONT.render(line, True, COLOR_BLACK)
            main_display.blit(label, (WIDTH // 2 - label.get_width() // 2, 100 + i * 35))

        for event in pygame.event.get():
            if event.type == pygame.QUIT: pygame.quit(); sys.exit()
            if event.type == pygame.KEYDOWN: waiting = False

        pygame.display.flip()
        clock.tick(60)

def show_message_png():
    message_img = pygame.image.load("message.png")
    message_img = pygame.transform.scale(message_img, (600, 200))
    rect = message_img.get_rect(center=(WIDTH // 2, HEIGHT // 2))

    waiting = True
    while waiting:
        main_display.blit(background, (0, 0))
        main_display.blit(message_img, rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT: pygame.quit(); sys.exit()
            if event.type == pygame.KEYDOWN: waiting = False

        pygame.display.flip()
        clock.tick(60)


    
    waiting = True
    while waiting:
        main_display.fill(COLOR_WHITE)
        for i, line in enumerate(story_lines):
            label = FONT.render(line, True, COLOR_BLACK)
            main_display.blit(label, (WIDTH//2 - label.get_width()//2, 100 + i * 40))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                waiting = False
        pygame.display.flip()
        clock.tick(60)

pygame.init()

HEIGHT = 800
WIDTH = 1200
FONT = pygame.font.SysFont('Verdana', 20)
BIG_FONT = pygame.font.SysFont("arial", 40)

COLOR_WHITE = (255, 255, 255)
COLOR_BLACK = (0, 0, 0)
COLOR_LIGHT = (200, 200, 200)
COLOR_DARK = (100, 100, 100)

main_display = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Гусь за свободу Київа")
pygame.display.set_icon(pygame.image.load('icon.png'))
background = pygame.image.load("bg.png")
background = pygame.transform.scale(background, (WIDTH, HEIGHT))
main_display.blit(background, (0, 0))

pygame.mixer.init()
pygame.mixer.music.load('background_music.mp3')
pygame.mixer.music.set_volume(0.1)
pygame.mixer.music.play(-1)

clock = pygame.time.Clock()
bg = pygame.transform.scale(pygame.image.load('background.png'), (WIDTH, HEIGHT)) 
bg_X1 = 0
bg_X2 = bg.get_width()
bg_move = 3
IMAGE_PATH = "Goose"
PLAYER_IMAGES = os.listdir(IMAGE_PATH)

def draw_button(text, x, y, w, h, active):
    color = COLOR_DARK if active else COLOR_LIGHT
    pygame.draw.rect(main_display, color, (x, y, w, h))
    label = BIG_FONT.render(text, True, COLOR_BLACK)
    main_display.blit(label, (x + (w - label.get_width()) // 2, y + (h - label.get_height()) // 2))

def show_intro():
    story_lines = [
        "Коли темні хмари нависли над Києвом і вороги заполонили небо,",
        "простий гусак на ім’я Шусак з лівого берега став на захист свободи.",
        "",
        "Він був не просто птахом — він бачив несправедливість, чув крики людей,",
        "і коли ворог намагався стерти культуру, мову й дух столиці —",
        "Шусак розправив крила.",
        "",
        "Озброєний хоробрістю, гумором та відром сміливості,",
        "він вирушає у свою найважливішу місію:",
        "",
        "Звільнити Київ. І знищити Капітана Зрадокрила.",
        "",
        "Натисни будь-яку клавішу, щоб продовжити..."
    ]
    waiting = True
    while waiting:
        main_display.fill(COLOR_WHITE)
        for i, line in enumerate(story_lines):
            label = FONT.render(line, True, COLOR_BLACK)
            main_display.blit(label, (WIDTH//2 - label.get_width()//2, 100 + i * 40))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                waiting = False
        pygame.display.flip()
        clock.tick(60)

def boss_dialogue():
    dialogue = [
        "Капітан Зрадокрил: ...Шусак?",
        "Шусак: Так, це я. Ми знову зустрілись.",
        "Зрадокрил: Я думав, тебе знищили в лабораторії.",
        "Шусак: Мене — ні. Але ти зрадив усе, за що ми боролись.",
        "Зрадокрил: Я став сильнішим. Я став генералом.",
        "Шусак: Ти став монстром.",
        "Зрадокрил: Мені шкода, друже... Але я не зупинюсь.",
        "Шусак: Тоді я зупиню тебе сам. За Київ!",
        "",
        "Натисни будь-яку клавішу, щоб почати битву!"
    ]
    waiting = True
    while waiting:
        main_display.fill(COLOR_WHITE)
        for i, line in enumerate(dialogue):
            label = FONT.render(line, True, COLOR_BLACK)
            main_display.blit(label, (WIDTH//2 - label.get_width()//2, 100 + i * 40))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                waiting = False
        pygame.display.flip()
        clock.tick(60)

def boss_battle():
    boss_dialogue()

    boss = pygame.transform.scale(pygame.image.load('boss.png'), (150, 150)).convert_alpha()
    boss_rect = boss.get_rect(center=(WIDTH - 200, HEIGHT // 2))
    boss_health = 50
    lives = 3
    bullets, boss_bullets, big_attacks = [], [], []
    player_rect = pygame.Rect(15, HEIGHT // 2, 80, 45)
    player_speed = 5
    boss_direction = 2
    BOSS_HIT_SOUND = pygame.mixer.Sound("boss_hit.wav")

    player_anim_index = 0
    player_anim_timer = pygame.USEREVENT + 6
    pygame.time.set_timer(player_anim_timer, 100)

    pygame.time.set_timer(pygame.USEREVENT + 4, 1000)
    pygame.time.set_timer(pygame.USEREVENT + 5, 3000)

    running = True
    while running:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                bullets.append(pygame.Rect(player_rect.right, player_rect.centery - 5, 10, 5))
            if event.type == pygame.USEREVENT + 4:
                boss_bullets.append(pygame.Rect(boss_rect.left, boss_rect.centery, 8, 8))
            if event.type == pygame.USEREVENT + 5:
                big_attacks.append(pygame.Rect(boss_rect.left, boss_rect.centery, 14, 14))
            if event.type == player_anim_timer:
                player_anim_index = (player_anim_index + 1) % len(PLAYER_IMAGES)

        keys = pygame.key.get_pressed()
        if keys[K_DOWN] and player_rect.bottom < HEIGHT:
            player_rect.y += player_speed
        if keys[K_UP] and player_rect.top > 0:
            player_rect.y -= player_speed
        if keys[K_LEFT] and player_rect.left > 0:
            player_rect.x -= player_speed
        if keys[K_RIGHT] and player_rect.right < WIDTH:
            player_rect.x += player_speed

        boss_rect.y += boss_direction * 3
        if boss_rect.top <= 50 or boss_rect.bottom >= HEIGHT - 50:
            boss_direction *= -1

        for bullet in bullets[:]:
            bullet.x += 10
            if bullet.colliderect(boss_rect):
                bullets.remove(bullet)
                boss_health -= 1
                BOSS_HIT_SOUND.play()

        for proj in boss_bullets[:]:
            proj.x -= 8
            if proj.colliderect(player_rect):
                boss_bullets.remove(proj)
                lives -= 1

        for big in big_attacks[:]:
            big.x -= 6
            if big.colliderect(player_rect):
                big_attacks.remove(big)
                lives -= 3

        if boss_health <= 0:
            show_victory_ending()
            return
        elif lives <= 0:
            show_defeat_ending()
            return

        bullets = [b for b in bullets if b.x < WIDTH]
        boss_bullets = [b for b in boss_bullets if b.x > 0]
        big_attacks = [b for b in big_attacks if b.x > 0]

        main_display.blit(bg, (0, 0))
        player_img = pygame.image.load(os.path.join(IMAGE_PATH, PLAYER_IMAGES[player_anim_index]))
        player_img = pygame.transform.scale(player_img, (80, 45)).convert_alpha()
        main_display.blit(player_img, player_rect)
        main_display.blit(boss, boss_rect)

        for b in bullets:
            pygame.draw.rect(main_display, (255, 0, 0), b)
        for b in boss_bullets:
            pygame.draw.rect(main_display, (0, 0, 255), b)
        for b in big_attacks:
            pygame.draw.rect(main_display, (0, 0, 0), b)

        main_display.blit(FONT.render(f"Здоров'я боса: {boss_health}", True, COLOR_BLACK), (50, 20))
        main_display.blit(FONT.render(f"Життя: {lives}", True, COLOR_BLACK), (WIDTH - 150, 20))
        pygame.display.flip() 

def game_loop():
    global bg_X1, bg_X2
    player = pygame.transform.scale(pygame.image.load('player.png'), (80, 45)).convert_alpha()
    player_rect = player.get_rect(x=15, y=(HEIGHT / 2))
    player_move_down = [0, 4]
    player_move_right = [4, 0]
    player_move_up = [0, -4]
    player_move_left = [-4, 0]
    lives = 1
    CREATE_ENEMY = pygame.USEREVENT + 1
    pygame.time.set_timer(CREATE_ENEMY, 1500)
    CREATE_BONUS = pygame.USEREVENT + 2
    pygame.time.set_timer(CREATE_BONUS, 2000)
    CHANGE_IMAGE = pygame.USEREVENT + 3
    pygame.time.set_timer(CHANGE_IMAGE, 200)

    def create_enemy():
        enemy = pygame.transform.scale(pygame.image.load('enemy.png'), (70, 50)).convert_alpha()
        rect = pygame.Rect(WIDTH - 70, random.randint(50, HEIGHT - 50), 70, 50)
        return [enemy, rect, [random.randint(-8, -4), 0]]

    def create_bonus():
        bonus = pygame.transform.scale(pygame.image.load('bonus.png'), (70, 100)).convert_alpha()
        rect = pygame.Rect(random.randint(100, WIDTH - 100), 0, 70, 100)
        return [bonus, rect, [0, random.randint(4, 8)]]

    enemies, bonuses = [], []
    score = 0
    image_index = 0
    playing = True

    while playing:
        clock.tick(120)
        for event in pygame.event.get():
            if event.type == QUIT: pygame.quit(); sys.exit()
            if event.type == CREATE_ENEMY: enemies.append(create_enemy())
            if event.type == CREATE_BONUS: bonuses.append(create_bonus())
            if event.type == CHANGE_IMAGE:
                player = pygame.image.load(os.path.join(IMAGE_PATH, PLAYER_IMAGES[image_index]))
                image_index = (image_index + 1) % len(PLAYER_IMAGES)

        keys = pygame.key.get_pressed()
        if keys[K_DOWN] and player_rect.bottom < HEIGHT: player_rect = player_rect.move(player_move_down)
        if keys[K_RIGHT] and player_rect.right < WIDTH: player_rect = player_rect.move(player_move_right)
        if keys[K_UP] and player_rect.top >= 0: player_rect = player_rect.move(player_move_up)
        if keys[K_LEFT] and player_rect.left >= 0: player_rect = player_rect.move(player_move_left)

        main_display.blit(bg, (bg_X1, 0))
        main_display.blit(bg, (bg_X2, 0))
        bg_X1 -= bg_move; bg_X2 -= bg_move
        if bg_X1 < -bg.get_width(): bg_X1 = bg.get_width()
        if bg_X2 < -bg.get_width(): bg_X2 = bg.get_width()

        for enemy in enemies:
            enemy[1] = enemy[1].move(enemy[2])
            main_display.blit(enemy[0], enemy[1])
            if player_rect.colliderect(enemy[1]):
                lives -= 1
                if lives <= 0: playing = False

        for bonus in bonuses:
            bonus[1] = bonus[1].move(bonus[2])
            main_display.blit(bonus[0], bonus[1])
            if player_rect.colliderect(bonus[1]):
                score += 1
                bonuses.remove(bonus)

        bonuses = [b for b in bonuses if b[1].top <= HEIGHT]
        enemies = [e for e in enemies if e[1].left > 0]
        main_display.blit(FONT.render(f"Очки: {score}", True, COLOR_BLACK), (WIDTH - 120, 20))
        main_display.blit(player, player_rect)
        pygame.display.flip()
        if score >= 10:
            playing = False
            boss_battle()

def main_menu():
    while True:
        main_display.blit(background, (0, 0))
        title_text = BIG_FONT.render("Гусь за свободу Київа", True, COLOR_BLACK)
        main_display.blit(title_text, (WIDTH // 2 - title_text.get_width() // 2, 100))

        mx, my = pygame.mouse.get_pos()
        start_btn = pygame.Rect(500, 300, 200, 50)
        rules_btn = pygame.Rect(500, 400, 200, 50)
        quit_btn = pygame.Rect(500, 500, 200, 50)

        draw_button("Старт гри", *start_btn.topleft, *start_btn.size, start_btn.collidepoint(mx, my))
        draw_button("Правила", *rules_btn.topleft, *rules_btn.size, rules_btn.collidepoint(mx, my))
        draw_button("Вихід", *quit_btn.topleft, *quit_btn.size, quit_btn.collidepoint(mx, my))

        for event in pygame.event.get():
            if event.type == pygame.QUIT: pygame.quit(); sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if start_btn.collidepoint(event.pos): show_intro(); game_loop()
                elif rules_btn.collidepoint(event.pos): show_rules()
                elif quit_btn.collidepoint(event.pos): pygame.quit(); sys.exit()

        pygame.display.flip()
        clock.tick(60)

main_menu()
