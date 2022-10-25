from pgl import *
from gtools import *
from EnigmaConstants import *

class EnigmaRotor(GCompound):
    def __init__(self, x, y, letter, offset = 0):
        self.x = x
        self.y = y
        GCompound.__init__(self)
        rotor = createFilledRect(x - (ROTOR_WIDTH / 2), y - (ROTOR_HEIGHT / 2), ROTOR_WIDTH, ROTOR_HEIGHT, ROTOR_BGCOLOR)
        self.add(rotor)
        rotorLetter = createCenteredLabel(letter, x - 5, y - 2, ROTOR_FONT)
        rotorLetter.setColor(ROTOR_COLOR)
        self.letter = rotorLetter
        self.add(rotorLetter)
        self.offset = offset

    def getOffset(self):
        return self.offset

    def setOffset(self, offset):
        self.offset = offset

    def advance(self):
        self.setOffset(self.getOffset() + 1)
        q = self.getOffset()
        if q == 26:
            self.setOffset(0)
            self.letter.setLabel(ALPHABET[self.getOffset()])
            return True
        else:
            self.letter.setLabel(ALPHABET[self.getOffset()])
            return False

    def clickAction(self, enigma):
        self.advance()

def applyPermutation(key, permutation, offset):
    i = (ALPHABET.index(key.letter.getLabel())) + offset
    if i > 25:
        i = 25 - (i % 25)
    ch = permutation[i]
    i = (ALPHABET.index(ch)) - offset
    if i > 25:
        i = 25 - (i % 25)
    return i

def invertKey(string):
    invertedKey = ""
    for ch in ALPHABET:
        invertIndex = string.find(ch)
        invertLetter = ALPHABET[invertIndex]
        invertedKey += invertLetter
    return invertedKey

def applyEnigma(key, enigma):
    r1 = enigma.rotorList[0].getOffset()
    r2 = enigma.rotorList[1].getOffset()
    r3 = enigma.rotorList[2].getOffset()

    permutation = ROTOR_PERMUTATIONS[2]
    offset = r3
    # if x < 0:
    #     x += 25
    xch = enigma.keyList[applyPermutation(key, permutation, offset)]

    permutation = ROTOR_PERMUTATIONS[1]
    offset = r2
    # if y < 0:
    #     y += 25
    ych = enigma.keyList[applyPermutation(xch, permutation, offset)]

    permutation = ROTOR_PERMUTATIONS[0]
    offset = r1
    # if z < 0:
    #     z += 25
    zch = enigma.keyList[applyPermutation(ych, permutation, offset)]

    permutation = REFLECTOR_PERMUTATION
    offset = 0
    # if r < 0:
    #     r += 25
    rch = enigma.keyList[applyPermutation(zch, permutation, offset)]

    permutation = invertKey(ROTOR_PERMUTATIONS[0])
    offset = r1
    # if a < 0:
    #     a += 25
    ach = enigma.keyList[applyPermutation(rch, permutation, offset)]

    permutation = invertKey(ROTOR_PERMUTATIONS[1])
    offset = r2
    # if b < 0:
    #     b += 25
    bch = enigma.keyList[applyPermutation(ach, permutation, offset)]

    permutation = invertKey(ROTOR_PERMUTATIONS[2])
    offset = r3
    c = applyPermutation(bch, permutation, offset)
    # if c < 0:
    #     c += 25

    return c



