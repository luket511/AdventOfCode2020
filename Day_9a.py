from commonFunctions import reader
from Day_1a import findMatchingPairs
INPUT = "input9.csv"

def findBroken(data,preamble):
    if preamble >= len(data):
        return None
    
    data = list(map(int,data))

    for i in range(preamble,len(data)):
        number = data[i]
        if findMatchingPairs(number,data[i-preamble:i]) is None:
            return number
    
    return None
    


if __name__ == "__main__":
    print (findBroken(reader(INPUT),25))
