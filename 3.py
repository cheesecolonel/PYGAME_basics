
import pygame
import random

pygame.init()
window_width,window_height=800,600
displayscreen = pygame.display.set_mode((window_width,window_height))
pygame.display.set_caption("movement and collections!")

#SET FPS AND CLOCK
FPS=60
clock=pygame.time.Clock()
#set game values
VELOCITY=5  #速率
BLACK=(0,0,0)

angry_bird=pygame.image.load("angrybird.png")
angry_bird_rect=angry_bird.get_rect()
angry_bird_rect.center=(window_width//2,window_height//2)
#COIN
coin=pygame.image.load("coin.png")
coin_rect=coin.get_rect()
coin_rect.center=(100,100)


running=True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False

    keys=pygame.key.get_pressed() #偵測是否有案件被按下
    if (keys[pygame.K_LEFT] or keys[pygame.K_a])and angry_bird_rect.left>0:
        angry_bird_rect.x -=VELOCITY
    if (keys[pygame.K_RIGHT] or keys[pygame.K_d])and angry_bird_rect.right<window_width:
        angry_bird_rect.x +=VELOCITY
    if (keys[pygame.K_UP] or keys[pygame.K_w])and angry_bird_rect.top>0:
        angry_bird_rect.y -=VELOCITY
    if (keys[pygame.K_DOWN] or keys[pygame.K_s])and angry_bird_rect.bottom<window_height:
        angry_bird_rect.y +=VELOCITY
    if angry_bird_rect.colliderect(coin_rect):
        print("hit")
        coin_rect.x=random.randint(0,window_width-50)
        coin_rect.y=random.randint(0,window_height-50)

    displayscreen.fill(BLACK)
    displayscreen.blit(angry_bird,angry_bird_rect)
    displayscreen.blit(coin,coin_rect)
    pygame.display.update()

    clock.tick(FPS) #FPS
pygame.quit()