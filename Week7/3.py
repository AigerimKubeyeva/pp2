import pygame
pygame.init()


screen = pygame.display.set_mode((490, 490))  
running = True


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

clock = pygame.time.Clock()
FPS = 60
color = RED

x = 25
y = 25


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    pressed = pygame.key.get_pressed()

    if pressed[pygame.K_UP]:
        if y >= 45 :
            y -= 20
    if pressed[pygame.K_DOWN]:
        if y <= 450 :
            y += 20
    if pressed[pygame.K_LEFT]:
        if x >= 45 :
            x -= 20
    if pressed[pygame.K_RIGHT]:
        if x <= 455 :
            x += 20

    screen.fill(WHITE)
    pygame.draw.circle(screen, color, (x, y), 25)

    pygame.display.flip()

    clock.tick(FPS)