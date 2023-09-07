import pygame

# Données du joueur
WIDTH, HEIGHT = 1280, 720

player = pygame.Rect(0, 0, 10, 100)
player.center = (WIDTH-100, HEIGHT/2)

# Données de l'opposant
opponent = pygame.Rect(0, 0, 10, 100)
opponent.center = (100, HEIGHT/2)