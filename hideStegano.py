
from stegano import lsb
import sys

messageFile = open(sys.argv[2], "r") 
message = messageFile.read() 
messageFile.close()

secret = lsb.hide(sys.argv[1], message)
secret.save("./Stegano.bmp")
