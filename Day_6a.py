from commonFunctions import reader, NEWLINECHAR
INPUT = "input6.csv"

def processAnswers(answers):
    groups = []
    group = set()
    for answer in answers:
        if answer == NEWLINECHAR:
            groups.append(group)
            group = set()
        else:
            for char in answer:
                group.add(char)
    if group != set():
        groups.append(group)

    total = 0
    for answers in groups:
        total += len(answers)
    
    print (total)




if __name__ == "__main__":
    processAnswers(reader(INPUT))
