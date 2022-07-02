
from tkinter.tix import WINDOW
import pygame#載入遊戲模組
pygame.init()#遊戲模組啟動

window_width,window_height=800,600
displayscreen = pygame.display.set_mode((window_width,window_height))
pygame.display.set_caption("MY FIRST PYGAME !")

#定義顏色:
BLACK =(0,0,0)
WHITE =(255,255,255)
RED   =(255,0,0)
GREEN =(0,255,0)
BLUE  =(0,0,255)
YELLOW=(255,255,0)
CYAN  =(0,255,255)
MEG   =(255,0,255)
GRAY  =(192,192,192)
displayscreen.fill(YELLOW)#填滿背景色
#pygame.draw.line(畫布名稱,顏色,end,厚度)
pygame.draw.line(displayscreen,RED,(0,window_height//2),(window_width,window_height//2),5)
pygame.draw.line(displayscreen,RED,(window_width//2,0),(window_width//2,window_height),5)

#pygame.draw.circle(畫布名稱,顏色,中心點,半徑,厚度) 厚度=0會填滿圓
pygame.draw.circle(displayscreen,BLACK,(window_width//2,window_height//2),200,6)
pygame.draw.circle(displayscreen,WHITE,(window_width//2,window_height//2),180,0)

#pygame.draw.rect(名稱,顏色,(topleft-x,toFleft-y,width,height),thickness)
pygame.draw.rect(displayscreen,BLUE,(0,0,window_width,100),0)

running=True
while running:
    for event in pygame.event.get():#抓取遊戲中所有的事件
        if event.type==pygame.QUIT:#如果事件是關閉遊戲:
            running=False

    pygame.display.update()#畫布更新

pygame.quit()#遊戲模組結束
