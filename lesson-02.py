import pygame, sys
from pygame.locals import *

pygame.init()
FPS = 90
clock = pygame.time.Clock()

size = (800, 600)

DISPLAY = pygame.display.set_mode(size)

guffcake = pygame.image.load("img/giraffe.png")
pineapple = pygame.image.load('img/pineapple.png')
pea = pygame.image.load('img/pea.png')
cupcake = pygame.image.load('img/cupcake.png')
donut = pygame.image.load('img/donut.png')
cupcake_rect = pygame.Rect(400, 275, 64,64)
donut_rect = pygame.Rect(600, 275, 64,64)
pineapple_rect = pygame.Rect(500,200,64,64)
pea_rect = pygame.Rect(500,350,64,64)

y = 0
x = 0
gameOn = True
pink = (255,192,203)

direction = "down"

while gameOn:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameOn = False
        if event.type == MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if pineapple_rect.collidepoint(mouse_pos):
                direction = "up"
            if pea_rect.collidepoint(mouse_pos):
                direction = "down"
            if cupcake_rect.collidepoint(mouse_pos):
                direction = "left"
            if donut_rect.collidepoint(mouse_pos):
                direction = "right"
    
    DISPLAY.fill(pink)
    DISPLAY.blit(guffcake, (x,y))
    DISPLAY.blit(pineapple, (500,200))
    DISPLAY.blit(pea, (500,350))
    DISPLAY.blit(cupcake, (400,275))
    DISPLAY.blit(donut, (600, 275))

    if direction == "down":
        y = y+1
    elif direction == "up":
        y = y-1
    elif direction == "left":
        x = x-1
    elif direction == "right":
        x = x+1
    guffcake_rect = pygame.Rect(x,y,64,64)
    if guffcake_rect.bottom > size[1]:
        direction = "up"
    if guffcake_rect.top < 0:
        direction = "down"
    if guffcake_rect.left < 0:
        direction = "right"
    if guffcake_rect.right > 800:
        direction = "left"
    
    

    clock.tick(FPS)
    pygame.display.update()