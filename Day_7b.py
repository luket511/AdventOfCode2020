from commonFunctions import reader, flatten
from Day_7a import Bag, generateBagStructure
INPUT = "input7test2.csv"

class AdvancedBag(Bag):
    def __init__(self,colour,canContain,isContainedIn):
        super().__init__(colour,canContain,isContainedIn)

    def getContains(self):
        return self.contains

def findTotalBagsNeeded(bagStructure,needed):
    contains = bagStructure[needed].getContains()
    if contains == []:
        return 1
    else:
        counter = 1
        for type in contains:
            counter += int(type[0]) * findTotalBagsNeeded(bagStructure,type[1])
        return counter
        
if __name__ == "__main__":
    rules = generateBagStructure(INPUT,AdvancedBag)
    print (findTotalBagsNeeded(rules,"shiny gold")-1)
