from pgl import *
from gtools import *
from EnigmaConstants import *

class EnigmaKey(GCompound):
    def __init__(self, x, y, letter):
        self.x = x
        self.y = y
        GCompound.__init__(self)
        key = createFilledCircle(x - 1, y, KEY_RADIUS, KEY_BGCOLOR, KEY_BORDER_COLOR)
        key.setLineWidth(KEY_BORDER)
        self.add(key)
        keyLetter = createCenteredLabel(letter, x - 1, y - KEY_BORDER, KEY_FONT)
        keyLetter.setColor(KEY_UP_COLOR)
        self.letter = keyLetter
        self.add(keyLetter)

    def mousedownAction(self, enigma):
        self.letter.setColor(KEY_DOWN_COLOR)
        enigma.keyPressed(self)

    def mouseupAction(self, enigma):
        self.letter.setColor(KEY_UP_COLOR)
        enigma.keyReleased(self)