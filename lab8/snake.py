import pygame
from random import randrange

# Установка разрешения экрана и размера клетки
RES = 800
SIZE = 50

# Начальная позиция змейки и яблока
x, y = randrange(0, RES, SIZE), randrange(0, RES, SIZE)
apple = randrange(0, RES, SIZE), randrange(0, RES, SIZE)

# Начальные параметры змейки: направление движения, длина, массив координат
dirs = {'W': True, 'S': True, 'A': True, 'D': True}
length = 1
snake = [(x, y)]
dx, dy = 0, 0

# Начальные значения счета и FPS (скорости игры)
score = 0
fps = 5

# Инициализация Pygame
pygame.init()
screen = pygame.display.set_mode((RES, RES))
pygame.display.set_caption("Snake")
clock = pygame.time.Clock()

# Настройка шрифтов для отображения счета и конечного сообщения
font_score = pygame.font.SysFont('Times New Roman', 26, bold=True)
font_end = pygame.font.SysFont('Times New Roman', 66, bold=True)

running = True
while running:
    
    # Очистка экрана
    screen.fill(pygame.Color('black'))
    
    # Отрисовка змейки и яблока
    [(pygame.draw.rect(screen, pygame.Color('green'), (i, j, SIZE - 2, SIZE - 2))) for i, j in snake]
    pygame.draw.rect(screen, pygame.Color('red'), (*apple, SIZE, SIZE))
    
    # Отрисовка счета
    render_score = font_score.render(f'SCORE: {score}', 1, pygame.Color('orange'))
    screen.blit(render_score, (5, 5))
    
    # Обновление координат змейки и добавление новой головы
    x += dx * SIZE
    y += dy * SIZE
    snake.append((x, y))
    snake = snake[-length:]
    
    # Обработка съедания яблока
    if snake[-1] == apple:
        apple = randrange(0, RES, SIZE), randrange(0, RES, SIZE)
        length += 1
        score += 1
        fps += 1
        
    # Обработка окончания игры при столкновении с границами экрана или самой собой
    if x < 0 or x > RES - SIZE or y < 0 or y > RES - SIZE or len(snake) != len(set(snake)):
        render_end = font_end.render('GAME OVER', 1, pygame.Color('orange'))
        screen.blit(render_end, (RES // 2 - 200, RES // 3))
        pygame.display.flip() 
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit() 
                    exit()
    
    # Обновление экрана и управление FPS
    pygame.display.flip()
    pygame.display.update()
    clock.tick(fps)
    
    # Обработка событий клавиатуры
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
            
    key = pygame.key.get_pressed()
    if key[pygame.K_w] and dirs['W']:
        dx, dy = 0, -1
        dirs = {'W': True, 'S': False, 'A': True, 'D': True}
    if key[pygame.K_s] and dirs['S']:
        dx, dy = 0, 1
        dirs = {'W': False, 'S': True, 'A': True, 'D': True}
    if key[pygame.K_a] and dirs['A']:
        dx, dy = -1, 0
        dirs = {'W': True, 'S': True, 'A': True, 'D': False}
    if key[pygame.K_d] and dirs['D']:
        dx, dy = 1, 0
        dirs = {'W': True, 'S': True, 'A': False, 'D': True}




