from commonFunctions import reader
from Day_8a import InstructionProcessor
INPUT = "input8.csv"

class CompletedInstructionProcessor(InstructionProcessor):
    def __init__(self,program):
        super().__init__(program)
        self.completed = False

    def isCompleted(self):
        return self.completed

    def next(self):
        try:
            return super().next()
        except IndexError:
            print("Final Acc Value: {0}, Program Completed".format(self.getAcc()))
            self.completed = True
            return False

    def nextDebug(self):
        try:
            return super().nextDebug()
        except IndexError:
            print("Final Acc Value: {0}, Program Completed".format(self.getAcc()))
            self.completed = True
            return False


if __name__ == "__main__":
    instructionSet = reader(INPUT)

    for i in range(len(reader(INPUT))):
        instruction = instructionSet[i].split()
        operator = instruction[0]
        operand = instruction[1]
        if operator == "nop":
            instructionSet[i] = "jmp {0}".format(operand)
        elif operator == "jmp":
            instructionSet[i] = "nop {0}".format(operand)
        else:
            continue
        # print ("======================")
        # print ("{0}:{1}".format(i+1,instructionSet))


        ip = CompletedInstructionProcessor(instructionSet)
        while ip.next():
            pass
        if ip.isCompleted():
            print ("======================")
            print ("======================")
            print ("Changed Instruction from ({0} {1}) to ({2}) at position {3}".format(operator,operand,instructionSet[i],i+1))
            print ("Completed Program ACC Value: {0}".format(ip.getAcc()))
            break

        instructionSet = reader(INPUT)