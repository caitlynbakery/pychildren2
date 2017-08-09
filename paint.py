import pygame, sys
import random
pygame.init()
clock = pygame.time.Clock()
size = (600, 800)
screen = pygame.display.set_mode(size)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    p = pygame.mouse.get_pos()
    c1 = random.randrange(20, 255)
    c2 = random.randrange(20, 255)
    c3 = random.randrange(20, 255)
    color = (c1,c2,c3)
    pygame.draw.circle(screen, color, p,10)
    clock.tick(30)
    pygame.display.update() 