from commonFunctions import reader, Point, DIRECTION_MAP
INPUT = "input12.csv"

class Ship():
    def __init__(self):
        self.direction = 90
        self.pos = Point()
        self.instructionSet = {
            "N":self.moveNorth,
            "S":self.moveSouth,
            "E":self.moveEast,
            "W":self.moveWest,
            "L":self.turnLeft,
            "R":self.turnRight,
            "F":self.moveForwards
        }

    def navigate(self,instructions):
        for instruction in instructions:
            operator = instruction[0]
            operand = int(instruction[1:])
            self.instructionSet[operator](operand)

    def moveNorth(self,distance):
        self.pos.moveCoords(0,distance)

    def moveSouth(self,distance):
        self.pos.moveCoords(0,-distance)

    def moveEast(self,distance):
        self.pos.moveCoords(distance,0)

    def moveWest(self,distance):
        self.pos.moveCoords(-distance,0)

    def moveForwards(self,distance):
        self.instructionSet[self.getDirection()](distance)

    def turnLeft(self,degrees):
        self.direction = (self.direction - degrees)%360

    def turnRight(self,degrees):
        self.direction = (self.direction + degrees)%360

    def reset(self):
        self.__init__()

    def getPosition(self):
        return self.pos

    def getDegrees(self):
        return self.direction

    def getDirection(self):
        return DIRECTION_MAP[self.direction]

    def getManhattenDistance(self):
        return abs(self.pos.y) + abs(self.pos.x)

if __name__ == "__main__":
    s = Ship()
    s.navigate(reader(INPUT))
    print (s.getManhattenDistance())