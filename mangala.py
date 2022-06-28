class Mangala():
    def __init__(self):
        self.tahta=[[4,4,4,4,4,4,0],[4,4,4,4,4,4,0]]
        self.current_player=0
    def play(self,start_index,player):
        """This is the basic method of game that replace the stones between holes

        Args:
            tahtam (list): the list that holds place of game board
            start_index (int): the index that you played
            player (int): understand which player is playing. Can be 0 or 1

        Returns:nothing
            _type_: _description_
        """
        tahtam=self.tahta
        if start_index!=6 and player==self.current_player and tahtam[player][start_index]!=0:
            addone=0
            if tahtam[player][start_index]==1:addone=1
            for i in range(1,bkts:=tahtam[player][start_index]+addone):
                try:
                    tahtam[player][start_index+i]+=1
                    if i == bkts-1 and tahtam[player][start_index+i]==1 and start_index+bkts-1!=6 and tahtam[0 if player else 1][5-start_index+i]!=0:
                        tahtam[player][6]+=tahtam[player][start_index+i]+tahtam[0 if player else 1][5-start_index+i]
                        tahtam[player][start_index+i],tahtam[0 if player else 1][5-start_index+i]=0,0
                except IndexError:
                    switchedplayer = 0 if player else 1
                    
                    # start_index-bkts
                    (start_index+i)-7
                    tahtam[switchedplayer][(start_index+i)-7]+=1
                    
                    if i == bkts-1:
                        if tahtam[switchedplayer][(start_index+i)-7]%2==0:
                            tahtam[player][6]+=tahtam[switchedplayer][(start_index+i)-7]
                            tahtam[switchedplayer][(start_index+i)-7]=0
                            
            if not tahtam[player][start_index]==1:tahtam[player][start_index]=1
            else:tahtam[player][start_index]=0
            self.tahta=tahtam
            if not start_index+bkts-1==6:self.current_player=0 if self.current_player else 1
        else:pass#show error
    def get_data(self):
        # print(self.tahta[0]+self.tahta[1])
        return self.tahta[0]+self.tahta[1]
        
if __name__=="__main__":
    m=Mangala()
    m.play(5,0)
    # m.play(3,0)
    # m.play(3,0)
    # m.play(3,0)
    # m.play(3,0)
    
    print(m.tahta)