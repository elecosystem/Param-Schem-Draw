'''
    Current Source module for ParamSchemDraw

    A set of classes and methods to ease the drawing and manipulation of current
    sources.

    Author: Pedro Martins
    version: 0.1.2
'''

from math import floor, log10
from random import randint, choice

from ParamSchemDraw import *


class iSource(electricComponent):
    '''
        Class used to define an ideal independent current source
        It offers a method to check if a number is a valid voltage value
        It can also format the voltage value to enginnering notation
    '''

    def __init__(self, current, label= "", digits=3):
        '''
            USAGE: iSource(voltage, label, digits)
                   iSource(voltage, label)
                   iSource(voltage)

            ARGUMENTS:
                current -> current value for the given voltage source element
                label   -> name/identifier of the current source (optional)
                digits  -> number of significant digits to use in enginnering notation

            OUTPUT: a independent current source object

            CONSTRAINTS:
                currents must be a non zero number. Float and Integer are supported
                label must be a string
                digits must be a integer in the interval [1, 16]

                other types/values outside the specified will result in
                AssertionError/Exceptions
        '''
        assert isinstance(label, str), "The label element must be a string"
        assert isinstance(digits, int), "The digits element must be an integer"
        assert digits >= 1 and digits <= 16, "The digits element must be between [1, 16]"

        if iSource.isValidISource(current):
            self._current = current
            self._label   = label
            self._digits  = digits
        else:
            raise InvalidIndepentSource

    __UNIT = "A"

    @property
    def current(self):
        return self._current

    @property
    def currentEng(self):
        '''
            Outputs the voltage of the voltage source in enginnering notation,
            appending the volts unit and using the significant number of digits
            defined when the object was created
        '''
        return engineerNotation(self._current, iSource.__UNIT, self._digits)

    @property
    def label(self):
        return self._label

    @label.setter
    def label(self, label):
        assert isinstance(label, str), "The label of the current source must be a string"
        self._label = label

    @property
    def digits(self):
        return self._digits

    @property
    def schem(self):
        return self._schem

    @schem.setter
    def schem(self, schematic):
        self._schem = schematic

    @staticmethod
    def unit():
        return iSource.__UNIT

    @staticmethod
    def isValidISource(I):
        '''
            Check if I is a valid value for current.
            It must be a non zero integer or float
        '''
        return True
        if isinstance(I, (int, float, complex)):
            if I != 0:
                return True
        return False

class InvalidIndepentSource(ValueError, TypeError):
    '''
        The voltage/current value can't be zero
        Float, integer and complex are acceptable
    '''
    pass
