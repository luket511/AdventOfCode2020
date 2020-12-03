from commonFunctions import reader
from Day_3a import MapNavigator
INPUT = "Input3.csv"

def navigateMap(file,slopeXGradient,slopeYGradient):
    mn = MapNavigator(reader(file))
    numTreesHit = 0
    stepsToBottom = int(mn.getSlopeHeight()/slopeYGradient)
    for y in range(stepsToBottom):
        x = slopeXGradient*y
        y = slopeYGradient*y
        if mn.isTree(x,y):
            numTreesHit += 1
    
    return numTreesHit


if __name__ == "__main__":
    slopes = [
        (1,1),
        (3,1),
        (5,1),
        (7,1),
        (1,2)
        ]

    treesHit = []

    for slope in slopes:
        treesHit.append(navigateMap(INPUT,slope[0],slope[1]))
        
    total = 1
    for i in range(5):
        print ("Slope: {0}, Number of Trees Hit: {1}".format(slopes[i],treesHit[i]))
        total *= treesHit[i]


    print ("Total: {0}".format(total)) 
    