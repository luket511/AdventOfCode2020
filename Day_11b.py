from commonFunctions import reader
from Day_11a import Layout
INPUT = "input11.csv"

class AdvancedLayout(Layout):

    def updateMap(self):
        newLayout = []
        for yCoord in range(self.dimensionY):
            newLayout.append([])
            for xCoord in range(self.dimensionX):
                if self.isUnoccupied(xCoord,yCoord):
                    if self.getDirectionalOccupation(xCoord,yCoord) == 0:
                        newLayout[yCoord].append("#")
                    else:
                        newLayout[yCoord].append("L")
                elif self.isOccupied(xCoord,yCoord):
                    if self.getDirectionalOccupation(xCoord,yCoord) >= 5:
                        newLayout[yCoord].append("L")
                    else:
                        newLayout[yCoord].append("#")
                else:
                    newLayout[yCoord].append(".")
        return newLayout

    def getDirectionalOccupation(self,xStart,yStart):
        directions = [
            (-1,-1),    #NW
            (0,-1),     #N
            (1,-1),     #NE
            (1,0),      #E
            (1,1),      #SE
            (0,1),      #S
            (-1,1),     #SW
            (-1,0)      #W
        ]

        counter = 0
        for direction in directions:
            x = xStart + direction[0]
            y = yStart + direction[1]

            while self.isValidCoord(x,y) and self.isFloor(x,y):
                x += direction[0]
                y += direction[1]

            if self.isInvalidCoord(x,y):
                continue

            if self.isOccupied(x,y):
                counter += 1

        return counter

    def isSeat(self,x,y):
        return not self.isFloor(x,y)        

    def isInvalidCoord(self,x,y):
        return not self.isValidCoord(x,y)

if __name__ == "__main__":
    layout = AdvancedLayout(reader(INPUT))
    print (layout.getFinalNumberOccupied())