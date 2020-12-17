from os import read, times
from commonFunctions import reader
from math import ceil
INPUT = "input13.csv"

class Bus():
    def __init__(self,ID):
        self.id = int(ID)

    def getNextBusTime(self,currentTime):
        rem = currentTime%self.id
        return  (self.id - rem) + currentTime

    def getId(self):
        return self.id

    def __str__(self):
        return str(self.id)

def getNextBus(inputTuple):
    timeStamp = inputTuple[0]
    buses = inputTuple[1]
    nextBus = buses.pop(0)
    nextBusTime = nextBus.getNextBusTime(timeStamp)
    for bus in buses:
        time = bus.getNextBusTime(timeStamp)
        if time < nextBusTime:
            nextBusTime = time
            nextBus = bus
    return (nextBus,nextBusTime-timeStamp)



def formatInput(input):
    timeStamp = int(input[0])
    buses = []
    for id in input[1].split(","):
        if id != "x":
            buses.append(Bus(id))
    return (timeStamp,buses)

if __name__ == "__main__":
    inputTuple = formatInput(reader(INPUT))
    busTuple = getNextBus(inputTuple)
    print (busTuple[0].getId() * busTuple[1])
