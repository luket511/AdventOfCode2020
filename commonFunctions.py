import csv

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

def reader(inputFile):
    output = []
    with open(inputFile) as file:
        reader = csv.reader(file,delimiter=',')
        for row in reader:
            output.append(row[0])
    return output