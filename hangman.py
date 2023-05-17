import os
import pygame
from pygame.locals import *

directory = os.getcwd()
#window
pygame.init()
WIDTH = 800
HEIGHT = 500
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hangman")

#images
images = []
for i in range(7):
    image = pygame.image.load(f"{directory}\\hangman-sprites\\hangman_" + str(i) + ".png")
    images.append(image)

#game variables
hangman_status = 0

#colors
WHITE = (255,255,255)

#game loop
FPS = 60
clock = pygame.time.Clock()
run = True

while run:
    clock.tick(FPS)

    win.fill(WHITE)
    win.blit(images[hangman_status], (150, 100))
    pygame.display.update()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            print(pos)
pygame.quit()