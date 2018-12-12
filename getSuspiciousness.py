
import os
import time
from pprint import pprint


passDict = {}
failDict = {}
numPassedHits = {}
totalFailed = 1
totalPassed = 1784




def getPassFail():
    allFiles = open("new-output-parse.txt", "r")
    completedFile = 0
    for line in allFiles:
        line = line.strip("\n")
        #print("attempt to open file: ./coverage/coverage_", line, sep = '')
        
        isFailedFile = False
        coverageFile = open("./coverage/coverage_" + line, "r")

        failFile = open("failed-tests.txt", "r")
        for failLine in failFile:
            #print("comparing", failLine, "and", line)
            if line in failLine:
                isFailedFile = True
                #print("found failed file")
                break
        failFile.close()

        for coverageLine in coverageFile:
            openQuoteInd = coverageLine.find("line number=\"") + 13
            if openQuoteInd - 13 > 0:
                closeQuoteInd = coverageLine.find("\"", openQuoteInd)
                lineNum = coverageLine[openQuoteInd : closeQuoteInd]
                numHits = coverageLine[closeQuoteInd + 8 : coverageLine.find("\"", closeQuoteInd + 8)]
                #print("coverageLine:", coverageLine)
                #print("numHits:", numHits)
                #print("openQuoteInd: ", openQuoteInd)
                if int(numHits) > 0:
                    #print("coverageLine:", coverageLine)
                    #print("numHits:", numHits)
                    incrementDict(isFailedFile, lineNum, numHits)
        coverageFile.close()
        completedFile = completedFile + 1
        #print("completed", completedFile, "file(s)")
    allFiles.close()
    failFile.close() 
                        


                
def incrementDict(isFailedFile, lineNum, numHits):            #increment respective dictionary
    lineNum = int(lineNum)
    #print(isFailedFile)
    if isFailedFile:                        
        if lineNum in failDict.keys():
            failDict[lineNum] = failDict[lineNum] + 1
        else:
            failDict[lineNum] = 1
            
    else:
        if lineNum in passDict.keys():
            passDict[lineNum] = passDict[lineNum] + 1
            numPassedHits[lineNum] = numPassedHits[lineNum] + int(numHits)
        else:
            passDict[lineNum] = 1
            numPassedHits[lineNum] = int(numHits)


def createCSV():
    csvFile = open("result.csv", "w")
    csvFile.write("Project,Bug ID,Line Number,Suspiciousness Score\n")
    allKeys = list(passDict.keys()) + list(failDict.keys())
    allKeys.sort()
    for key in allKeys:

        if key in failDict:
            numerator = failDict[key] / totalFailed
        else:
            numerator = 0

        if key in passDict:
            denominator = (passDict[key] / numPassedHits[key]) + numerator
        else:
            denominator = numerator
        
        

        stringToEnter = "Lang,27," + str(key) + "," + str(numerator / denominator)
        csvFile.write(stringToEnter + "\n")

    csvFile.close()






def main():
    getPassFail()
    createCSV()    



if __name__ == "__main__":
    main()
    print("passDict:")
    pprint(passDict)
    print("failDict:")
    pprint(failDict)































