#!/usr/bin/python3
import pygame

pygame.init()

screen = pygame.display.set_mode((1280,720), 0, 32)
pygame.display.set_caption("S4 Reborned")

# Coordonnées initiales de l'objet
x_current_pos = 225
y_current_pos = 225

# Dimensions de l'objet
obj_width = 20
obj_height = 20
# Velocité du rectangle
velocity = 1
# Image de fond + mise en place de l'icone
bg = pygame.image.load("icon/bg.png")
icon = pygame.image.load("icon/icon.png")
pygame.display.set_icon(icon)
runs = True
while runs:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runs = False
    keys = pygame.key.get_pressed()
    screen.fill((0,0,0))
    screen.blit(bg,(0,0))

    pygame.time.delay(1)

    if keys[pygame.K_LEFT] and x_current_pos > 0:
        x_current_pos -= velocity
    if keys[pygame.K_RIGHT] and x_current_pos < 1280 - obj_width:
        x_current_pos += velocity

    if keys[pygame.K_UP] and y_current_pos > 0:
        y_current_pos -= velocity
    if keys[pygame.K_DOWN] and y_current_pos < 720 - obj_height:
        y_current_pos += velocity

    pygame.draw.rect(screen, (0, 0, 255), (x_current_pos, y_current_pos, obj_width, obj_height))
    pygame.display.flip()

pygame.quit()
