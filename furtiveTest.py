from furtive.furtiveBase import furtiveFactory


testCase1 = furtiveFactory.Open("test.bmp")

print(type(testCase1))

#testCase1.Analyze()

messageFile = open("mona.bmp.zip", "rb") 
message = messageFile.read()
messageFile.close()

testCase1.Hide(message)

testCase1.Analyze()

revealedMessage = testCase1.Reveal()
messageFile = open("mona-revealed.bmp.zip", "wb") 
messageFile.write(revealedMessage)
messageFile.close()


testCase1.Save("sunsetSmallHidden.bmp")

testCase1.Close()



