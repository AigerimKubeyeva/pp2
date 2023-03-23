import pygame
from datetime import datetime
pygame.init()
W, H = 800, 800
x = W//2
y = H//2
WHITE = (255, 255, 255)
sc = pygame.display.set_mode((W, H))
mickey = pygame.image.load('/Users/a../Desktop/ProgrammingPrinciples2/Week7/main-clock.png')
leftHand = pygame.image.load("left-hand.png")
rightHand = pygame.image.load("right-hand.png")
seconds = pygame.transform.scale(leftHand, (50, 100))
minutes = pygame.transform.scale(rightHand, (30, 60))
mickeyRect = mickey.get_rect()

def blitRotateCenter(surf, image, center, angle):
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center = image.get_rect(center = center).center)
    surf.blit(rotated_image, new_rect)

langle = 0
rangle = 0
done=False
while not done:
    angle = datetime.now().second * 6
    min = datetime.now().minute * 6
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done=True
    langle -= 1
    rangle += 1
    blitRotateCenter(mickey, seconds,  (W/ 2 - 8, H/ 2 + 45), angle)
    blitRotateCenter(mickey, minutes, (W / 2 - 15, H/ 2 + 10), min)
    sc.fill(WHITE)
    sc.blit(mickey, (x, y))
    sc.blit(mickey, mickeyRect)
    
    blitRotateCenter(sc, leftHand, (x,y), langle) 
    blitRotateCenter(sc, rightHand, (x,y), rangle)
    pygame.display.update()