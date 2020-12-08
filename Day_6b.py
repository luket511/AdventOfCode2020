from commonFunctions import reader, NEWLINECHAR
INPUT = "input6.csv"

def processAnswers(answers):
    groups = []
    group = []
    for answer in answers:
        if answer == NEWLINECHAR:
            groups.append(group)
            group = []
        else:
            group.append(answer)
    if group != []:
        groups.append(group)

    totalAnswersCorrect = []
    for group in groups:
        answersCorrect = 0
        # answersCorrect = []
        groupLen = len(group)
        answerTally = {}
        for person in group:
            for question in person:
                try:
                    answerTally[question] += 1
                except KeyError:
                    answerTally[question] = 1
        for question in answerTally.keys():
            if answerTally[question] == groupLen:
                answersCorrect += 1
                # answersCorrect.append(question)
        totalAnswersCorrect.append(answersCorrect)
    
    print (sum(totalAnswersCorrect))

                
                

if __name__ == "__main__":
    processAnswers(reader(INPUT))