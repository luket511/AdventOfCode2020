import csv
import math
from functools import reduce

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

class Point():
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y

    def equals(self,p):
        return type(p) == type(self) and p.x == self.x and p.y == self.y

    def getPos(self):
        return "({0},{1})".format(self.x,self.y)

    def setPos(self,x,y):
        self.__init__(x,y)

    def moveCoords(self,x,y):
        self.x += int(x)
        self.y += int(y)

    def movePoint(self,p):
        self.x += p.x
        self.y += p.y

    def __str__(self):
        return "({0},{1})".format(self.x,self.y)

DIRECTION_MAP = {
    0:"N",
    90:"E",
    180:"S",
    270:"W"
}

### https://rosettacode.org/wiki/Chinese_remainder_theorem#Python_3.6 ###
def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a*b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod

### https://rosettacode.org/wiki/Chinese_remainder_theorem#Python_3.6 ###
def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a // b
        a, b = b, a%b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1