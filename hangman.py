import math
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

#button vars
RADIUS = 20
GAP = 20
letters = []
startx = round((WIDTH - (RADIUS * 2 + GAP) * 13) / 2)
starty = 370
A = 65
for i in range (26): # will add coordinates of letters to the array
    x = startx + GAP * 2 + ((RADIUS * 2 + GAP ) * (i % 13)) # says off of edge of screen | distance between buttons and the gap | simulates having 2 rows / remainder will count up normally intil its >13 and then it will re count back from 0 in the "second row"
    y = starty + ((i // 13) * (GAP + 25) + RADIUS * 2 ) # uses int division to ust give a num without decimal
    letters.append([x, y, chr(A+i), True]) # x coord, y coord, letter, if button has been clicked

#font
LETTER_FONT = pygame.font.SysFont("comicsans", 30)

#images
images = []
for i in range(7):
    image = pygame.image.load(f"{directory}\\hangman-sprites\\hangman_" + str(i) + ".png")
    images.append(image)

#game variables
hangman_status = 0

#colors
WHITE = (255,255,255)
BLACK = (0, 0, 0,)

#game loop
FPS = 60
clock = pygame.time.Clock()
run = True

def draw():
    win.fill(WHITE)

    #draw buttons
    for letter in letters:
        x, y, ltr, visible = letter
        if visible:
            pygame.draw.circle(win, BLACK, (x, y), RADIUS, 3)
            text = LETTER_FONT.render(ltr, 1, BLACK)
            win.blit(text, (x-text.get_width()/2, y-text.get_height()/2))

    win.blit(images[hangman_status], (150, 100))
    pygame.display.update()

while run:
    clock.tick(FPS)

    draw()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            m_x, m_y = pygame.mouse.get_pos()
            for letter in letters:
                x, y, ltr, visible = letter
                if visible:
                    distance = math.sqrt((x-m_x)**2 + (y-m_y)**2) #distance formula
                    if distance < RADIUS:
                        letter[3]=False #set the 3rd index (boolean) to false. 
pygame.quit()