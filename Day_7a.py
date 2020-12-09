from commonFunctions import reader, merge, isTuple, isList
import re
INPUT = "input7test.csv"



class Bag():
    def __init__(self,colour,canContain,isContainedIn):
        self.colour = colour
        self.contains = canContain
        self.isContainedBy = isContainedIn

    def findTopBags(self):
        if self.isContainedIn() == []:
            return set().union({self.colour})
        else:
            try:
                output = {self.colour}
                for bag in self.isContainedIn():
                    output.union({bag.findTopBags()})
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

if __name__ == "__main__":
    rules = {}
    for rule in reader(INPUT):
        ruleSplit = rule.split("contain")
        # print (ruleSplit)
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
        
        # print (body)
        
        rules[head] = (body,[])
        
    # print (rules)

    for key in rules.keys():
        rules[key] = Bag(key,rules[key][0],rules[key][1])
        for colour in rules[key].coloursContained():
            try:
                rules[colour].addNewContainer(rules[key])
            except AttributeError:
                rules[colour][1].append(rules[key])

    print (rules["shiny gold"].findTopBags())

    print (rules["light red"].findTopBags())
