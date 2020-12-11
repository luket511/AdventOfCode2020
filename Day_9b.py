from commonFunctions import reader
from Day_9a import findBroken
INPUT = "input9.csv"

def findSequence(data,targetNum):

    data = list(map(int,data))

    for i in range(len(data)):
        continuousTotal = 0
        continuousSequence = []
        for num in data[i:]:
            continuousTotal += num
            continuousSequence.append(num)
            if continuousTotal == targetNum:
                return continuousSequence
            elif continuousTotal > targetNum:
                break


if __name__ == "__main__":
    dataSet = reader(INPUT)
    brokenNum = findBroken(dataSet,25)
    print ("Broken Number: {0}".format(brokenNum))
    seq = findSequence(dataSet,brokenNum)
    seq.sort()
    print ("Sequence: {0}".format(seq))
    print ("Biggest and Smallest Sum: {0}".format(seq[0]+seq[len(seq)-1]))
