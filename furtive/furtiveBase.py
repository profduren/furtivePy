

from os import system, name 
from collections import OrderedDict
from time import sleep, time


class stegoParameters:
    def __init__(self) -> None:
        pass

class furtiveFactory:
    def __init__(self, startRow = 0, startCol = 0) -> None:
        pass

    @staticmethod
    def Open(source, stegoParameters = None, mediaType = ""):     

        if (source.lower().endswith(".bmp")):
            # import the bmp type now that we know we need it
            from furtive.furtiveBitmap import furtiveBmp
            return furtiveBmp(source)
        
        elif (source.lower().endswith(".png")):
            return furtiveBmp()
        else:
            raise Exception("Incompatible image format.")

class furtiveInterface:
    width = 0
    height = 0
    imageType = "unknown"

    def __init__(self, source, startRow = 0, startCol = 0) -> None:
        pass

    def Open(self, source, stegoParameters = None):        
        pass

    def Close(self):        
        pass

    def Hide(self, message):
        pass

    def Reveal(self):
        pass

    def Detect(self):
        pass

    def Analyze(self):
        pass

    def Capacity(self):
        pass
