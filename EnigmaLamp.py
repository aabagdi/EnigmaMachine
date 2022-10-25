from pgl import *
from gtools import *
from EnigmaConstants import *

class EnigmaLamp(GCompound):
    def __init__(self, x, y, letter, state = None):
        self.x = x
        self.y = y
        self.state = state
        GCompound.__init__(self)
        lamp = createFilledCircle(x - 1, y, LAMP_RADIUS, LAMP_BGCOLOR, LAMP_BORDER_COLOR)
        self.add(lamp)
        lampLetter = createCenteredLabel(letter, x - 1, y - 2, LAMP_FONT)
        lampLetter.setColor(LAMP_OFF_COLOR)
        self.letter = lampLetter
        self.add(lampLetter)

    def getState(self):
        return self.state

    def setState(self, state):
        self.state = state
        if state == True:
            self.letter.setColor(LAMP_ON_COLOR)
        else:
            self.letter.setColor(LAMP_OFF_COLOR)

