# File: EnigmaMachine.py

"""
This module is the starter file for the EnigmaMachine class.
"""

from pgl import *
from EnigmaConstants import *
from EnigmaKey import *
from EnigmaLamp import *
from EnigmaRotor import *



# Class: EnigmaMachine

class EnigmaMachine():

    """
    This class is responsible for storing the data needed to simulate
    the Enigma machine.  If you need to maintain any state information
    that must be shared among different parts of this implementation,
    you should define that information as part of this class and
    provide the necessary getters, setters, and other methods needed
    to manage that information.
    """
    def __init__(self, gw):
        """
        The constructor for the EnigmaMachine class is responsible for
        initializing the graphics window along with the state variables
        that keep track of the machine's operation.
        """
        enigmaImage = GImage("images/EnigmaTopView.png")
        gw.add(enigmaImage)

        self.gw = gw
        lampList = []
        keyList = []
        rotorList = []

        p = 2

        for i in range(len(ALPHABET)):
            x = int(KEY_LOCATIONS[i][0])
            y = int(KEY_LOCATIONS[i][1])
            letter = str(ALPHABET[i])
            key = EnigmaKey(x, y, letter)
            keyList.append(key)
            gw.add(key)

        for i in range(len(ALPHABET)):
            x = int(LAMP_LOCATIONS[i][0])
            y = int(LAMP_LOCATIONS[i][1])
            letter = str(ALPHABET[i])
            lamp = EnigmaLamp(x, y, letter)
            lampList.append(lamp)
            gw.add(lamp)

        for i in range(len(ROTOR_LOCATIONS)):
            x = int(ROTOR_LOCATIONS[i][0])
            y = int(ROTOR_LOCATIONS[i][1])
            letter = "A"
            rotor = EnigmaRotor(x, y, letter)
            rotorList.append(rotor)
            gw.add(rotor)

        self.lamp = lamp
        self.lampList = lampList
        self.keyList = keyList
        self.rotor = rotor
        self.rotorList = rotorList
        self.p = p

    def keyPressed(self, key):
        x = self.rotorList[self.p].advance()
        if x is True:
            y = self.rotorList[self.p - 1].advance()
            if y is True:
                z = self.rotorList[self.p - 2].advance()
        index = applyEnigma(key, self)
        self.index = index
        self.lamp = self.lampList[index]
        self.lamp.setState(True)

    def keyReleased(self, key):
        self.lamp = self.lampList[self.index]
        self.lamp.setState(False)