import pygame
pygame.init()
SIZE = (800, 600)

DISPLAY = pygame.display.set_mode(SIZE)
timer_font = pygame.font.Font("font/animeace2_ital.ttf", 15)
purple = (175, 32, 223)
palegreen = (152, 251, 152)
gameOn = True
start_time = pygame.time.get_ticks()

while gameOn:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameOn = False
    
    timer_num = pygame.time.get_ticks()/1000
    timer_num = "{0:.1f}".format(timer_num)
    timer_str = str(timer_num)
    timer_surface = timer_font.render("Time: " + timer_str, True, purple)
    DISPLAY.fill(palegreen)
    DISPLAY.blit(timer_surface, (20, 20))
    
    pygame.display.update()
