import pygame
import os
from mangala2 import Mangala
from tkinter import Tk,messagebox
mang=Mangala()
WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode ((WIDTH, HEIGHT))
pygame.display.set_caption("Mangala")
bg = pygame.transform.scale(pygame.image.load(os.path.join("Assets","bg.png")),(900,500))
pygame.init()
font = pygame.font.Font('freesansbold.ttf', 32)
def draw_win_bg():
    WIN.blit(bg, (0, 0))
def button(x:int,y:int,w:int,h:int,pos:tuple):
    if x+w>pos[0]>x and  y+h>pos[1]>y:
        mx=pos[0]
        if 100<pos[1]<210: # checks if the curser is in the 1st row
            match mx: # finds curser is on which hole
                case mx if 150<mx<220:mang.play(5,1)
                case mx if 250<mx<320:mang.play(4,1)
                case mx if 365<mx<435:mang.play(3,1)
                case mx if 475<mx<545:mang.play(2,1)
                case mx if 575<mx<645:mang.play(1,1)
                case mx if 685<mx<755:mang.play(0,1)
        else:
            match mx:
                case mx if 150<mx<220:mang.play(0,0)
                case mx if 250<mx<320:mang.play(1,0)
                case mx if 365<mx<435:mang.play(2,0)
                case mx if 475<mx<545:mang.play(3,0)
                case mx if 575<mx<645:mang.play(4,0)
                case mx if 685<mx<755:mang.play(5,0)
            
def add_nums2holes(nums=mang.get_data()):
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
        (55,100)]
    for i,j in zip(nums,cords):
        text = font.render(str(i),True,(0,0,0))
        WIN.blit(text,j)
# class timer():
#     def __init__(self,sec):
#         self.st=pygame.time.get_ticks()
#         self.sec=sec
#     def check(self):
#         if (pygame.time.get_ticks()-self.st)/1000>=self.sec:return True
#         else:return False
def show_msg():
    # text = font.render("AAAAAAAA",True,(0,0,0))
    # WIN.blit(text,(0,0))
    # pygame.display.update()
    # pygame.event.pump()
    # pygame.time.wait(3000)
    for i in mang.Msgs:
        Tk().wm_withdraw()
        messagebox.showinfo("",i)
        mang.Msgs.clear()
    
    # t = timer(3)
    # if t.check()!=True:
    #     pygame.time.wait(1)
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
                
        add_nums2holes(mang.get_data())
        show_msg()
        pygame.display.update()
    pygame.quit()
    
if __name__ == '__main__':
    main()