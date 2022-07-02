
import pygame

pygame.init()
window_width,window_height=800,600
displayscreen = pygame.display.set_mode((window_width,window_height))
pygame.display.set_caption("blitting image!")

bird_topleft=pygame.image.load("angrybird.png")
bird_topleft_rect=bird_topleft.get_rect()#得知圖案大小
bird_topleft_rect.topleft=(0,0)#圖案出現位置

bird_topright=pygame.image.load("angrybird.png")
bird_topright_rect=bird_topright.get_rect()
bird_topright_rect.topright=(window_width,0)

#播放音效
sound_1=pygame.mixer.Sound("sound_1.wav")
sound_2=pygame.mixer.Sound("sound_2.wav")
sound_1.play()
pygame.time.delay(2000)#延遲兩秒
sound_2.play()
pygame.time.delay(2000)
sound_2.set_volume(1.0)
sound_2.play()

#背景音
pygame.mixer.music.load("music.wav")#從頭重複撥放
pygame.mixer.music.play(-1,0.0)
pygame.time.delay(10000)
pygame.mixer.music.stop()

running=True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False

    WHITE=(255,255,255)
    GREEN=(0,255,0)
    DARKGREEN=(10,50,10)
    #fonts=pygame.font.get_fonts()查看所有pygame的字形

    system_font=pygame.font.SysFont("century",64)
    custom_font=pygame.font.Font("AbstractGroovy.ttf",50)#載入外部字形

    show_text_1=system_font.render("Angry bird game:",True,GREEN)
    show_text_1_rect=show_text_1.get_rect()
    show_text_1_rect_center=(window_width//2,30)
    
    show_text_2=custom_font.render("move angry bird soon",True,GREEN)
    show_text_2_rect=show_text_2.get_rect()
    show_text_2_rect.center=(window_width//2,window_height//2+100)

    pygame.draw.line(displayscreen,WHITE,(0,75),(window_width,75),5)
    displayscreen.blit(bird_topleft,bird_topleft_rect)
    displayscreen.blit(bird_topright,bird_topright_rect)
    displayscreen.blit(show_text_1,show_text_1_rect)
    displayscreen.blit(show_text_2,show_text_2_rect)
    pygame.display.update()
pygame.quit()