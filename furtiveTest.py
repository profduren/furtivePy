from furtive.furtiveBase import furtiveFactory
from furtive.furtiveAnalysis import furtiveAnalysisLsb

testCase1 = furtiveFactory.Open("n00433458_765_resized.png", True)
testCase1.CalculateDigest()

quit()

testCase1 = furtiveFactory.Open("test.bmp", True)
furtiveAnalysisLsb.Playground(testCase1)

messageFile = open("mona.bmp.zip", "rb") 
message = messageFile.read()
messageFile.close()

testCase1.Hide(message)

furtiveAnalysisLsb.Playground(testCase1)


testCase1.SaturateLsbs()
furtiveAnalysisLsb.Playground(testCase1)

testCase1.SaturateLsbs()
furtiveAnalysisLsb.Playground(testCase1)
testCase1.SaturateLsbs()
furtiveAnalysisLsb.Playground(testCase1)
testCase1.Analyze()

revealedMessage = testCase1.Reveal()
messageFile = open("mona-revealed.bmp.zip", "wb") 
messageFile.write(revealedMessage)
messageFile.close()


testCase1.Save("sunsetSmallHidden.bmp")

testCase1.Close()



