import pygame

pygame.init()

clock = pygame.time.Clock()

SIZE = (800, 600)

DISPLAY = pygame.display.set_mode(SIZE)

gameOn = True

while gameOn:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameOn = False
    print(pygame.time.get_ticks())
    pygame.display.update()
