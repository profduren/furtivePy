from os import system, name 
from collections import OrderedDict
from time import sleep, time
from furtive.furtiveBase import furtiveInterface


class furtiveAnalysisInterface(furtiveInterface):


    def GetLsbPairs(self):
        pass



class furtiveAnalysisLsb():

    # just for playing, testing, and debugging!!
    @staticmethod
    def Playground(media: furtiveAnalysisInterface):
        
        lsbPairs = media.GetLsbPairs()

        S = 0
        # calculate S
        for pair in lsbPairs:
            Hk = lsbPairs[pair][0]
            H_k = (lsbPairs[pair][0] + lsbPairs[pair][1]) / 2

            if (H_k) > 4:
                S += pow(Hk - H_k, 2) / H_k

        
        print(S)
        print(S/len(lsbPairs))
