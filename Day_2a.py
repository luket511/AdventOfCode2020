from commonFunctions import reader

def formatInput(file):
    inpList = reader(file)
    output = []
    for item in inpList:
        map = {}
        firstFormat = item.split()
        map['password'] = firstFormat[2]
        map['char'] = firstFormat[1][0]
        amounts = firstFormat[0].split("-")
        map['numOne'] = int(amounts[0])
        map['numTwo'] = int(amounts[1])
        output.append(map)
    return (output)

def checkPasswords(file):
    passwordDetails = formatInput(file)
    numValid = 0
    for map in passwordDetails:
        startLength = len(map['password'])
        minLength = startLength - map['numTwo']
        maxLength = startLength - map['numOne']
        map['password'] = map['password'].replace(map['char'],"")
        endLength = len(map['password'])
        if endLength >= minLength and endLength <= maxLength:
            numValid += 1
    return numValid

if __name__ == "__main__":
    print (checkPasswords("Input2.csv"))