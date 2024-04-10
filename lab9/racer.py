import pygame
from pygame.locals import *
import random
import time
import sys

# Инициализация Pygame
pygame.init()

# Установка частоты обновления экрана (FPS)
FPS = 60
FramePerSec = pygame.time.Clock()

# Определение цветов
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Размеры экрана
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600

# Начальная скорость, счет и количество монет
SPEED = 5
SCORE = 0
COINS = 0

# Шрифты для отображения текста на экране
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)

# Загрузка фонового изображения
background = pygame.image.load(r"C:\Users\Huawei\Desktop\AnimatedStreet.png")

# Создание окна игры
DISPLAYSURF = pygame.display.set_mode((400, 600))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Game")

# Класс для монет
class Coin(pygame.sprite.Sprite):
    
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(r"C:\Users\Huawei\Desktop\coin1.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    def contact(self):
        global COINS, SPEED
        SPEED += 1
        COINS += 1
        self.rect.top = 0
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)
    
    def move(self):
        self.rect.move_ip(0, SPEED)
        if (self.rect.top > 600):
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

# Класс для больших монет
class Coin_big(pygame.sprite.Sprite):
    
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(r"C:\Users\Huawei\Desktop\coin2.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    def contact(self):
        global COINS, SPEED
        SPEED += 2
        COINS += 1
        self.rect.top = 0
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)
    
    def move(self):
        self.rect.move_ip(0, SPEED)
        if (self.rect.top > 600):
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

# Класс для врагов (препятствий)
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(r"C:\Users\Huawei\Desktop\Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    def move(self):
        global SCORE
        self.rect.move_ip(0, SPEED)
        if (self.rect.top > 600):
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

# Класс для игрока
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(r"C:\Users\Huawei\Desktop\Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)

    def move(self):
        pressed_keys = pygame.key.get_pressed()

        if self.rect.left > 0:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(5, 0)

# Создание объектов игрока, монет, врагов
P1 = Player()
E1 = Enemy()
C1 = Coin()

# Создание групп спрайтов для монет, врагов и всех спрайтов
friends = pygame.sprite.Group()
friends.add(C1)
enemies = pygame.sprite.Group()
enemies.add(E1)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
all_sprites.add(C1)

# Установка таймера для увеличения скорости через определенное время
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

# Основной игровой цикл
while True:
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # Отрисовка фонового изображения
    DISPLAYSURF.blit(background, (0, 0))
    
    # Отрисовка количества монет
    coins = font_small.render(str(COINS), True, BLACK)
    DISPLAYSURF.blit(coins, (360, 10))

    # Обновление позиций и движение всех спрайтов
    for entity in all_sprites:
        DISPLAYSURF.blit(entity.image, entity.rect)
        entity.move()
    
    # Проверка столкновения игрока с монетой
    if pygame.sprite.spritecollideany(P1, friends):
        C1.contact()
        for entity in friends:
            entity.kill()
        C1 = random.choice([Coin, Coin_big])()  # Случайный выбор типа монеты
        friends.add(C1)
        all_sprites.add(C1)

    # Проверка столкновения игрока с врагом (препятствием)
    if pygame.sprite.spritecollideany(P1, enemies):
        pygame.mixer.Sound(r"C:\Users\Huawei\Desktop\crash.wav").play()
        time.sleep(0.5)
        DISPLAYSURF.fill(RED)
        DISPLAYSURF.blit(game_over, (30, 250))
        pygame.display.update()
        for entity in all_sprites:
            entity.kill()
        time.sleep(0.5)
        pygame.quit()
        sys.exit()
    
    pygame.display.update()
    FramePerSec.tick(FPS)