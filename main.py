#!/usr/bin/python3
import pygame
import color
import random
import sys
from obj import ball, joueurs, opposant

pygame.init()

WIDTH, HEIGHT = 1280, 720
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pongo!")
CLOCK = pygame.time.Clock()
Score_Joueur, Score_Opposant = 0, 0
x_speed, y_speed = 1, 1

runs = True
while runs:
    keys_pressed = pygame.key.get_pressed()
    if keys_pressed[pygame.K_UP]:
        if joueurs.player.top > 0:
            joueurs.player.top -= 2
    if keys_pressed[pygame.K_DOWN]:
        if joueurs.player.bottom < HEIGHT:
            joueurs.player.bottom += 2

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runs = False

    pygame.draw.rect(screen,color.WHITE,joueurs.player)
    pygame.draw.rect(screen,color.WHITE,joueurs.opponent)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
CLOCK.tick(300)
