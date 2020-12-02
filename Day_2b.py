from Day_2a import formatInput

def checkPasswords(file):
    passwordDetails = formatInput(file)
    numValid = 0
    for map in passwordDetails:
        char1 = map['password'][map['numOne']-1]
        char2 = map['password'][map['numTwo']-1]
        if (char1 == map['char']) ^ (char2 == map['char']):
            numValid += 1
    return numValid

if __name__ == "__main__":
    print (checkPasswords("Input2.csv"))
