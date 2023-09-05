#!/usr/bin/python3
import pygame

pygame.init()

screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("S4 Reborned")

# Coordonnées initiales de l'objet
x_initial_pos = 30
y_initial_pos = 500
x_current_pos = 30
y_current_pos = 500

# Dimensions de l'objet
obj_width = 5
# Velocité du rectangle
velocity = 10
# Image de fond + mise en place de l'icone
icon = pygame.image.load("icon/icon.png")
pygame.display.set_icon(icon)

runs = True

while runs:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runs = False
    keys = pygame.key.get_pressed()
    screen.fill((0, 0, 0))

    if keys[pygame.K_UP] and y_current_pos > 0:
        y_current_pos -= velocity
        if y_current_pos < 0:
            y_current_pos = 0

    if keys[pygame.K_DOWN] and y_current_pos < 720:
        y_current_pos += velocity
        if y_current_pos > 720:
            y_current_pos = 720

    pygame.draw.line(screen, (248, 248, 255), (x_initial_pos, y_initial_pos), (x_current_pos, y_current_pos), obj_width)
    pygame.display.flip()

pygame.quit()
