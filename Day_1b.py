import Input1
from Day_1a import findMatchingPairs

def bruteForceTrips(target,inputList):
    for firstNum in inputList:
        for secondNum in inputList:
            for thirdNum in inputList:
                if (firstNum + secondNum + thirdNum) == target:
                    return [firstNum,secondNum,thirdNum]

def findMatchingTrips(target,inputList):
    for num in inputList:
        inputList.remove(num)
        otherTarget = target - num
        pairList = findMatchingPairs(otherTarget,inputList)
        if pairList is not None:
            pairList.append(num)
            return pairList 

if __name__ == "__main__":
    solutionList = bruteForceTrips(2020,Input.LIST)
    # solutionList = findMatchingTrips(2020,Input.LIST)
    print (solutionList)