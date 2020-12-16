from commonFunctions import reader, Point
from Day_12a import Ship
INPUT = "input12.csv"

class BetterShip(Ship):
    def __init__(self):
        super().__init__()
        self.pos = Point(10,1)      #Here this variable represents the waypoint position. However if i were to rename it to a better name, I would also have to redo most of the methods previously defined in the Ship class
        self.actualPos = Point()

    def moveForwards(self,distance):
        for i in range(distance):
            self.actualPos.movePoint(self.pos)

    def turnRight(self,degrees):
        for i in range(degrees//90):
            self.pos.setPos(self.pos.y,-self.pos.x)

    def turnLeft(self,degrees):
        for i in range(degrees//90):
            self.pos.setPos(-self.pos.y,self.pos.x)

    def getPosition(self):
        return self.actualPos

    def getWayPoint(self):
        return self.pos

    def getManhattenDistance(self):
        return abs(self.actualPos.y) + abs(self.actualPos.x)

if __name__ == "__main__":
    ship = BetterShip()
    ship.navigate(reader(INPUT))
    print (ship.getManhattenDistance())