import pygame

pygame.init()

FPS = 30
clock = pygame.time.Clock()

SIZE = (800, 600)
DISPLAY = pygame.display.set_mode(SIZE)

speed = 8
rightarrow = pygame.image.load("img/arrows/right.png")
giraffe = pygame.image.load('img/giraffe.png')
giraffe_rect = pygame.Rect(0, 0, 64, 64)
rightarrow = pygame.image.load('img/arrows/right.png')
rightarrow_rect = pygame.Rect(680, 400, 100, 55)
larrow = pygame.image.load('img/arrows/left.png')
larrow_rect = pygame.Rect(500, 400, 100, 55)
uarrow = pygame.image.load('img/arrows/up.png')
uarrow_rect = pygame.Rect(610, 300, 55, 100)
darrow = pygame.image.load('img/arrows/down.png')
darrow_rect = pygame.Rect(610, 475, 55, 100)


lavender = (230, 230, 250)


direction = "down"

gameOn = True

while gameOn:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameOn = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if uarrow_rect.collidepoint(mouse_pos):
                direction = "up"
            if darrow_rect.collidepoint(mouse_pos):
                direction = "down"
            if rightarrow_rect.collidepoint(mouse_pos):
                direction = "right"
            if larrow_rect.collidepoint(mouse_pos):
                direction = "left"

    DISPLAY.fill(lavender)
    DISPLAY.blit(giraffe, giraffe_rect)
    DISPLAY.blit(rightarrow, rightarrow_rect)
    DISPLAY.blit(larrow, larrow_rect)
    DISPLAY.blit(uarrow, uarrow_rect)
    DISPLAY.blit(darrow, darrow_rect)

    if direction == "down":
        giraffe_rect.centery += speed
    elif direction == "up":
        giraffe_rect.centery -= speed
    elif direction == "right":
        giraffe_rect.centerx += speed
    elif direction == "left":
        giraffe_rect.centerx -= speed
    if giraffe_rect.bottom > 600:
        direction = "up"
    if giraffe_rect.top < 0:
        direction = "down"
    if giraffe_rect.left < 0:
        direction = "right"
    if giraffe_rect.right > 800:
        direction = "left"


    clock.tick(FPS)
    pygame.display.update()
