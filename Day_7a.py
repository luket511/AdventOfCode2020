﻿from commonFunctions import reader
import re
INPUT = "input7test.csv"



class Bag():
    def __init__(self,canContain):
        pass

    def canBeContainedIn(self):
        pass

    def canContain(self):
        pass

if __name__ == "__main__":
    rules = []
    for rule in reader(INPUT):
        r = {}

        head = re.findall("([a-z]+) ([a-z]+) bags c",rule)[0]
        head = "{0} {1}".format(head[0],head[1])

        body = re.findall("(\d [a-z]+ [a-z]+)")
        
