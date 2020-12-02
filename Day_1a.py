import Input1

def bruteForcePairs(target,inputList):
    for firstNum in inputList:
        for secondNum in inputList:
            if (firstNum + secondNum) == target:
                return [firstNum,secondNum]

def findMatchingPairs(target,inputList):
    for num in inputList:
        required = target - num
        if required in inputList:
            return [num,required]
    return None

if __name__ == "__main__":
    # solutionList = bruteForcePairs(2020,Input.LIST)
    solutionList = findMatchingPairs(2020,Input.LIST)
    print (solutionList)