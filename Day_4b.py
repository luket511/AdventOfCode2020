from commonFunctions import reader, NEWLINECHAR
from Day_4a import batchHandler, validatePassports, Passport
import re, random

INPUT = "input4.csv"

NEEDEDFIELDS = [
    "byr:\d{4}",
    "iyr:\d{4}",
    "eyr:\d{4}",
    "hgt:\d+(?:cm|in)",
    "hcl:#[\da-f]{6}",
    "ecl:[a-z]{3}",
    "pid:\d*",
    "cid:[^ \n]+"
]

class SecurePassport(Passport):
    def __init__(self,inputDetails,neededFields):
        self.passport = {}
        self.missingFields = []
        for field in neededFields:
            try:
                fieldString = re.findall(field,inputDetails)[0]
                fieldList = fieldString.split(":")
                self.passport[fieldList[0]] = fieldList[1]
            except IndexError:
                self.missingFields.append(field[:3])
                
    
    def getFieldAsString(self,field):
        return super().getField(field)

    def getFields(self):
        return self.passport.keys()

    def getField(self,field):
        try:
            return int(super().getField(field))
        except:
            return super().getField(field)

    def isValid(self):
        byrCheck = self.checkYear("byr",1920,2002)
        iyrCheck = self.checkYear("iyr",2010,2020)
        eyrCheck = self.checkYear("eyr",2020,2030)
        hgtCheck = self.checkDistance("hgt")
        hclCheck = not self.isFieldNone("hcl")
        eclCheck = self.checkColour("ecl")
        pidCheck = not self.isFieldNone("pid") and len(str(super().getField("pid"))) == 9
        return byrCheck and iyrCheck and eyrCheck and hgtCheck and hclCheck and eclCheck and pidCheck

    def checkDistance(self,field):
        if self.isFieldNone(field):
            return False
        string = self.getField(field)
        distance = int(string[:-2])
        unit = string[-2:]
        if unit == "cm":
            return distance >= 150 and distance <= 193
        elif unit == "in":
            return distance >= 59 and distance <= 76 

    def checkColour(self,field):
        if self.isFieldNone(field):
            return False
        return self.getField(field) in ["amb","blu","brn","gry","grn","hzl","oth"]

        
    def checkYear(self,field,min,max):
        if self.isFieldNone(field):
            return False
        return self.getField(field) >= min and self.getField(field) <= max 
    
    def isFieldNone(self,field):
        return type(self.getField(field)) == type(None)
        

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
    
    return passports



if __name__ == "__main__":
    counter = 0

    for passportDetails in batchHandler(INPUT):
        passport = SecurePassport(passportDetails,NEEDEDFIELDS)
        if passport.isValid():
            counter += 1
    print (counter)
