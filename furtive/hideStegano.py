
import sys
from stegano import lsb

messageFile = open(sys.argv[2], "r") 
message = messageFile.read() 
messageFile.close()

secret = lsb.hide(sys.argv[1], message)
secret.save("./Stegano.bmp")
