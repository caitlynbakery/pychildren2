import pygame
pygame.init()
SIZE = (800, 600)

DISPLAY = pygame.display.set_mode(SIZE)
red = (255,0,0)
gameOn = True
timer_font = pygame.font.Font('font/animeace2_ital.ttf', 15)
while gameOn:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameOn = False
    timer_surface = timer_font.render("time:", False, red)
    DISPLAY.blit(timer_surface, (10,10))
    pygame.display.update()
