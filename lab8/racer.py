import pygame, sys
from pygame.locals import *
import random, time

# Инициализация Pygame
pygame.init()

# Установка частоты кадров в секунду
FPS = 60
FramePerSec = pygame.time.Clock()

# Определение цветов
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Определение параметров экрана
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600

# Начальные значения скорости, счета и количества монет
SPEED = 5
SCORE = 0
COINS = 0

# Настройка шрифтов
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)

# Загрузка фонового изображения
background = pygame.image.load(r"C:\Users\Huawei\Desktop\AnimatedStreet.png")

# Создание экрана
DISPLAYSURF = pygame.display.set_mode((400, 600))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Racer game")

# Класс монеты
class Coin(pygame.sprite.Sprite):
    
    def __init__(self):
        super().__init__()
        # Загрузка изображения монеты
        self.image = pygame.image.load(r"C:\Users\Huawei\Desktop\coin1.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    # Метод для обработки контакта с игроком
    def contact(self):
        global COINS
        COINS += 1
        self.rect.top = 0
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    # Метод для перемещения монеты
    def move(self):
        self.rect.move_ip(0, SPEED)
        if (self.rect.top > 600):
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

# Класс игрока
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # Загрузка изображения игрока
        self.image = pygame.image.load(r"C:\Users\Huawei\Desktop\Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)

    # Метод для движения игрока
    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 0:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(5, 0)

# Создание игрока и монеты
P1 = Player()
C1 = Coin()

# Создание групп спрайтов
friends = pygame.sprite.Group()
friends.add(C1)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(C1)

# Добавление пользовательского события для увеличения скорости
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

# Главный игровой цикл
while True:
    # Обработка событий
    for event in pygame.event.get():
        if event.type == INC_SPEED:
            SPEED += 0.3
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # Отображение фонового изображения
    DISPLAYSURF.blit(background, (0, 0))

    # Отображение количества монет на экране
    coins = font_small.render(str(COINS), True, BLACK)
    DISPLAYSURF.blit(coins, (360, 10))

    # Перемещение и отображение всех спрайтов
    for entity in all_sprites:
        DISPLAYSURF.blit(entity.image, entity.rect)
        entity.move()

    # Обработка столкновений игрока с монетой
    if pygame.sprite.spritecollideany(P1, friends):
        C1.contact()
        for entity in friends:
            entity.kill()
        C1 = Coin()
        friends.add(C1)
        all_sprites.add(C1)

    # Обновление экрана
    pygame.display.update()
    FramePerSec.tick(FPS)