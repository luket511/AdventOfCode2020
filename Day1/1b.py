import csv

inputList = []
with open("Input.csv") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        inputList.append(int(row[0]))

def obviousSolution():
    for firstNum in inputList:
        for secondNum in inputList:
            for thirdNum in inputList:
                if (firstNum + secondNum + thirdNum) == 2020:
                    return [firstNum,secondNum,thirdNum]

solutionList = obviousSolution()
print (solutionList)
print (solutionList[0] * solutionList[1] * solutionList[2])