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