import pygame 
pygame.init() 

W,H = 450, 450
x,y = W//2, H//2
x1, y1 = 0,0 
RED = (255, 0, 0)
GREEN = (0, 255, 0) 
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
speed=1
sc = pygame.display.set_mode((W,H)) 
pygame.display.set_caption("Snake")
apple = pygame.image.load("apple2.png")
bg = pygame.image.load("bg_snake.jpg") 
sc.blit(bg, (0,0))
sc.blit(apple, (45,45) )
running = True 
FPS=60 
font_style = pygame.font.SysFont(None, 50)
clock = pygame.time.Clock()

def message(msg,color):
   mesg = font_style.render(msg, True, color)
   sc.blit(mesg, [W/2, H/2])

while running: 
    pressed = pygame.key.get_pressed()

    if pressed[pygame.K_UP]:
        if y >= 0 :
            y -=speed
    if pressed[pygame.K_DOWN]:
        if y <= 450 :
            y += speed
    if pressed[pygame.K_LEFT]:
        if x >= 0:
            x -= speed
    if pressed[pygame.K_RIGHT]:
        if x <= 450 :
            x +=speed
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.draw.rect(sc, GREEN, (x,y,20,20))
    pygame.display.update()

    if x>=W or x<0 or y>=W or y<0: #закрываем игру если игрок вышел за границу
        running = False
clock.tick(FPS)
