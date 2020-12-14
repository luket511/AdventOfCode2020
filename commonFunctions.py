import csv

NEWLINECHAR = "---NEWLINE---"
LIST = type([])
TUPLE = type(())

## USELESS split() method already exists for strings
# def split(inpString,breakChar):
#     output = []
#     currentString = ""
#     for cha in inpString:
#         if cha == breakChar:
#             if currentString != "":
#                 output.append(currentString)
#             currentString = ""
#         else:
#             currentString += (cha)
#     if currentString != "":
#         output.append(currentString)
#     return output

def removeDuplicates(inpList):
    if isList(inpList):
        s = set(inpList)
        return list(s)
    else:
        raise TypeError

#https://stackoverflow.com/questions/12472338/flattening-a-list-recursively
def flatten(S):
    if S == []:
        return S
    if isinstance(S[0], list):
        return flatten(S[0]) + flatten(S[1:])
    return S[:1] + flatten(S[1:])
        
def isTuple(inp):
    return type(inp) == TUPLE

def isList(inp):
    return type(inp) == LIST

def merge(inpList):
    output = ""
    for i in inpList:
        output += i
        output += " "
    return output

def reader(inputFile):
    output = []
    with open(inputFile) as file:
        reader = csv.reader(file,delimiter='¬')
        for row in reader:
            try:
                output.append(row[0])
            except IndexError:
                output.append(NEWLINECHAR)
    return output

def findMax(inpList): #Takes input list of integers and returns largest item in list
    output = 0
    for i in inpList:
        if i > output:
            output = i
    return output


class Node():
    def __init__(self,value,parentNodes):
        self.value = value
        self.children = []
        for node in parentNodes:
            node.addChildNode(self)

    def getValue(self):
        return self.value

    def getChildNodes(self):
        return self.children

    def addChildNode(self,node):
        self.children.append(node)
    
    def hasChildren(self):
        return len(self.children) != 0

    def hasNoChildren(self):
        return not self.hasChildren()

    def getNumberOfChildren(self):
        return len(self.children)

    def __str__(self):
        return ("(Node {0}:{1})".format(self.value,self.children))


#Takes input of the form {key,([parentNodes],[childNodes])} and returns a dictionary of the type {key, Node} where Node is linked to parents
def generateStructure(nodeMap):
    for key in nodeMap.keys():
        nodeVal = key
        nodeChildren = nodeMap[key][1]
        nodeParents = nodeMap[key][0]
        nodeMap[key] = Node(nodeVal,nodeParents)
        for child in nodeChildren:
            if isTuple(nodeMap[child]):
                nodeMap[child][0].append(nodeMap[key])
            else:
                nodeMap[key].addChildNode(nodeMap[child])
    return nodeMap

def printDict(inpDict):
    for key in inpDict.keys():
        print ("{0}:{1}".format(key,inpDict[key]))