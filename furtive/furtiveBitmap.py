import os
import numpy as np
import png, array
import sys
from os import system, name 
from collections import OrderedDict
from time import sleep, time
from furtive.furtiveBase import furtiveInterface

''' 3rd Party Library '''
from PIL import Image

class furtiveBmp(furtiveInterface):
    def __init__(self, srcImage, startRow=0, startCol=0):
        super().__init__(srcImage, startRow, startCol)
        self.img    = Image.open(srcImage)
        self.width  = self.img.width
        self.height = self.img.height
        self.Pix    = self.img.load()
        self.imageType = "bmp"
        self._counter = 0

    def Close(self):  
        self.img.close()      

    def Analyze(self, analysisType = "none"):  
        integerRepresentation = 0
        integerSizeInBits = 8
        bitPos = 0
        lsbBytes = bytearray()

        for x in range(self.width):
            for y in range(self.height):
                pixel = self.Pix[x,y]

                for colorVal in pixel:

                    if (bitPos == 0):
                        #print(str(integerRepresentation))
                        lsbBytes.append(integerRepresentation)
                        bitPos = integerSizeInBits - 1
                        integerRepresentation = 0
                
                    integerRepresentation += (colorVal & 0b00000001) << bitPos
                    bitPos -= 1

        d = lsbBytes


        import matplotlib.pyplot as plt

        # An "interface" to matplotlib.axes.Axes.hist() method
        n, bins, patches = plt.hist(x=d, bins='auto', color='#0504aa',
                                    alpha=0.7, rwidth=0.85)
        plt.grid(axis='y', alpha=0.75)
        plt.xlabel('Value')
        plt.ylabel('Frequency')
        plt.title('My Very Own Histogram')
        plt.text(23, 45, r'$\mu=15, b=3$')
        maxfreq = n.max()
        # Set a clean upper y-axis limit.
        plt.ylim(ymax=np.ceil(maxfreq / 10) * 10 if maxfreq % 10 else maxfreq + 10)
        plt.savefig('plot' + str(self._counter) + '.png')
        self._counter += 1

    def Reveal(self):

        message = bytearray()
        msgLengthBytes = [0,0,0,0]
        i = 0
        self._currentRow = 0
        self._currentCol = 0
        self._colorIndex = 0
        # TODO: make sure there is room for our message
        for lenByte in msgLengthBytes:
            value = self._RevealByte()
            msgLengthBytes[i] = value
            i += 1

        messageLength = int.from_bytes(msgLengthBytes, "little")

        print(messageLength)

        for i in range(messageLength):
            message.append(self._RevealByte())

        print(len(message))

        return message
    
    def Hide(self, message):

        self._currentRow = 0
        self._currentCol = 0
        self._colorIndex = 0

        # get the length of the message
        msgLen = len(message)

        # TODO: make sure there is room for our message
        for lenByte in msgLen.to_bytes(4, "little"):
            self._HideByte(lenByte)

        # hide the message
        for byteToHide in message:
            self._HideByte(byteToHide)

    def _HideByte(self, value):         
         for i in range(7,-1,-1):

             if (self._currentCol >= self.width):
                 self._currentRow += 1
                 self._currentCol = 0
                 if (self._currentRow >= self.height):
                     self._colorIndex += 1
                     if (self._colorIndex > 2):
                         #TODO throw exception, out of room
                         pass

             bitToHide = value >> i
             bitToHide &= 0x01

             currentPix = self.Pix[self._currentCol, self._currentRow]

             
             curColorVal = currentPix[self._colorIndex] 

             if bitToHide == 1:                 
                 newColorValue = curColorVal | 0x01
             else:
                 newColorValue = curColorVal & 0xFE
                 
             newPix = [currentPix[0], currentPix[1], currentPix[2]]

             newPix[self._colorIndex] = newColorValue

             newPixTuple = (newPix[0], newPix[1], newPix[2])

             self.Pix[self._currentCol, self._currentRow, ] = newPixTuple

             # move to the next column
             self._currentCol += 1
             
    def _RevealByte(self):     
         value = 0    
         for i in range(7,-1,-1):

             if (self._currentCol >= self.width):
                 self._currentRow += 1
                 self._currentCol = 0
                 if (self._currentRow >= self.height):
                     self._colorIndex += 1
                     if (self._colorIndex > 2):
                         #TODO throw exception, out of room
                         pass

             currentPix = self.Pix[self._currentCol, self._currentRow]
             
             curColorVal = currentPix[self._colorIndex] 

             if (curColorVal & 0x01):
                 value += 0x01 << i

             # move to the next column
             self._currentCol += 1

         return value
    
    def Save(self, filename):
        # Save this as a new image
        try:
            self.img.save(filename)
            return True
        except Exception as err:
            print("Error Saving Image: "+str(err))
            return False

