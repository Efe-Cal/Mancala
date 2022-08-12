import pygame
import os
from mangala import Mangala
from tkinter import Tk,messagebox
import event_scheduler
mang=Mangala()
WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode ((WIDTH, HEIGHT))
pygame.display.set_caption("Mangala")
bg = pygame.transform.scale(pygame.image.load(os.path.join("Assets","bg.png")),(900,500))
helpB=pygame.transform.scale(pygame.image.load(os.path.join("Assets","help_button.png")),(50,50))
arrows=pygame.transform.scale(pygame.image.load(os.path.join("Assets","arrows.png")),(150,150))
pygame.init()
font = pygame.font.Font('freesansbold.ttf', 32)

def add_nums2holes(nums=mang.get_data(False)):
    cords=[(150+20,310+20),
           (250+20,310+20),
           (365+20,310+20),
           (475+20,310+20),
           (575+20,310+20),
           (685+20,310+20),
           (800+20,100+20),
           
           (685+20,100+20),
           (575+20,100+20),
           (475+20,100+20),
           (365+20,100+20),
           (250+20,100+20),
           (150+20,100+20),
           (55+20,100+20)]
    for i,j in zip(nums,cords):
        text = font.render(str(i),True,(0,0,0))
        WIN.blit(text,j)

bgl = [bg,(0,0)]
def draw_win_bg(uR=False):
    global bgl
    WIN.fill((0,0,0))
    WIN.blit(bgl[0], bgl[1])
    WIN.blit(helpB,(850,0))
    if bgl==[bg,(0,0)]:add_nums2holes(mang.get_data(uR))
    
    
def button(x:int,y:int,w:int,h:int,pos:tuple):
    global DO_ROT1TIME
    if x+w>pos[0]>x and  y+h>pos[1]>y:
        mx=pos[0]
        if 100<pos[1]<210: # checks if the curser is in the 1st row
            mang.Msgs.append("Rakibinin taşlarını oynayamazsın")
        else: 
            if 150<mx<220:mang.play(0,mang.current_player)
            if 250<mx<320:mang.play(1,mang.current_player)
            if 365<mx<435:mang.play(2,mang.current_player)
            if 475<mx<545:mang.play(3,mang.current_player)
            if 575<mx<645:mang.play(4,mang.current_player)
            if 685<mx<755:mang.play(5,mang.current_player)
        if mang.LAST_STONE_IN_STORE==False:
            show.append(arrows)
            DO_ROT1TIME = True
            

def show_msg():
    for i in mang.Msgs:
        Tk().wm_withdraw()
        messagebox.showinfo("",i)
        mang.Msgs.clear()

def clear(): # removes arrows from sceen by clearing show list
    global show,b
    show.clear()
    b = False
    
def reset_bg():
    global bgl
    bgl = [bg,(0,0)]
rotated=pygame.transform.rotate(pygame.transform.scale(bg,(500,277)),90.0)  
def rotationJob():
    global bgl,show,PAUSE_UPDATING_SCREEN
    PAUSE_UPDATING_SCREEN = False
    #if b == False:
    eventsc.enter(.7,1,clear)
    bgl=[rotated,(312,0)]
    eventsc.enter(.7,2,reset_bg)



def main():
    run = True
    global show,bgl,DO_ROT1TIME,PAUSE_UPDATING_SCREEN,eventsc
    show=[]
    DO_ROT1TIME=False
    PAUSE_UPDATING_SCREEN=False
    eventsc=event_scheduler.EventScheduler()
    eventsc.start()
    while run:
        draw_win_bg()
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                if 900>pos[0]>850 and 50>pos[1]>0:
                    mang.Msgs.append(open("rules.txt","r",encoding="utf-8").read())

                button(150,310,70,110,pos)
                button(250,310,70,110,pos)
                button(365,310,70,110,pos)
                button(475,310,70,110,pos)
                button(575,310,70,110,pos)
                button(685,310,70,110,pos)
        show_msg()
        
        try:
            WIN.blit(show[0],(375,175))
            if DO_ROT1TIME:
                eventsc.enter(1.2,0,rotationJob)
                DO_ROT1TIME=False
                PAUSE_UPDATING_SCREEN=True
                draw_win_bg(True)
                pygame.display.update()
        except IndexError:pass
        
        
        if not PAUSE_UPDATING_SCREEN:pygame.display.update()
    pygame.quit()
    
    
if __name__ == '__main__':
    main()
    eventsc.stop(True)