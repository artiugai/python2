import pygame, sys
from pygame.locals import *
import random, time

pygame.init() # инициализируем pygame

#sprites - граф объекты 
FPS = 60 # устанавливаем кол-во кадров в секунду 
FramePerSec = pygame.time.Clock() #  создает объект для отслеживания времени в игре. 
# он используется для ограничения частоты кадров в игре и
#для обеспечения ее стабильной скорости на всех устройства

# всякие переменные рамер экрана и тд 
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5
SCORE = 0
COINSCORE = 0

# устанавливаем шрифт
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, 'Black')

background = pygame.image.load("AnimatedStreet.png") # добавляем картинку дороги как бг

DISPLAYSURF = pygame.display.set_mode((400, 600)) # создает дисплей окно
DISPLAYSURF.fill('White') 
pygame.display.set_caption("Racer") # задаем название 

#создаем класс Enemy, загружаем картинки, область рандомного спавна
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    def move(self):
        global SCORE
        self.rect.move_ip(0, SPEED)

# если враг вышел за пределы экрана, то обновляем SCORE, устанавливаем врага на начальную позицию

        if (self.rect.top > 600):
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)


class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("coin.png")

        #cоздаем хитбокс такого же размера как и картинка
        self.rect = self.image.get_rect()
        #установка начальной позиции монеты
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    def update(self):
        global COINSCORE
        if self.rect.colliderect(P1.rect):
            COINSCORE += 1
            self.rect.top = 0
            self.generateCoin()
            self.kill()

    def movea(self):
        global SCORE
        self.rect.move_ip(0, SPEED)
        if (self.rect.top > 600):
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    def generateCoin(self):
        all_sprites.add(Coin())


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)

    def move(self):
        pressed_keys = pygame.key.get_pressed()

        if self.rect.left > 0:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(5, 0)

#Setting up Sprites
P1 = Player()
E1 = Enemy()
C1 = Coin()

#Creating Sprites Groups
enemies = pygame.sprite.Group()
enemies.add(E1)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
all_sprites.add(C1)
coins = pygame.sprite.Group()
coins.add(C1)

#Adding a new User event
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

#Game Loop
while True:
    for event in pygame.event.get():
        if event.type == INC_SPEED:
            SPEED += 0.1
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    DISPLAYSURF.blit(background, (0, 0))
    scores = font_small.render(str(SCORE), True, 'Black')
    DISPLAYSURF.blit(background, (0, 0))
    coinscores = font_small.render(str(COINSCORE), True, 'Green')
    DISPLAYSURF.blit(scores, (10, 10))
    DISPLAYSURF.blit(coinscores, (200, 0))

    for entity in all_sprites:
        DISPLAYSURF.blit(entity.image, entity.rect)
        entity.move()
        if isinstance(entity, Coin):
            entity.update()

#To be run if collision occurs between Player and Enemy
    if pygame.sprite.spritecollideany(P1, enemies):
        pygame.mixer.Sound('crash.mp3').play()
        time.sleep(0.5)

        DISPLAYSURF.fill('Red')
        DISPLAYSURF.blit(game_over, (30, 250))

        pygame.display.update()
        for entity in all_sprites:
            entity.kill()
        time.sleep(2)
        pygame.quit()
        sys.exit()

    pygame.display.update()
    FramePerSec.tick(FPS)