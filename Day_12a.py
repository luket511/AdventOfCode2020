from commonFunctions import reader, Point
INPUT = "input12test.csv"

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
            operand = instruction[1:]
            self.instructionSet[operator](operand)

    def moveNorth(self,distance):
        self.pos.move(0,distance)

    def moveSouth(self,distance):
        self.pos.move(0,-distance)

    def moveEast(self,distance):
        self.pos.move(distance,0)

    def moveWest(self,distance):
        self.pos.move(-distance,0)

    def moveForwards(self,distance):
        pass

    def turnLeft(self,degrees):
        self.direction = abs()

    def turnRight(self,degrees):
        pass

    def reset(self):
        self.__init__()

    def getPosition(self):
        pass

    def getDirection(self):
        pass

    def getManhattenDistance(self):
        pass

if __name__ == "__main__":
    pass
