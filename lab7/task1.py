import pygame
from datetime import datetime as dt

pygame.init()
screen = pygame.display.set_mode((590, 620))
pygame.display.set_caption("mickey mouse watch")
icon = pygame.image.load(r'C:\Users\Huawei\Downloads\photo_5199574004124477086_x.jpg')
pygame.display.set_icon(icon)
suret = pygame.image.load(r'C:\Users\Huawei\Downloads\photo_5199574004124477150_x.jpg')
suret = pygame.transform.scale(suret, (590, 620)) 
suret2 = pygame.image.load(r'C:\Users\Huawei\Downloads\rightarm.png')
suret2 = pygame.transform.scale(suret2, (1000,1430)) 
suret3 = pygame.image.load(r'C:\Users\Huawei\Downloads\leftarm.png')
suret3 = pygame.transform.scale(suret3, (80,630)) 
clock = pygame.time.Clock()

running = True
while running:
    screen.fill((255,255,255))
    screen.blit(suret, (10, 10))

    current_time = dt.now().time()

    seconds_angle = -(current_time.second * 6)
    minutes_angle = -(current_time.minute * 6)

    rotated_leftarm = pygame.transform.rotate(suret3, seconds_angle)
    rotated_rightarm = pygame.transform.rotate(suret2, minutes_angle)

    leftarm_rect = rotated_leftarm.get_rect(center=(293, 305))
    rightarm_rect = rotated_rightarm.get_rect(center=(293, 305))

    screen.blit(rotated_leftarm, leftarm_rect)
    screen.blit(rotated_rightarm, rightarm_rect)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()
    clock.tick(60)

pygame.quit()