import pygame
from datetime import datetime
pygame.init()
W, H = 800, 800
x = W//2
y = H//2
WHITE = (255, 255, 255)
screen = pygame.display.set_mode((W, H))
mickey = pygame.image.load('/Users/a../Desktop/ProgrammingPrinciples2/Week7/main-clock.png')
leftHand = pygame.image.load("left-hand.png")
rightHand = pygame.image.load("right-hand.png")

def blitRotateCenter(surf, image, topleft, angle):
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center=image.get_rect(topleft=topleft).center)
    surf.blit(rotated_image, new_rect)

clock = pygame.time.Clock()
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done=True
    screen.fill(WHITE)
    screen.blit(mickey, (0, 0))
    time = datetime.now()
    minute = time.minute
    second = time.second
    blitRotateCenter(screen, leftHand, (140, 340), ((second % 60) / 60) * -360)
    blitRotateCenter(screen, rightHand, (205, 325), ((minute % 60) / 60) * -(360 -120))
    
    pygame.display.update()
clock.tick(60)
    
    
