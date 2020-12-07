from commonFunctions import reader, NEWLINECHAR
import re

INPUT = "input4.csv"

NEEDEDFIELDS = [
    "byr:[^ \n]+",
    "iyr:[^ \n]+",
    "eyr:[^ \n]+",
    "hgt:[^ \n]+",
    "hcl:[^ \n]+",
    "ecl:[^ \n]+",
    "pid:[^ \n]+",
    "cid:[^ \n]+"
]

class Passport():
    def __init__(self,inputDetails):
        self.passport = {}
        self.missingFields = []
        for field in NEEDEDFIELDS:
            try:
                fieldString = re.findall(field,inputDetails)[0]
                fieldList = fieldString.split(":")
                self.passport[fieldList[0]] = fieldList[1]
            except IndexError:
                self.missingFields.append(field[:3])
                continue

    def getField(self,fieldType):
        try:
            return self.passport[fieldType]
        except KeyError:
            return None

    def getNumOfFields(self):
        return (len(self.passport.keys()))

    def getMissingFields(self):
        return self.missingFields

    def __str__(self):
        return str(self.passport)

def batchHandler(file):
    batch = reader(file)
    passports = []
    currentPassport = ""

    for string in batch:
        if string == NEWLINECHAR:
            if currentPassport != "":
                passports.append(currentPassport)
            currentPassport = ""
        else:
            currentPassport += string
    if currentPassport != "":
        passports.append(currentPassport)

    refinedPassports = []

    for passportDetails in passports:
        refinedPassports.append(Passport(passportDetails))
    return refinedPassports

def validatePassports(passports):
    numValid = 0
    for passport in passports:
        if passport.getNumOfFields() == 8:
            numValid += 1
        elif passport.getNumOfFields() == 7 and passport.getField("cid") == None:
            numValid += 1
    return numValid


if __name__ == "__main__":
    passports = batchHandler(INPUT)
    numValid = validatePassports(passports)
    print (numValid)