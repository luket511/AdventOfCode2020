from commonFunctions import reader, generateStructure, printDict
from Day_10a import formatInput
INPUT = "input10.csv"
KNOWN_PATH_NUMBERS = {}


def getInRange(target,inpList):
    output = []
    for i in inpList:
        if i in [target+1,target+2,target+3]:
            output.append(i)
    return output

def findNumArrangements(currentNode):    
    if currentNode.hasNoChildren():
        KNOWN_PATH_NUMBERS[currentNode.getValue()] = 1
        return 1
    else:
        sum = 0
        for child in currentNode.getChildNodes():
            try:
                sum += KNOWN_PATH_NUMBERS[child.getValue()]
            except KeyError:
                sum += findNumArrangements(child)
        KNOWN_PATH_NUMBERS[currentNode.getValue()] = sum
        return sum
        

if __name__ == "__main__":
    steps = formatInput(INPUT)
    nodeMap = {}
    for step in steps:
        nodeMap[step] = ([],getInRange(step,steps))
    nodeMap = generateStructure(nodeMap)
    print (findNumArrangements(nodeMap[0]))
