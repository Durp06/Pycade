import pygame
import sys
import os
import random

# pygame setup
pygame.init()

window_width = 600
window_height = 500
running = True
dt = 0

screen = pygame.display.set_mode((window_width, window_height))
clock = pygame.time.Clock()
fps = 60
directory = os.getcwd()

#sprites
bg = pygame.image.load(f"{directory}\\flap-sprites\\background.jpg")
pipe = pygame.image.load(f"{directory}\\flap-sprites\\pipe.png")
bird = pygame.image.load(f"{directory}\\flap-sprites\\bird.png")
base = pygame.image.load(f"{directory}\\flap-sprites\\base.png")

pygame.display.set_caption("Flappy Bird")