class Mangala():
    def __init__(self):
        self.tahta=[0,4,4,4,4,4,4,0,4,4,4,4,4,4]
    def oyna(self,tahtam,start_index):
        """This is the basic method of game that replace the stones between holes

        Args:
            tahtam (list): the list that holds plase of game board
            start_index (int): the index that you played

        Returns:nothing
            _type_: _description_
        """
        if start_index!=0 and start_index!=7:
            for i in range(1,tahtam[start_index]):
                tahtam[start_index+i]+=1
            tahtam[start_index]=1
            self.tahta=tahtam
        else:pass#show error
    # tahta=[0,4,4,4,4,4,4,0,4,4,4,4,4,4]
    # tahta = oyna(tahta,3)
    # print(tahta)