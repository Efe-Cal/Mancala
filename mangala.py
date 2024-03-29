class Mangala():
    def __init__(self):
        self.tahta=[[4,4,4,4,4,4,0],[4,4,4,4,4,4,0]]
        self.current_player=0
        self.Msgs=[]
        self.situ=None
    def play(self,start_index:int,player:int):
        """This is the basic method of game that replace the stones between holes

        Args:
            start_index (int): the index that you played
            player (int): understand which player is playing. Can be 0 or 1

        Returns:nothing
            _type_: _description_
        """
        PLAYABLE_HOLE = start_index!=6 and self.tahta[player][start_index]!=0
        CORRECT_PLAYER = player==self.current_player
        # [Following if block] checks if the hole is playable
        if PLAYABLE_HOLE and CORRECT_PLAYER: 
            addone=0
            switchedplayer = 0 if player else 1
            if self.tahta[player][start_index]==1:addone=1
            # [Following for loop] moves the stons
            for i in range(1,bkts:=self.tahta[player][start_index]+addone): 
                self.LAST_STONE = i == bkts-1
                subtract=0
                match a := start_index+i:
                    case a if 7>a>0: 
                        self.tahta[player][start_index+i]+=1
                        # [Following if block] checks if the situation in 3rd rule and enforces the rule
                        REQ_FOR_3RD_RULE=self.tahta[player][start_index+i+subtract]==1 and start_index+i+subtract!=6 and self.tahta[0 if player else 1][5-(start_index+i+subtract)]!=0
                        if self.LAST_STONE and REQ_FOR_3RD_RULE :
                            self.situ="3rdR"
                            self.tahta[player][6] += self.tahta[player][start_index+i+subtract] + self.tahta[0 if player else 1][5-(start_index+i+subtract)]
                            self.tahta[player][start_index+i+subtract]=0
                            self.tahta[0 if player else 1][5-(start_index+i+subtract)]=0
                    case a if 13>a>6:
                        self.tahta[0 if player else 1][(start_index+i)-7]+=1
                        subtract=-7
                        if self.LAST_STONE:
                            # [Following if block] checks if the situation in 2nd rule and enforces the rule
                            if self.tahta[switchedplayer][(start_index+i)+subtract]%2==0:
                                self.situ="2ndR"
                                self.tahta[player][6]+=self.tahta[switchedplayer][(start_index+i)+subtract]
                                self.tahta[switchedplayer][(start_index+i)+subtract]=0
                    case 13:continue
                    case a if 19>a>13:
                        self.tahta[player][(start_index+i)-14]+=1
                        subtract=-14
                        # [Following if block] checks if the situation in 3rd rule and enforces the rule
                        REQ_FOR_3RD_RULE=self.tahta[player][start_index+i+subtract]==1 and start_index+i+subtract!=6 and self.tahta[0 if player else 1][5-(start_index+i+subtract)]!=0
                        if self.LAST_STONE and REQ_FOR_3RD_RULE :
                            self.situ="3rdR"
                            self.tahta[player][6] += self.tahta[player][start_index+i+subtract] + self.tahta[0 if player else 1][5-(start_index+i+subtract)]
                            self.tahta[player][start_index+i+subtract]=0
                            self.tahta[0 if player else 1][5-(start_index+i+subtract)]=0

            
                      
            if not self.tahta[player][start_index]==1:self.tahta[player][start_index]=1
            else:self.tahta[player][start_index]=0
            self.LAST_STONE_IN_STORE=start_index+bkts-1==6
            if not self.LAST_STONE_IN_STORE:self.current_player=0 if self.current_player else 1
            else:self.situ="LSIS"
            # [Following if block] checks win situation
            if self.tahta[0].count(0)==6 or self.tahta[1].count(0)==6:
                switchedplayer = 0 if player else 1
                self.tahta[player][6]+=sum(self.tahta[switchedplayer][:5])
                self.tahta[switchedplayer][:5]=[0]*6
                if self.tahta[0][6]>self.tahta[0][6]:self.Msgs.append("Kazanan Oyuncu 1")
                else:self.Msgs.append("Kazanan Oyuncu 2")
        else:
            if start_index==6:self.Msgs.append("Bu taşlar hareket ettirilemez.")
            if player!=self.current_player:self.Msgs.append("Sıra diğer oyuncuda.")
            if self.tahta[player][start_index]==0:self.Msgs.append("Bu kuyuda hiç taş yok.")
    def get_data(self,undoRotate=False,saveM=False):
        if not undoRotate:
            if not saveM:
                if self.current_player==0:return self.tahta[0]+self.tahta[1]
                else:return self.tahta[1]+self.tahta[0]
            else:return (str(self.tahta[0])+"|"+str(self.tahta[1])+"|"+str(self.current_player)).replace("[","").replace("]","")
        else:
            if self.current_player==1:return self.tahta[0]+self.tahta[1]
            else:return self.tahta[1]+self.tahta[0]
    def load_data(self,string):
        l = string.split("|")
        l[0] = [int(i) for i in l[0].split(",")]
        l[1] = [int(i) for i in l[1].split(",")]
        self.current_player=int(l[2])
        self.tahta=l
        
if __name__=="__main__":
    m=Mangala()
    print(m.get_data(saveM=True))