class Mangala():
    def __init__(self):
        self.tahta=[[4,4,4,4,4,4,0],[4,4,4,4,4,4,0]]
    def oyna(self,start_index,player):
        """
        This is the basic method of game that replace the stones between holes and 
        when situation in 2nd and 3rd rules occures runs the rules.

        Args:
            start_index (int): the index that you played
            player (int): understand which player is playing. Can be 0 or 1

        """
        tahtam=self.tahta
        if start_index!=6:
            addone=0
            if tahtam[player][start_index]==1:addone=1
            for i in range(1,bkts:=tahtam[player][start_index]+addone):
                try:
                    tahtam[player][start_index+i]+=1
                    if i == bkts-1 and tahtam[player][start_index+i]==1:
                        tahtam[player][6]+=tahtam[player][start_index+i]+tahtam[0 if player else 1][5-start_index+i]
                        tahtam[player][start_index+i],tahtam[0 if player else 1][5-start_index+i]=0,0
                except IndexError:
                    switchedplayer = 0 if player else 1
                    
                    # start_index-bkts
                    tahtam[switchedplayer][i-bkts+3]+=1
                    
                    if i == bkts-1:
                        if tahtam[switchedplayer][i-bkts+3]%2==0:
                            tahtam[player][6]+=tahtam[switchedplayer][i-bkts+3]
                            tahtam[switchedplayer][i-bkts+3]=0
                            
            if not tahtam[player][start_index]==1:tahtam[player][start_index]=1
            else:tahtam[player][start_index]=0
            self.tahta=tahtam
        else:pass#show error

    def send_data(self):
        """
        Creates the data for flask template
        """
        data= {}
        l = self.tahta[0]+self.tahta[1]
        for a,i in enumerate(l):
            data["hole"+str(a)]=i
        return data
if __name__=="__main__":
    masa = Mangala()
    masa.oyna(3,0)
    print(masa.tahta)