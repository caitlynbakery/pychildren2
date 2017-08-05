import pygame

SIZE = (800, 600)

DISPLAY = pygame.display.set_mode(SIZE)

mentos = pygame.image.load('img/cupcake.png')
donut = pygame.image.load('img/donut.png')
icecream = pygame.image.load('img/ice-cream.png')
pineapple = pygame.image.load('img/pineapple.png')
pea = pygame.image.load('img/pea.png')
giraffe = pygame.image.load('img/giraffe.png')

white = (255,255,255)
mint = (180,255,229)
gameOn = True

while gameOn:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameOn = False
    DISPLAY.fill(mint)
    DISPLAY.blit(mentos, (346, 235))
    DISPLAY.blit(donut, (131, 465))
    DISPLAY.blit(icecream, (632, 100))
    DISPLAY.blit(pineapple, (160, 115))
    DISPLAY.blit(pea,(456, 532))
    DISPLAY.blit(giraffe,(540, 350))

    pygame.display.update()
