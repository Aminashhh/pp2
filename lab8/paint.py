import pygame

# Функция для рисования прямоугольника
def rect(screen):
    # Определение локальных координат для верхнего левого угла
    x_local, y_local = x, y
    # Вычисление ширины и высоты прямоугольника
    width, height = x2 - x, y2 - y
    # Подстройка локальных координат и размеров, если прямоугольник рисуется справа налево или снизу вверх
    if x2 < x:
        x_local = x2
        width = x - x2
    if y2 < y:
        y_local = y2
        height = y - y2
    # Рисование прямоугольника на экране
    pygame.draw.rect(screen, colors[current_color], (x_local, y_local, width, height), width=3)

# Функция для рисования окружности
def circle(screen):
    # Вычисление радиуса окружности
    radius = ((x2 - x) ** 2 + (y2 - y) ** 2) ** 0.5
    # Рисование окружности на экране
    pygame.draw.circle(screen, colors[current_color], (x, y), radius=int(radius), width=3)

# Функция для стирания
def eraser(screen):
    # Рисование белой окружности для имитации стирания
    pygame.draw.circle(screen_work, (255, 255, 255), (x2, y2), radius=10)

# Инициализация Pygame
pygame.init()

# Установка размеров экрана
screen = pygame.display.set_mode((1200, 800))
screen_work = pygame.Surface(screen.get_size())
instruments = pygame.Surface((295, 50))

# Рисование кнопок для различных режимов рисования и цветов на поверхности инструментов
pygame.draw.rect(instruments, (255, 255, 255), (5, 5, 40, 40), width=3)  # Кнопка для белого цвета
pygame.draw.circle(instruments, (255, 255, 255), (75, 25), radius=20, width=3)  # Кнопка для белого цвета
pygame.draw.rect(instruments, (255, 255, 255), (105, 5, 30, 40), width=0)  # Кнопка для черного цвета
pygame.draw.rect(instruments, (200, 0, 0), (105, 5, 30, 15))  # Кнопка для красного цвета
pygame.draw.rect(instruments, (255, 0, 0), (145, 5, 40, 40))  # Кнопка для красного цвета
pygame.draw.rect(instruments, (0, 255, 0), (195, 5, 40, 40))  # Кнопка для зеленого цвета
pygame.draw.rect(instruments, (0, 0, 255), (245, 5, 40, 40))  # Кнопка для синего цвета

# Словарь для хранения значений цветов
colors = {"red": (255, 0, 0), "green": (0, 255, 0), "blue": (0, 0, 255)}
current_color = 'red'  # Изначальный цвет рисования

# Словарь для хранения режимов рисования
modes = {'rect': rect, 'circle': circle, 'eraser': eraser}
current_mode = 'rect'  # Изначальный режим рисования

clock = pygame.time.Clock()
x, y, x2, y2 = -1, -1, -1, -1

program = True
while program:
    clock.tick(120)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            program = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            # Проверка нажатия кнопок цветов
            if 145 <= x <= 285 and 755 <= y <= 800:
                if x < 190:
                    current_color = 'red'
                elif x < 240:
                    current_color = 'green'
                else:
                    current_color = 'blue'
            # Проверка нажатия кнопок режимов рисования
            elif 0 <= x <= 145 and 755 <= y <= 800:
                if x < 50:
                    current_mode = 'rect'
                elif x < 100:
                    current_mode = 'circle'
                else:
                    current_mode = 'eraser'
            x2, y2 = x, y
        if pygame.mouse.get_pressed()[0]:
            x2, y2 = pygame.mouse.get_pos()
            screen.blit(screen_work, (0, 0))
            modes[current_mode](screen)
            screen.blit(instruments, (0, 750))
            pygame.display.flip()
        if event.type == pygame.MOUSEBUTTONUP:
            modes[current_mode](screen_work)
    screen.blit(instruments, (0, 750))
    pygame.display.flip()





