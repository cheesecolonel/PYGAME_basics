# python_game:利用pygame module自製python遊戲

1. **參考資料**:
    1. Pygame homepage: http://pygame.org 
    2. documentation:http://pygame.org/docs/ref
 ------
2. **what is pygame?**
    1. pygame 提供 display,sound,image,text,event 等模組
    2. pygame可製作2d遊戲
    3. pygame偵測使用者鍵盤、搖桿與滑鼠
    4. pygame可提供內建game objects來做遊戲

**_3.pygame basics_**
| name | description |
|:-----:|:----------:|
| _1.py_ | Create game surface , game loop and drawing|
| _2.py_ | Blit text, font, sound and image objects.|
| _3.py_ | Getting keyboard and collection dection

**_4.Code snippet_**
```python
#create game display
window_width,window_height=800,600
displayscreen = pygame.display.set_mode((window_width,window_height))
pygame.display.set_caption("MY FIRST PYGAME !")
```
```python
#blit
pygame.draw.line(displayscreen,WHITE,(0,75),(window_width,75),5)
displayscreen.blit(bird_topleft,bird_topleft_rect)
displayscreen.blit(bird_topright,bird_topright_rect)
displayscreen.blit(show_text_1,show_text_1_rect)
displayscreen.blit(show_text_2,show_text_2_rect)
pygame.display.update()
```

**_5.Game assets_**<br>
[icon archive:](https://iconarchive.com/)網站提供遊戲腳色下載<br>
[leshylabs:](https://www.leshylabs.com/apps/sfMaker/)網站提供音效製作與下載

<img src="https://github.com/cheesecolonel/PYGAME_basics/blob/main/python_pic.png" width="400" height="300" alt="2.py程式截圖><br>
