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
    text = TITLE_FONT.render("HANGMAN", 1, BLACK)
    win.blit(text, (WIDTH/2 - text.get_width()/2, 20))
    #draw word
    display_word = ""
    for letter in word:
        if letter in guessed:
            display_word += letter + " "
        else:
            display_word += "_ "
    text = WORD_FONT.render(display_word, 1, BLACK)
    win.blit(text, (350, 200))

    #draw buttons
    for letter in letters:
        x, y, ltr, visible = letter
        if visible:
            pygame.draw.circle(win, BLACK, (x, y), RADIUS, 3)
            text = LETTER_FONT.render(ltr, 1, BLACK)
            win.blit(text, (x-text.get_width()/2, y-text.get_height()/2))

    win.blit(images[hangman_status], (150, 100))
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
            for letter in letters:
                x, y, ltr, visible = letter
                if visible:
                    distance = math.sqrt((x-m_x)**2 + (y-m_y)**2) #distance formula
                    if distance < RADIUS:
                        letter[3]=False #set the 3rd index (boolean) to false. 
                        guessed.append(ltr) #add the letter to the guessed list.
                        if ltr not in word:
                            hangman_status -= 1 #reduce the hangman status by 1.

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