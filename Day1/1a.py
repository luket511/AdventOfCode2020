import csv

inputList = []
with open("Input.csv") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        inputList.append(int(row[0]))

def obviousSolution():
    for firstNum in inputList:
        for secondNum in inputList:
            if (firstNum + secondNum) == 2020:
                return [firstNum,secondNum]

def otherSolution():
    for num in inputList:
        required = 2020 - num
        if required in inputList:
            return [num,required]

solutionList = otherSolution()
solution = solutionList[0] * solutionList[1]
print (solution)