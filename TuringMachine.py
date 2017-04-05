from Transition import Transition
class TuringMachine:
    transitions = [[]];     # This attribute store a 2d list representing the transition table
    transitionTableRows = transitionTableColumns = 0;
    currentState, finalState = 0, 9;
    tape = "";  
    tapeHeadPosition = 0;   # Represents which character the TM tapehead is pointing at
    stepCount, maxAllowedSteps = 0, 0;

    """
        An encoding of the transition table is given to the constructor
        An input is also required (it must be a binary string)
        A '2' in the tape represents a blank
        By defualt, this is a 3 state machine (a 2x3 transition table)
        Example of use: tm = TuringMachine("001090151104", "1111")
                        tm.simulate()
    """
    def __init__(self, transitions, inputString, maxSteps = 100000, \
                 terminalState = 9, transTableRows = 2, transTableColumns = 3):
        self.transitionTableRows, self.transitionTableColumns = transTableRows, transTableColumns
        self.tape = inputString
        self.finalState = terminalState
        self.maxAllowedSteps = maxSteps
        self.setTransitions(transitions);

    """
        The encoding is a 12 digit string by default
        Each consecutive pair of digits represents an entry in the transitions table
        The first digit is the next state to move to
        The second digit % 2 tells which direction to move the tape head (0 = Move Left, 1 = Move Right)
        The second digit % 3 is the symbol to write to the tape
    """
    def setTransitions(self, transitions):
        pairs = self.getPairsFromDescription(transitions)
        transitions = []
        for i in pairs:
            state, move, writeSymbol = int(i[0]), int(i[1]) % 2, int(i[1]) % 3
            transitions.append(Transition(state, move, writeSymbol))
        self.transitions = self.convert1dArrayTo2dArray(transitions)

    # Simply takes the string and returns a list of the digits in pairs
    def getPairsFromDescription(self, transitions):
        pairs = []
        for i in range(0, len(transitions), 2):
            pairs.append(transitions[i : i + 2])
        return pairs

    # Converts list of transition into a tabular form suitable for quick indexing
    def convert1dArrayTo2dArray(self, transitions):
        twoDArray = []
        for i in range(0, len(transitions), self.transitionTableRows + 1):
            twoDArray.append(transitions[i : i + self.transitionTableColumns])
        return twoDArray

    """
        Runs the TM on the current input
        Returns true if the TM halts within the limited number of steps
    """
    def simulate(self):
        while (self.stepCount < self.maxAllowedSteps):
            if (self.currentState == self.finalState): break

            nextTransition = self.getNextTransition()
            self.writeSymbolOnTape(nextTransition.writeSymbol)
            self.setTapeHeadPosition(nextTransition.move)

            if self.tapeHeadPosition >= len(self.tape): self.tape += "2";
            self.currentState = nextTransition.state
            self.stepCount += 1
        return self.currentState == self.finalState

    def getNextTransition(self):
        readSymbol = int(self.tape[self.tapeHeadPosition])
        return self.transitions[self.currentState][readSymbol]
    
    def writeSymbolOnTape(self, writeSymbol):
        self.tape = self.tape[0 : self.tapeHeadPosition] + \
                    str(writeSymbol) + \
                    self.tape[self.tapeHeadPosition + 1 :]

    def setTapeHeadPosition(self, move):
        if move == 0:
            if self.tapeHeadPosition != 0:
                self.tapeHeadPosition -= 1
        else: self.tapeHeadPosition += 1
