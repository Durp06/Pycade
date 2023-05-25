import math
import os
import pygame
import random
from pygame.locals import *

directory = os.getcwd()
#window
pygame.init()
WIDTH = 800
HEIGHT = 500
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pycade")

#button vars
RADIUS = 20
GAP = 20
letters = []
startx = round((WIDTH - (RADIUS * 2 + GAP) * 13) / 2)
starty = 370
A = 65
for i in range (26): 
    x = startx + GAP * 2 + ((RADIUS * 2 + GAP ) * (i % 13)) 
    y = starty + ((i // 13) * (GAP + 25) + RADIUS * 2 ) 
    letters.append([x, y, chr(A+i), True]) 

#font
LETTER_FONT = pygame.font.SysFont("comicsans", 30)
WORD_FONT = pygame.font.SysFont("comicsans", 50)
TITLE_FONT = pygame.font.SysFont("comicsans", 60)

#images
images = []
for i in range(7):
    image = pygame.image.load(f"{directory}\\hangman-sprites\\hangman_" + str(i) + ".png")
    images.append(image)

#game variables
hangman_status = 6
words = ["VSCODE", "IGKNIGHTER", "PYTHON", "JAVA", "MAXWELL", "SCIENCE", 
    "ROBOTICS", "CODE", "ECLIPSE", "BUNNY", "DISCORD", "SCORPION", "CAT", 
    "DOG", "PARROT", "MONKEY", "BANNANA", "TECH", "GERMAN", "AMERICAN", 
    "TANK", "BRITISH", "INDIAN", "ITALIAN", "CUBAN", "SYSTEM", "JEWISH", 
    "CHRISTIAN", "GAY", "TRANS", "BI", "COPE", "MADDOX", "CHUCK"]
word = random.choice(words)
guessed = []

#colors
WHITE = (255,255,255)
BLACK = (0, 0, 0,)

#game loop
FPS = 60
clock = pygame.time.Clock()
run = True

def draw():
    win.fill(WHITE)

    #draw title
    text = TITLE_FONT.render("PYCADE", 1, BLACK)
    win.blit(text, (WIDTH/2 - text.get_width()/2, 20))


    #draw buttons
    pygame.draw.rect(win, BLACK, Rect(284, 94, 225, 5))
    pygame.draw.rect(win, BLACK, Rect(400, 110, 5, 335))
    pygame.draw.rect(win, BLACK, Rect(425, 130, 300, 90), 2)
    pygame.draw.rect(win, BLACK, Rect(425, 330, 300, 90), 2)
    pygame.draw.rect(win, BLACK, Rect(80, 130, 300, 90), 2)
    pygame.draw.rect(win, BLACK, Rect(80 ,330, 300, 90), 2)

    
    pygame.display.update()


def display_message(message):
    pygame.time.delay(1000) #wait 1 second
    win.fill(WHITE) #fill screen with blank white
    text = WORD_FONT.render(message, 1, BLACK) #render param 'message' 
    win.blit(text, (WIDTH/2 - text.get_width()/2, HEIGHT/2 - text.get_height()/2)) # blit/put text in middle of screen
    pygame.display.update() #update screen
    pygame.time.delay(3000) #wait 3 seconds
        

while run:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            m_x, m_y = pygame.mouse.get_pos()
            print(pygame.mouse.get_pos())
            for letter in letters:
                x, y, ltr, visible = letter
                if visible:
                    distance = math.sqrt((x-m_x)**2 + (y-m_y)**2) #distance formula
                    if distance < RADIUS:
                        letter[3]=False #set the 3rd index (boolean) to false. 
                        

    draw()

    won = True
    for letter in word:
        if letter not in guessed:
            won = False
            break
    
    if won:
        display_message("You Won!")
        break

    if hangman_status == 0:
        display_message("nope")
        break

pygame.quit()