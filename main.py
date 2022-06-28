import pygame
import os
from mangala import Mangala
mang=Mangala()
WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode ((WIDTH, HEIGHT))
pygame.display.set_caption("Mangala")
bg = pygame.transform.scale(pygame.image.load(os.path.join("Assets","bg.png")),(900,500))
pygame.init()
font = pygame.font.Font('freesansbold.ttf', 32)
def draw_win_bg():
    WIN.blit(bg, (0, 0))
def button(x,y,w,h,pos):
    pygame.draw.rect(WIN,(0,0,0),(x,y,w,h))
    #(x+(x+w)//2,y+(y+h)//2)
    if x+w>pos[0]>x and  y+h>pos[1]>y:
        mx=pos[0]
        if 100<pos[1]<210:
            print("2st row")
            match mx:
                case mx if 150<mx<220:mang.oyna(5,1)
                case mx if 250<mx<320:mang.oyna(4,1)
                case mx if 365<mx<435:mang.oyna(3,1)
                case mx if 475<mx<545:mang.oyna(2,1)
                case mx if 575<mx<645:mang.oyna(1,1)
                case mx if 685<mx<755:mang.oyna(0,1)
        else:
            print("1nd row")
            match mx:
                case mx if 150<mx<220:mang.oyna(0,0)
                case mx if 250<mx<320:mang.oyna(1,0)
                case mx if 365<mx<435:mang.oyna(2,0)
                case mx if 475<mx<545:mang.oyna(3,0)
                case mx if 575<mx<645:mang.oyna(4,0)
                case mx if 685<mx<755:mang.oyna(5,0)
            
def hole_nums(nums):
    #print(nums)
    cords=[(150,310),
        (250,310),
        (365,310),
        (475,310),
        (575,310),
        (685,310),
        (800,100),
        
        (685,100),
        (575,100),
        (475,100),
        (365,100),
        (250,100),
        (150,100),
        (55,100)
        ]
    for i,j in zip(nums,cords):
        text = font.render(str(i),True,(0,0,0))
        WIN.blit(text,j)

def main():
    run = True
    while run:
        draw_win_bg()
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                print(pos)
                button(150,100,70,110,pos)
                button(250,100,70,110,pos)
                button(365,100,70,110,pos)
                button(475,100,70,110,pos)
                button(575,100,70,110,pos)
                button(685,100,70,110,pos)
                
                button(150,310,70,110,pos)
                button(250,310,70,110,pos)
                button(365,310,70,110,pos)
                button(475,310,70,110,pos)
                button(575,310,70,110,pos)
                button(685,310,70,110,pos) 
        
        hole_nums(mang.get_data())        
        pygame.display.update()
    pygame.quit()
    
if __name__ == '__main__':
    main()