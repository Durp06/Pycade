import math
import os
import pygame
import random
from pygame.locals import *
import subprocess

directory = os.getcwd()

#window
pygame.init()
WIDTH = 800
HEIGHT = 500
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe")

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
GREEN = (0, 255, 0)

#game loop
FPS = 60
clock = pygame.time.Clock()
run = True
turn_count = -1

class Button:
    def __init__(self, x, y, width, height, color, text):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.text = text

    def drawButton(self, screen):
        # Check if the mouse is hovering over the button
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            # Use a lighter color when the mouse is hovering
            hover_color = tuple(min(c + 0, 200) for c in self.color)
            pygame.draw.rect(screen, hover_color, self.rect)
        else:
            pygame.draw.rect(screen, self.color, self.rect)
        
        font = pygame.font.Font(None, 80)
        text = font.render(str(self.text), True, BLACK)
        text_rect = text.get_rect(center=self.rect.center)
        screen.blit(text, text_rect)

    def setText(self, screen, msg):
        self.text = msg
        font = pygame.font.Font(None, 80)
        text = font.render(str(msg), True, BLACK)
        text_rect = text.get_rect(center=self.rect.center)
        screen.blit(text, text_rect)
    
    def getText(self):
        return self.text
    



#buttons
b_1 = Button(190, 110, 120, 120, WHITE, "")
b_2 = Button(190+120+5, 110, 120, 120, WHITE, "")
b_3 = Button(190+240, 110, 120, 120, WHITE, "")

b_4 = Button(190, 110+120+5, 120, 120, WHITE, "")
b_5 = Button(190+120+5, 110+120+5, 120, 120, WHITE, "")
b_6 = Button(190+240, 110+120+5, 120, 120, WHITE, "")

b_7 = Button(190, 110+240, 120, 120, WHITE, "")
b_8 = Button(190+120+5, 110+240, 120, 120, WHITE, "")
b_9 = Button(190+240, 110+240, 120, 120, WHITE, "")

buttons = [b_1, b_2, b_3, b_4, b_5, b_6, b_7, b_8, b_9]

#example funcs
def start_game():
    print("Starting the game!")

def quit_game():
    print("Quitting the game!")
    pygame.quit()
    

def draw():
    win.fill(WHITE)

    #draw title
    text = TITLE_FONT.render("TIC TAC TOE", 1, BLACK)
    win.blit(text, (WIDTH/2 - text.get_width()/2, 20))

    #draw player turn
    text = WORD_FONT.render("TURN:", 1, BLACK)
    win.blit(text, (600, 155))

    if turn_count == -1:
        text = LETTER_FONT.render("Player 1", 1, BLACK)

    elif turn_count % 2 != 0: #even
        text = LETTER_FONT.render("Player 1", 1, BLACK)
    else:
        text = LETTER_FONT.render("Player 2", 1, BLACK)
    win.blit(text, (610, 230))

    #draw lines
    pygame.draw.rect(win, BLACK, Rect(220, 94, 375, 5)) #underline
    #draw buttons
    for button in buttons:
        button.drawButton(win)
        if button.text:
            button.setText(win, button.text)
    #draw board
    pygame.draw.rect(win, BLACK, Rect(310, 110, 5, 120*3))
    pygame.draw.rect(win, BLACK, Rect(310+120, 110, 5, 120*3))
    pygame.draw.rect(win, BLACK, Rect(310-120, 110+120, 120*3, 5))
    pygame.draw.rect(win, BLACK, Rect(310-120, 110+120*2, 120*3, 5))


    
    pygame.display.update()

def button_clicked(button):
    if button == b_1:
        if not button.text:
            if turn_count % 2 == 0: #even:
                button.setText(win, "X")
            else:
                button.setText(win, "O")
    elif button == b_2:
        if not button.text:
            if turn_count % 2 == 0: #even:
                button.setText(win, "X")
            else:
                button.setText(win, "O")
    elif button == b_3:
        if not button.text:
            if turn_count % 2 == 0: #even:
                button.setText(win, "X")
            else:
                button.setText(win, "O")
    elif button == b_4:
        if not button.text:
            if turn_count % 2 == 0: #even:
                button.setText(win, "X")
            else:
                button.setText(win, "O")
    elif button == b_5:
        if not button.text:
            if turn_count % 2 == 0: #even:
                button.setText(win, "X")
            else:
                button.setText(win, "O")
    elif button == b_6:
        if not button.text:
            if turn_count % 2 == 0: #even:
                button.setText(win, "X")
            else:
                button.setText(win, "O")
    elif button == b_7:
        if not button.text:
            if turn_count % 2 == 0: #even:
                button.setText(win, "X")
            else:
                button.setText(win, "O")
    elif button == b_8:
        if not button.text:
            if turn_count % 2 == 0: #even:
                button.setText(win, "X")
            else:
                button.setText(win, "O")
    elif button == b_9:
        if not button.text:
            if turn_count % 2 == 0: #even:
                button.setText(win, "X")
            else:
                button.setText(win, "O")
    pygame.display.update()


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
                    # Button clicked
                    turn_count += 1
                    print(turn_count)
                    button_clicked(button)
            print(pygame.mouse.get_pos())
            
    #pygame.draw.rect(win, BLACK, Rect(425, 130, 300, 90)) # top right


    draw()


pygame.quit()