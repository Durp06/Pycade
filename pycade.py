import math
import os
import pygame
import random
from pygame.locals import *
import subprocess

directory = os.getcwd()
hang_file_path = f"{directory}\\hangman.py"
flap_file_path = f"{directory}\\flappy.py"
photo_file_path = f"{directory}\\photobooth.py"
rand_file_path = f"{directory}\\random_1.py"
ttt_file_path = f"{directory}\\tictactoe.py"

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

#colors
WHITE = (255,255,255)
BLACK = (0, 0, 0,)

#game loop
FPS = 60
clock = pygame.time.Clock()
run = True

class Button:
    def __init__(self, x, y, width, height, color, text):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.text = text

    def drawButton(self, screen):
        # Check if the mouse is hovering over the button
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            # Use a lighter color when the mouse is hovering
            hover_color = tuple(min(c + 30, 255) for c in self.color)
            pygame.draw.rect(screen, hover_color, self.rect)
        else:
            pygame.draw.rect(screen, self.color, self.rect)
        
        font = pygame.font.Font(None, 24)
        text = font.render(self.text, True, WHITE)
        text_rect = text.get_rect(center=self.rect.center)
        screen.blit(text, text_rect)

    #draw buttons
    # pygame.draw.rect(win, BLACK, Rect(425, 130, 300, 90)) # top right
    # pygame.draw.rect(win, BLACK, Rect(425, 330, 300, 90), 2) # bottom right
    # pygame.draw.rect(win, BLACK, Rect(80, 130, 300, 90), 2) # top left
    # pygame.draw.rect(win, BLACK, Rect(80 ,330, 300, 90), 2) # bottom left

#buttons
start_button = Button(120, 120, 150, 50, BLACK, "Start")
quit_button = Button(120, 200, 150, 50, BLACK, "Quit")
flappy = Button(425, 130, 300, 90, BLACK, "Flappy Bird") #tr
ttt = Button(700, 10, 90, 90, BLACK, "Tic Tac Toe")
photo = Button(425, 330, 300, 90, BLACK, "Photobooth") #br
hang = Button(80, 130, 300, 90, BLACK, "Hangman") #tl
randomy = Button(80, 330, 300, 90, BLACK, "Random Num Gen") # bl
buttons = [flappy, hang, randomy, photo, ttt]

#example funcs
def start_game():
    print("Starting the game!")

def quit_game():
    print("Quitting the game!")
    pygame.quit()
    

def draw():
    win.fill(WHITE)

    #draw title
    text = TITLE_FONT.render("PYCADE", 1, BLACK)
    win.blit(text, (WIDTH/2 - text.get_width()/2, 20))

    #draw lines
    pygame.draw.rect(win, BLACK, Rect(284, 94, 225, 5)) #underline
    pygame.draw.rect(win, BLACK, Rect(400, 110, 5, 335)) #dividing line

    #draw buttons
    for button in buttons:
        button.drawButton(win)
    
    pygame.display.update()

def button_clicked(button):
    if button == hang:
        subprocess.run(["python", hang_file_path])
    elif button == flappy:
        subprocess.run(["python", flap_file_path])
    elif button == randomy:
        subprocess.run(["python", rand_file_path])
    elif button == photo:
        subprocess.run(["python", photo_file_path])
    elif button == ttt:
        subprocess.run(["python", ttt_file_path])
#buttons = [flappy, hang, randomy, photo]


def display_message(message):
    pygame.time.delay(1200) #wait 1 second
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
            pos = pygame.mouse.get_pos()
            for button in buttons:
                if button.rect.collidepoint(pos):
                    # Button clicked! Call a function or perform an action.
                    button_clicked(button)
            #print(pygame.mouse.get_pos())
            
    #pygame.draw.rect(win, BLACK, Rect(425, 130, 300, 90)) # top right


    draw()


pygame.quit()