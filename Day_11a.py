from commonFunctions import reader
INPUT = "input11.csv"

class Layout():
    def __init__(self,layout):
        self.layout = []
        for rowString in layout:
            row = []
            for char in rowString:
                row.append(char)
            self.layout.append(row)
        self.dimensionX = len(self.layout[0])
        self.dimensionY = len(self.layout)

    def getFinalNumberOccupied(self):
        nextLayout = self.updateMap()
        while nextLayout != self.layout:
            self.layout = nextLayout
            nextLayout = self.updateMap()
            
        counter = 0
        for row in self.layout:
            for tile in row:
                if tile == "#":
                    counter += 1
        return counter

    def updateMap(self):
        newLayout = []
        for yCoord in range(self.dimensionY):
            newLayout.append([])
            for xCoord in range(self.dimensionX):
                if self.isUnoccupied(xCoord,yCoord):
                    if self.getOccupiedAjacent(xCoord,yCoord) == 0:
                        newLayout[yCoord].append("#")
                    else:
                        newLayout[yCoord].append("L")
                elif self.isOccupied(xCoord,yCoord):
                    if self.getOccupiedAjacent(xCoord,yCoord) >= 4:
                        newLayout[yCoord].append("L")
                    else:
                        newLayout[yCoord].append("#")
                else:
                    newLayout[yCoord].append(".")
        return newLayout

    def getOccupiedAjacent(self,x,y):
        coordsToCheck = [
            (x+1,y+1),
            (x+1,y-1),
            (x+1,y),
            (x,y+1),
            (x,y-1),
            (x-1,y+1),
            (x-1,y-1),
            (x-1,y),
        ]
        counter = 0
        for coord in coordsToCheck:
            xCoord = coord[0]
            yCoord = coord[1]
            if self.isValidCoord(xCoord,yCoord):
                if self.isOccupied(xCoord,yCoord):
                    counter += 1
        return counter

    def isValidCoord(self,x,y):
        return x < self.dimensionX and x >= 0 and y < self.dimensionY and y >= 0

    def isOccupied(self,x,y):
        return self.layout[y][x] == "#"

    def isUnoccupied(self,x,y):
        return self.layout[y][x] == "L"

    def isFloor(self,x,y):
        return self.layout[y][x] == "."

    def getTile(self,x,y):
        return self.layout[y][x]

    def printLayout(self):
        for row in self.layout:
            print (row)

    def setLayout(self,newLayout):
        self.layout = newLayout

if __name__ == "__main__":
    layout = Layout(reader(INPUT))
    print (layout.getFinalNumberOccupied())