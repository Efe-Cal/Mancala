class Mangala():
    def __init__(self):
        self.tahta=[[4,4,4,4,4,4,0],[4,4,4,4,4,4,0]]
        self.current_player=0
        self.Msgs=[]
    def play(self,start_index:int,player:int):
        """This is the basic method of game that replace the stones between holes

        Args:
            start_index (int): the index that you played
            player (int): understand which player is playing. Can be 0 or 1

        Returns:nothing
            _type_: _description_
        """
        if start_index!=6 and player==self.current_player and self.tahta[player][start_index]!=0: # checks if the hole is playable
            addone=0
            if self.tahta[player][start_index]==1:addone=1
            for i in range(1,bkts:=self.tahta[player][start_index]+addone): # moves the stons
                try:
                    self.tahta[player][start_index+i]+=1
                    # [Following if block] checks if the situation in 3rd rule and enforces the rule
                    # if bkts>=10
                    if i == bkts-1 and self.tahta[player][start_index+i]==1 and start_index+bkts-1!=6 and self.tahta[0 if player else 1][5-(start_index+i)]!=0:
                        self.tahta[player][6] += self.tahta[player][start_index+i] + self.tahta[0 if player else 1][5-(start_index+i)]
                        self.tahta[player][start_index+i]=0
                        
                        self.tahta[0 if player else 1][5-(start_index+i)]=0
                        # bir tur döndükten sonra eğer boş hazneye gelirse 5-(start_index+i) işe yaramıyor
                except IndexError:
                    switchedplayer = 0 if player else 1

                    self.tahta[switchedplayer][(start_index+i)-7]+=1
                    
                    if i == bkts-1: # checks if the situation in 2nd rule and enforces the rule
                        # bir tur döndükten sonra durum sağlanırsa (start_index+i)-7 işe yaramıyor
                        if self.tahta[switchedplayer][(start_index+i)-7]%2==0:
                            self.tahta[player][6]+=self.tahta[switchedplayer][(start_index+i)-7]
                            self.tahta[switchedplayer][(start_index+i)-7]=0
                            
            if not self.tahta[player][start_index]==1:self.tahta[player][start_index]=1
            else:self.tahta[player][start_index]=0
            if not start_index+bkts-1==6:self.current_player=0 if self.current_player else 1
            # check win situation
            if self.tahta[0].count(0)==6 or self.tahta[1].count(0)==6:
                switchedplayer = 0 if player else 1
                self.tahta[player][6]+=sum(self.tahta[switchedplayer])
                if self.tahta[0][6]>self.tahta[0][6]:self.Msgs.append("Kazanan Oyuncu 1")
                else:self.Msgs.append("Kazanan Oyuncu 2")
        else:
            if start_index==6:self.Msgs.append("Bu taşlar hareket ettirilemez.")
            if player!=self.current_player:self.Msgs.append("Sıra diğer oyuncuda.")
            if self.tahta[player][start_index]==0:self.Msgs.append("Bu kuyuda hiç taş yok.")
    def get_data(self):
        return self.tahta[0]+self.tahta[1]
        
if __name__=="__main__":
    m=Mangala()
    m.play(3,0)
    print(m.tahta)
    m.play(5,0)
    print(m.tahta)
    m.play(2,1)
    print(m.tahta)
    m.play(2,1)
    print(m.tahta)
    m.play(5,0)
    print(m.tahta)
    m.play(2,0)
    print(m.tahta)
    