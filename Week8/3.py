import math
import random
import time

import pygame
clock = pygame.time.Clock()
fps = 60  

RED = (255, 0, 0)  # colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
SPEED = 6  # speed of enemy car
SCORE = 0  # player's score

WINDOW_SIZE = WINDOW_WIDTH, WINDOW_HEIGHT = 393, 600  # size of the window
pygame.init()  # initialization
screen = pygame.display.set_mode(WINDOW_SIZE)  # initializing main screen

font = pygame.font.SysFont('Verdana', 63)  # big font
font_small = pygame.font.SysFont('Verdana', 18)  # small font
game_over_text_label = font.render('Game over!', True, WHITE)  # game over label
background = pygame.image.load('street.png')  # background image
pygame.mixer.init()  

pygame.display.set_caption('GAME')  

game_over = False  # game not over condition


class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('coin.png')  # image of coin
        self.rect = self.image.get_rect()  # rectangle of image
        self.set_random_position()  

    def move(self):
        self.rect.move_ip(0, 3)  # it is moving by y-axis with step 3
        if self.rect.top > WINDOW_HEIGHT: 
            self.set_random_position()

    def draw(self, surface):
        surface.blit(self.image, self.rect)  # displaying coin

    def set_random_position(self):
        self.rect.center = (random.randint(65, WINDOW_WIDTH - 65), 0)
        self.rect.bottom = 0  

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('enemy.png')  # image of enemy car
        self.rect = self.image.get_rect()  # rectangle of image
        self.set_random_position()

    def move(self):
        global SPEED, SCORE
        self.rect.move_ip(0, SPEED)  # car is moving by y-axis with some speed

        if self.rect.top > WINDOW_HEIGHT:  # if enemy car reached the bottom of window
            SCORE += 1  # player get point for not collision with enemy car
            self.set_random_position()

    def set_random_position(self):
        self.rect.center = (random.randint(64, WINDOW_WIDTH - 64), 0)
        self.rect.bottom = 0  

    def draw(self, surface):
        surface.blit(self.image, self.rect)  # displaying the enemy car


class Player(pygame.sprite.Sprite):  # Player is moving by x-axis. It can collide with coin or enemy car
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('player.png')  # image of player
        self.rect = self.image.get_rect()  # rectangle of image
        self.rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT - 50)  # initial coordinates of center

    def move(self):
        pressed_keys = pygame.key.get_pressed()  # player moves by x-axis when some keys are pressed

        if self.rect.left > 43:  # possible coordinate by x-axis is limited by yellow line
            if pressed_keys[pygame.K_LEFT]:  # if left arrow touched, car will move to the left direction
                self.rect.move_ip(-5, 0)
        if self.rect.right < WINDOW_WIDTH - 43:
            if pressed_keys[pygame.K_RIGHT]:  # if right arrow touched, car will move to the right direction
                self.rect.move_ip(5, 0)

    def draw(self, surface):
        surface.blit(self.image, self.rect)  # displaying the player


player = Player()  # initializing the object of player class
enemy = Enemy()  # init the object of enemy class
coin = Coin()  # init the object of coin class

all_sprites = pygame.sprite.Group()
all_sprites.add(player)
all_sprites.add(enemy)
all_sprites.add(coin)

enemies = pygame.sprite.Group()  # pygame sprite collide method requires array of elements with which player can collide
enemies.add(enemy)

coins = pygame.sprite.Group()  # also, we need special array of coin sprites
coins.add(coin)

INC_SPEED = pygame.USEREVENT + 1  # increasing speed of enemy car event
pygame.time.set_timer(INC_SPEED, 4000)  # the period of increasing speed is 4s

captured_coins = 0  # variable which keeps number of touched coins


def generated_new_coin():  # generate coin
    global coin
    coin = Coin()  # we create new coin after the player takes previous
    coins.add(coin)
    all_sprites.add(coin)



while not game_over:  # while game is playing
    for event in pygame.event.get():  # events
        if event.type == pygame.QUIT:  # quit
            game_over = True
        if event.type == INC_SPEED:  # increase speed by 0.5
            SPEED += 0.5

    screen.blit(background, (0, 0))  # blitting background image to the window

    screen.blit(
        font_small.render(f'Score: {SCORE}', True, BLUE), (293, 10)
    )  # displaying total score

    screen.blit(
        font_small.render(f'Coins: {captured_coins}', True, BLUE), (293, 30)
    )  # displaying number of touched coins

    for sprite in all_sprites:
        sprite.move()  # moving and displaying all sprites
        sprite.draw(screen)

    if pygame.sprite.spritecollideany(player, coins):  # if player get coin
        coin.kill()  # coin disappear
        captured_coins += 1  # variable of number of touched coins
        SCORE += 1  # for touching a coin player get one point
        generated_new_coin()  # new coin will appear

    if pygame.sprite.spritecollideany(player, enemies):  # collision with enemy car
        pygame.mixer.music.stop()
        pygame.mixer.Sound('crash.wav').play()  # crash music appears
        time.sleep(1)  # wait of 1 second

        screen.fill((69, 172, 116))  # unique green color on a backgroung
        screen.blit(game_over_text_label, (12, 190))  # displaying message that game over
        screen.blit(font_small.render(f'Your score: {SCORE}', True, WHITE), (15, 270))  # display score
        screen.blit(font_small.render(f'Captured coins: {captured_coins}', True, WHITE),
                    (15, 290))  # display number of touched coins

        pygame.display.update()  # updating the screen for showing game over page

        for sprite in all_sprites:
            sprite.kill()  # stopping the game

        time.sleep(7)  # wait for 7 seconds

        game_over = True  # condition of game

    pygame.display.update()  # changing the position of objects
    clock.tick(fps)  # speed of changing the screen

pygame.quit()