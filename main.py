import pygame
import os
from mangala import Mangala
from tkinter import Tk,messagebox
mang=Mangala()
WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode ((WIDTH, HEIGHT))
pygame.display.set_caption("Mangala")
bg = pygame.transform.scale(pygame.image.load(os.path.join("Assets","bg.png")),(900,500))
helpB=pygame.transform.scale(pygame.image.load(os.path.join("Assets","help_button.png")),(50,50))
pygame.init()
font = pygame.font.Font('freesansbold.ttf', 32)
def draw_win_bg():
    WIN.blit(bg, (0, 0))
    WIN.blit(helpB,(850,0))
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

def show_msg():
    for i in mang.Msgs:
        Tk().wm_withdraw()
        messagebox.showinfo("",i)
        mang.Msgs.clear()

def main():
    run = True
    while run:
        draw_win_bg()
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                if 900>pos[0]>850 and 50>pos[1]>0:
                    mang.Msgs.append("""1.TEMEL KURAL: Başlama hakkı kazanan oyuncu kendi bölgesinde istediği kuyudan 4 adet taşı
alır. Avucunun içinde rakibinin görebileceği bir şekilde diğer eliyle kuyulara dağıtmaya başlar. Bir adet
taşı aldığı kuyuya bırakıp saatin tersi yönünde, yani sağa doğru her bir kuyuya birer adet taş bırakarak
elindeki taşlar bitene kadar dağıtır. Elindeki son taş hazinesine denk gelirse, oyuncu tekrar oynama
hakkına sahip olur. Oyuncunun kuyusunda tek taş varsa, sırası geldiğinde bu taşı sağındaki kuyuya
taşır. Hamle sırası rakibine geçer. Her seferinde oyuncunun elinde kalan son taş oyunun kaderini
belirler.

2.TEMEL KURAL: Hamle sırası gelen oyuncu kendi kuyusundan aldığı taşları avucunda rakibin
görebileceği bir şekilde diğer eliyle dağıtırken avucunda taş kaldıysa, rakibinin bölgesindeki kuyulara taş
bırakmaya devam eder. Eğer rakibinin kuyularına taş bıraktıktan sonra da elinde taş kaldıysa rakibinin
hazinesine taş bırakmadan kendi bölgesine taş bırakmaya devam eder. Oyuncunun elindeki son taş,
rakibinin bölgesinde denk geldiği kuyudaki taşların sayısını çift sayı yaparsa (2,4,6,8 gibi) oyuncu bu
kuyuda yer alan tüm taşların sahibi olur ve onları kendi hazinesine koyar. Hamle sırası rakibine geçer.

3.TEMEL KURAL: Oyuncu taşları dağıtırken elinde kalan son taş, yine kendi bölgesinde yer alan
boş bir kuyuya denk gelirse ve boş kuyunun karşısındaki kuyuda da rakibine ait taş varsa hem rakibinin
kuyusundaki taşları alır, hem de kendi boş kuyusuna bıraktığı tek taşı alıp hazinesine koyar. Eğer
oyuncunun bölgesinde yer alan boş kuyunun karşısına denk gelen kuyuda rakibinin taşı yoksa oyuncu
kendi boş kuyusuna bıraktığı taşı almaz. Her iki durumda da hamle sırası rakibine geçer.

4.TEMEL KURAL: Oyunculardan herhangi birinin bölgesinde yer alan taşlar bittiğinde oyun seti
biter. Oyunda kendi bölgesinde taşları ilk biten oyuncu, rakibinin bölgesinde bulunan tüm taşları da alıp,
kendi hazinesine koyar.
Oyun seti bittiğinde hakem oyuncuların hazinelerindeki taşları sayar ve en fazla taşı hazinesine
biriktiren oyuncu oyun setini kazanmış olur.""")
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