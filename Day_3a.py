from commonFunctions import reader
INPUT = "Input3.csv"

class MapNavigator():
    def __init__(self,map):
        self.map = map
        self.MAP_WIDTH = len(map[0])
        self.MAP_HEIGHT = len(map)

    def isTree(self,x,y):
        xNorm = x % self.MAP_WIDTH
        yNorm = y % self.MAP_HEIGHT
        return (self.map[yNorm][xNorm] == "#")

    def getSlopeHeight(self):
        return self.MAP_HEIGHT  



def navigateMapBase(file):
    mn = MapNavigator(reader(file))
    numTreesHit = 0
    for y in range(mn.getSlopeHeight()):
        x = 3*y
        if mn.isTree(x,y):
            numTreesHit += 1
    
    return numTreesHit

if __name__ == "__main__":
    print (navigateMapBase(INPUT))
