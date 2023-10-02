# furtivePy

This is the initial post that created the repo.  The intent is to define a common interface to perform all things Steganography across multiple media types and embedding methods.  We begin with a simple interface definition contained in furtiveBase.py:

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

For each supported media, there is a class factory that returns a class instance that is derived from fertiveInterface and is specific to your media.  See furtiveFactory in furiveBase.py.

Lots more to do!  This is just a starting point!