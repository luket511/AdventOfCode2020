from commonFunctions import reader
INPUT = "input5.csv"

def findNum(string,min,max):
    for c in string:
        if min != max:
            if c == "F" or c == "L":
                max = (min+max)//2
            elif c == "B" or c == "R":
                min = int(((min+max)/2)+0.5)
    if min == max:
        return max


if __name__ == "__main__":
    passes = reader(INPUT)
    table = []

    for p in passes:
        r = findNum(p[:-3],0,127)
        c = findNum(p[-3:],0,7)
        table.append(r*8+c)

    table.sort()
    print (table)
