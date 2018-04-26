'''
            ____
    __   __/ ___|  ___  _   _ _ __ ___ ___
    \ \ / /\___ \ / _ \| | | | '__/ __/ _ \
     \ V /  ___) | (_) | |_| | | | (_|  __/
      \_/  |____/ \___/ \__,_|_|  \___\___|


    Voltage Source module for ParamSchemDraw

    A set of classes and methods to ease the drawing and manipulation of voltage
    sources.

    Author: Pedro Martins
    version: 0.1.3
'''

from math import floor, log10
from random import randint, choice

import SchemDraw.elements as e

from ParamSchemDraw import *

class vSource(electricComponent):
    '''
        Class used to define an ideal independent voltage source
        It offers a method to check if a number is a valid voltage value
        It can also format the voltage value to enginnering notation
    '''

    def __init__(self, voltage, label= "", digits=3):
        '''
            USAGE: vSource(voltage, label, digits)
                   vSource(voltage, label)
                   vSource(voltage)

            ARGUMENTS:
                voltage -> voltage value for the given voltage source element
                label  -> name/identifier of the voltage source (optional)
                digits -> number of significant digits to use in enginnering notation

            OUTPUT: a independent voltage source object

            CONSTRAINTS:
                voltage must be a non zero number. Float and Integer are supported
                label must be a string
                digits must be a integer in the interval [1, 16]

                other types/values outside the specified will result in
                AssertionError/Exceptions
        '''
        assert isinstance(label, str), "The label element must be a string"
        assert isinstance(digits, int), "The digits element must be an integer"
        assert digits >= 1 and digits <= 16, "The digits element must be between [1, 16]"
        if vSource.isValidVSource(voltage):
            self._voltage = voltage
            self._label   = label
            self._digits  = digits
        else:
            raise InvalidIndepentSource

    __SCHEMATIC = e.SOURCE_V
    __UNIT = "V"


    @property
    def voltage(self):
        return self._voltage

    @property
    def voltageEng(self):
        '''
            Outputs the voltage of the voltage source in enginnering notation,
            appending the volts unit and using the significant number of digits
            defined when the object was created
        '''
        return engineerNotation(self._voltage, vSource.__UNIT, self._digits)

    @property
    def label(self):
        return self._label

    @label.setter
    def label(self, label):
        assert isinstance(label, str), "The label of the voltage source must be a string"
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
        return vSource.__UNIT

    @staticmethod
    def isValidVSource(V):
        '''
            Check if V is a valid value for voltage.
            It must be a non zero integer or float
        '''
        if isinstance(V, (int, float, complex)):
            if V != 0:
                return True
        return False

    @classmethod
    def schematic(cls):
        return cls.__SCHEMATIC

class InvalidIndepentSource(ValueError, TypeError):
    '''
        The voltage/current value can't be zero
        Float, integer and complex are acceptable
    '''
    pass
