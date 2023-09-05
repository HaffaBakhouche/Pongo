#!/usr/bin/python3
import pygame
import colors

pygame.init()

#lxL
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Pongo!")

# Coordonnées initiales de l'objet
x_initial_pos = 30
y_initial_pos = 500


y_current_pos = 600  # Initialize y_current_pos to the same as y_initial_pos
x_current_pos = 30  # Initialize x_current_pos to a different value for the line

# Dimensions de l'objet
obj_width = 10
# Velocité du rectangle
velocity = 1

runs = True

while runs:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runs = False

    pygame.time.delay(1)
    keys = pygame.key.get_pressed()
    screen.fill(colors.WHITE)
    if keys[pygame.K_UP] and y_initial_pos > 0:
        y_initial_pos -= velocity
        y_current_pos -= velocity

    if keys[pygame.K_DOWN] and y_initial_pos < 618:  # On soustrait un peu à 720 pour que la ligne dessinée reste dans la fenêtre
        y_initial_pos += velocity
        y_current_pos += velocity

    pygame.draw.line(screen,colors.BLACK, (x_initial_pos, y_initial_pos), (x_current_pos, y_current_pos), obj_width)
    pygame.display.flip()

pygame.quit()
