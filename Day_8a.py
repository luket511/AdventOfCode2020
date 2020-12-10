from commonFunctions import reader
INPUT = "input8test.csv"

class InstructionProcessor():
    def __init__(self, program):
        self.visited = []
        self.accumulator = 0
        self.programCounter = 0
        self.program = []
        instructionMap = {"nop":self.nop,"acc":self.acc,"jmp":self.jmp}
        for instruction in program:
            instruction = instruction.split()
            operator = instructionMap[instruction[0]]
            operand = int(instruction[1])
            self.program.append((operator,operand))


    def getAcc(self):
        return self.accumulator

    def getPC(self):
        return self.programCounter

    def acc(self,val):
        self.accumulator += val
        self.jmp(1)

    def jmp(self,val):
        self.programCounter += val

    def nop(self, val):
        self.jmp(1)

    def getInstructionMap(self):
        return {}

    def next(self):
        if self.getPC() in self.visited:
            print("Final Acc Value: {0}, Duplicate Visited:{1}".format(self.getAcc(),self.getPC()))
            return False
        else:
            self.visited.append(self.getPC())
            instruction = self.program[self.getPC()]
            instruction[0](instruction[1])
            return True

    def nextDebug(self):
        print ("PC:{0}, ACC:{1}, Next Instruction:{2}".format(self.getPC(),self.getAcc(),self.program[self.getPC()]))
        input("")
        return self.next()

if __name__ == "__main__":
    ip = InstructionProcessor(reader(INPUT))
    while ip.next():
        pass

