import pygame
import os
from mangala import Mangala
mang=Mangala()
WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode ((WIDTH, HEIGHT))
pygame.display.set_caption("Mangala")
bg = pygame.transform.scale(pygame.image.load(os.path.join("Assets","bg.png")),(900,500))
pygame.font.init()
font = pygame.font.Font('freesansbold.ttf', 32)
def draw_win_bg():
    WIN.blit(bg, (0, 0))

def button(x,y,w,h,pos):
    pygame.draw.rect(WIN,(0,0,0),(x,y,w,h))
    #(x+(x+w)//2,y+(y+h)//2)
    if x+w>pos[0]>x and  y+h>pos[1]>y:
        if 100<pos[1]<210:
            print("2st row")
            mx=pos[0]
            match mx:
                case mx if 150<mx<220:mang.oyna(5,1)
                case mx if 250<mx<320:mang.oyna(4,1)
                case mx if 365<mx<435:mang.oyna(3,1)
                case mx if 475<mx<545:mang.oyna(2,1)
                case mx if 575<mx<645:mang.oyna(1,1)
                case mx if 685<mx<755:mang.oyna(0,1)
        else:
            print("1nd row")
            
def hole_nums(num,x,y):
    text = font.render(str(num),True,(0,0,0))
    WIN.blit(text,(x,y))

def main():
    run = True
    while run:
        draw_win_bg()
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
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
        
        hole_nums(4,150,100)
        hole_nums(4,250,100)
        hole_nums(4,365,100)
        hole_nums(4,475,100)
        hole_nums(4,575,100)
        hole_nums(4,685,100)
        
        hole_nums(4,150,310)
        hole_nums(4,250,310)
        hole_nums(4,365,310)
        hole_nums(4,475,310)
        hole_nums(4,575,310)
        hole_nums(4,685,310)
        
        
                
        pygame.display.update()
    pygame.quit()
    
if __name__ == '__main__':
    main()