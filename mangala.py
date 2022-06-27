class Mangala():
    def __init__(self):
        self.tahta=[[4,4,4,4,4,3,0],[0,4,4,4,4,4,4,0]]
    def oyna(self,start_index,player):
        """This is the basic method of game that replace the stones between holes

        Args:
            tahtam (list): the list that holds place of game board
            start_index (int): the index that you played
            player (int): understand which player is playing. Can be 0 or 1

        Returns:nothing
            _type_: _description_
        """
        tahtam=self.tahta
        if start_index!=0:
            for i in range(1,bkts:=tahtam[player][start_index]):
                try:
                    tahtam[player][start_index+i]+=1
                except IndexError:
                    a= 0 if player else 1
                    
                    start_index-bkts
                    tahtam[a][i-bkts+3]+=1
                    
                    
                    if i == bkts-1:
                        if tahtam[a][i-bkts+3]%2==0:
                            tahtam[player][6]+=tahtam[a][i-bkts+3]
                            tahtam[a][i-bkts+3]=0
                            
                            
            tahtam[player][start_index]=1
            self.tahta=tahtam
        else:pass#show error
    # tahta=[0,4,4,4,4,4,4,0,4,4,4,4,4,4]
    # tahta = oyna(tahta,3)
    # print(tahta)
    
masa = Mangala()
masa.oyna(5,0)
masa.oyna(4,0)
print(masa.tahta)