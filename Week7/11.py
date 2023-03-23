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

    '''def blitRotate(surf, image, pos, originPos, angle):
    # offset from pivot to center
    image_rect = image.get_rect(topleft=(pos[0] - originPos[0], pos[1] - originPos[1]))
    offset_center_to_pivot = pygame.math.Vector2(pos) - image_rect.center

    # roatated offset from pivot to center
    rotated_offset = offset_center_to_pivot.rotate(angle)

    # roatetd image center
    rotated_image_center = (pos[0] - rotated_offset.x, pos[1] - rotated_offset.y)

    # get a rotated image
    rotated_image = pygame.transform.rotate(image, -angle)
    rotated_image_rect = rotated_image.get_rect(center=rotated_image_center)

    # rotate and blit the image
    surf.blit(rotated_image, rotated_image_rect)


seconds = pygame.image.load('images/big.png')
minutes = pygame.image.load('images/small.png')
seconds = pygame.transform.scale(seconds, (50, 100))
minutes = pygame.transform.scale(minutes, (30, 60))

bg = pygame.image.load('images/mickey-clock.jpg')
w, h = seconds.get_size()

done = False
while not done:
    angle = datetime.now().second * 6
    min = datetime.now().minute * 6
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    pos = (screen.get_width() / 2, screen.get_height() / 2)
    screen.blit(bg, (0, 0))
    blitRotate(screen, seconds, pos, (w / 2 - 8, h / 2 + 45), angle)
    blitRotate(screen, minutes, pos, (w / 2 - 15, h / 2 + 10), min)

    # pygame.draw.circle(screen, (0, 255, 0), pos, 7, 0)

    pygame.display.flip()
'''