from commonFunctions import reader, flatten, removeDuplicates
import re
INPUT = "input7.csv"



class Bag():
    def __init__(self,colour,canContain,isContainedIn):
        self.colour = colour
        self.contains = canContain
        self.isContainedBy = isContainedIn


    def findBagsIncludedIn(self):
        output = removeDuplicates(flatten(self.findTopBags()))
        output.remove(self.colour)
        return output

    def findTopBags(self):
        if self.isContainedIn() == []:
            return self.colour
        else:
            try:
                output = [self.colour]
                for bag in self.isContainedIn():
                    output.append(bag.findTopBags())
                return output
            except TypeError:
                print (output,self.colour)

    def isContainedIn(self):
        return self.isContainedBy

    def coloursContained(self):
        output = []
        for bagType in self.contains:
            output.append(bagType[1])
        return output

    def addNewContainer(self,newContainer):
        self.isContainedBy.append(newContainer)

    def __str__(self):
        return "Bag containing {0}, contained in {1}".format(self.coloursContained(), self.isContainedIn())

def generateBagStructure(file,bagType=Bag):
    rules = {}
    for rule in reader(file):
        ruleSplit = rule.split("contain")
        head = ruleSplit[0]
        head = head.split()
        head = "{0} {1}".format(head[0],head[1])

        body = []
        for description in ruleSplit[1].split(","):
            descriptor = description.split()
            if descriptor[0] == "no":
                break
            else:
                num = descriptor[0]
                colour = descriptor[1] + " " + descriptor[2]
                body.append((num,colour))
        
        rules[head] = (body,[])

    for key in rules.keys():
        rules[key] = bagType(key,rules[key][0],rules[key][1])
        for colour in rules[key].coloursContained():
            try:
                rules[colour].addNewContainer(rules[key])
            except AttributeError:
                rules[colour][1].append(rules[key])

    return rules

if __name__ == "__main__":
    rules = generateBagStructure(INPUT)
    print ((rules["shiny gold"].findBagsIncludedIn()))
