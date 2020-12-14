from commonFunctions import reader, findMax
INPUT = "input10.csv"

def formatInput(file):
    # Formats input list into sorted integers, with the first step (0) and last step (largest adapter + 3) included
    steps = list(map(int,reader(file)))
    steps.append(0)
    steps.append(findMax(steps)+3)
    steps = sorted(steps)
    return steps

if __name__ == "__main__":
    #Track number of 1 diffs and 3 diffs
    ones = 0
    threes = 0 

    steps = formatInput(INPUT)

    prev = None #Used to track previous number
    for adapter in steps:
        print (adapter)
        try:
            diff = adapter - prev
            print ("diff from prev: {0}".format(diff))
            if diff == 1:
                ones += 1
            elif diff == 3:
                threes += 1
        except:
            pass
        prev = adapter
        print ("==========")

    print ("==========")
    print ("Threes: {0}, Ones: {1}".format(threes, ones))
    print ("Threes x Ones: {0}".format(threes*ones))
            
