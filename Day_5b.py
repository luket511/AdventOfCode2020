from commonFunctions import reader
from Day_5a import findNum
INPUT = "input5.csv"


if __name__ == "__main__":
    passes = reader(INPUT)

    table = []
    for rowNum in range(128):
        row = []
        for colNum in range(8):
            row.append(rowNum*8+colNum)
        table.append(row)

    for p in passes:
        c = findNum(p[-3:],0,7)
        r = findNum(p[:-3],0,127)
        table[r][c] = "T "

    for row in table:
        print(row)

    print ("==============")