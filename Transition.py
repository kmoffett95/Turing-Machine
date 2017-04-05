"""
    This class represents an entry in the transition table
"""
class Transition():
    state = -1;
    move = -1
    writeSymbol = -1;

    def __init__(self, state, move, writeSymbol):
        self.state = state
        self.move = move
        self.writeSymbol = writeSymbol

    def __str__(self):
        return "State: " + str(self.state) + "\n" + \
               "Move: " + str(self.move) + "\n" + \
               "Write Symbol: " + str(self.writeSymbol);
            
        
    
