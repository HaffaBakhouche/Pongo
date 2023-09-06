#!/usr/bin/python3
import pygame
import color
from obj import left_line , right_line, ball


pygame.init()

screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Pongo! By HaffaBakh")

runs = True
while runs:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runs = False

    pygame.time.delay(1)
    keys = pygame.key.get_pressed()
    screen.fill(color.BLACK)

    # Left line
    if keys[pygame.K_UP] and left_line.y_initial_pos > 0:
        left_line.y_initial_pos -= left_line.velocity
        left_line.y_current_pos -= left_line.velocity

    if keys[pygame.K_DOWN] and left_line.y_initial_pos < 618:
        left_line.y_initial_pos += left_line.velocity
        left_line.y_current_pos += left_line.velocity

    pygame.draw.line(screen,color.WHITE, (left_line.x_initial_pos, left_line.y_initial_pos), (left_line.x_current_pos, left_line.y_current_pos), left_line.obj_width)

    # Right line
    pygame.draw.line(screen,color.WHITE, (right_line.x_initial_pos, right_line.y_initial_pos), (right_line.x_current_pos, right_line.y_current_pos), right_line.obj_width)

    # Ball

    pygame.draw.circle(screen,color.BLUE,(ball.x_initial_pos,ball.y_inital_pos),(ball.radius),ball.width)
    pygame.display.flip()
pygame.quit()
