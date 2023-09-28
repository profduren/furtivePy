from furtive.furtiveBase import furtiveFactory




testCase1 = furtiveFactory.Open("test.bmp")

print(type(testCase1))

messageFile = open("mona.bmp", "rb") 
message = messageFile.read()
messageFile.close()

# get stats before embedding
testCase1.Analyze()

testCase1.Hide(message)

testCase1.Save("testHidden.bmp")

testCase1.Analyze()

# get stats after embedding
message = testCase1.Reveal()

revealedMessageFile = open("monaRevealed.bmp", "wb") 
revealedMessageFile.write(message)
revealedMessageFile.close()


testCase1.Close()
