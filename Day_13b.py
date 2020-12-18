from commonFunctions import reader
from Day_13a import Bus
INPUT = "input13.csv"

class AdvancedBus(Bus):
    def __init__(self,id,offset):
        super().__init__(id)
        self.offset = offset

    def changeOffset(self,change):
        self.offset += change

    def checkTime(self,time):
        return (self.offset+time)%self.id == 0

def formatInput(input):
    counter = 0
    buses = []
    for id in input[1].split(","):
        if id != "x":
            buses.append(AdvancedBus(id,counter))
        counter += 1
    return buses

def findLeastCommonBus(buses):
    largestId = 0
    leastCommonBusIndex = 0
    for bus in buses:
        if bus.id > largestId:
            leastCommonBusIndex = buses.index(bus)
            largestId = bus.id
    return leastCommonBusIndex

def findSmallestOffset(buses):
    smallestOffset = 0
    for bus in buses:
        if bus.offset < smallestOffset:
            smallestOffset = bus.offset
    return smallestOffset

def reformatBuses(buses, function):
    leastCommonBusIndex = function(buses)
    offsetChange = 0 - buses[leastCommonBusIndex].offset
    for bus in buses:
        bus.changeOffset(offsetChange)
    return buses


def checkTime(buses,time):
    output = True
    for bus in buses:
        output = output and bus.checkTime(time)
        if not output:
            break
    return output

if __name__ == "__main__":
    buses = formatInput(reader(INPUT))
    buses = reformatBuses(buses,findLeastCommonBus)
    increment = buses[findLeastCommonBus(buses)].id
    print (increment)
    counter = 0
    while not checkTime(buses,counter):
        counter += increment
        print (counter)
    print (counter + findSmallestOffset(buses))
    
