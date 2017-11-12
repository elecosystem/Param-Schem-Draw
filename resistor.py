'''
    Resitor module for ParamSchemDraw

    A set of classes and methods to ease the drawing and manipulation of resitors.

    Author: Pedro Martins
    version: 0.1.3
'''

from math import floor, log10
from random import randint, choice

import SchemDraw.elements as e

from ParamSchemDraw import engineerNotation
from iSource import *
from vSource import *


class resistor(electricComponent):
    '''
        Class used to define an ideal resistor
        It provides static methods to compute a parallel/series association of
        n resistors, a current divider and a voltage divider. It also offers a
        method to check if a number is a valid resistance value
        It can also format the resistance value to enginnering notation
    '''

    def __init__(self, resistance, label= "", digits=3):
        '''
            USAGE: resistor(resistance, label, digits)
                   resistor(resistance, label)
                   resistor(resistance)

            ARGUMENTS:
                resistance  -> resistance value for the given resistor element
                label       -> name/identifier of the resistance (optional)
                digits      -> number of significant digits to use in enginnering notation

            OUTPUT: a ideal resistor object

            CONSTRAINTS:
                resistance must be a postive number. Float and Integer are supported
                label must be a string
                digits must be a integer in the interval [1, 16]

                other types/values outside the specified will result in
                AssertionError/Exceptions
        '''

        assert isinstance(label, str), "The label element must be a string"
        assert isinstance(digits, int), "The digits element must be an integer"
        assert digits >= 1 and digits <= 16, "The digits element must be between [1, 16]"

        if resistor.isValidResistor(resistance):
            self._resistance  = resistance
            self._label       = label
            self._digits      = digits
        else:
            raise InvalidResistor


    __UNIT = '$\Omega$'
    __SCHEMATIC = e.RES

    # E24 class resistor values
    __E24 = ( 1.0 , 10 , 100 , 1.0 * 10 ** 3 , 10 * 10 ** 3 , 100 * 10 ** 3 , 1.0 * 10 ** 6,
              1.1 , 11 , 110 , 1.1 * 10 ** 3 , 11 * 10 ** 3 , 110 * 10 ** 3 , 1.1 * 10 ** 6,
              1.2 , 12 , 120 , 1.2 * 10 ** 3 , 12 * 10 ** 3 , 120 * 10 ** 3 , 1.2 * 10 ** 6,
              1.3 , 13 , 130 , 1.3 * 10 ** 3 , 13 * 10 ** 3 , 130 * 10 ** 3 , 1.3 * 10 ** 6,
              1.5 , 15 , 150 , 1.5 * 10 ** 3 , 15 * 10 ** 3 , 150 * 10 ** 3 , 1.5 * 10 ** 6,
              1.6 , 16 , 160 , 1.6 * 10 ** 3 , 16 * 10 ** 3 , 160 * 10 ** 3 , 1.6 * 10 ** 6,
              1.8 , 18 , 180 , 1.8 * 10 ** 3 , 18 * 10 ** 3 , 180 * 10 ** 3 , 1.8 * 10 ** 6,
              2.0 , 20 , 200 , 2.0 * 10 ** 3 , 20 * 10 ** 3 , 200 * 10 ** 3 , 2.0 * 10 ** 6,
              2.2 , 22 , 220 , 2.2 * 10 ** 3 , 22 * 10 ** 3 , 220 * 10 ** 3 , 2.2 * 10 ** 6,
              2.4 , 24 , 240 , 2.4 * 10 ** 3 , 24 * 10 ** 3 , 240 * 10 ** 3 , 2.4 * 10 ** 6,
              2.7 , 27 , 270 , 2.7 * 10 ** 3 , 27 * 10 ** 3 , 270 * 10 ** 3 , 2.7 * 10 ** 6,
              3.0 , 30 , 300 , 3.0 * 10 ** 3 , 30 * 10 ** 3 , 300 * 10 ** 3 , 3.0 * 10 ** 6,
              3.3 , 33 , 330 , 3.3 * 10 ** 3 , 33 * 10 ** 3 , 330 * 10 ** 3 , 3.3 * 10 ** 6,
              3.6 , 36 , 360 , 3.6 * 10 ** 3 , 36 * 10 ** 3 , 360 * 10 ** 3 , 3.6 * 10 ** 6,
              3.9 , 39 , 390 , 3.9 * 10 ** 3 , 39 * 10 ** 3 , 390 * 10 ** 3 , 3.9 * 10 ** 6,
              4.3 , 43 , 430 , 4.3 * 10 ** 3 , 43 * 10 ** 3 , 430 * 10 ** 3 , 4.3 * 10 ** 6,
              4.7 , 47 , 470 , 4.7 * 10 ** 3 , 47 * 10 ** 3 , 470 * 10 ** 3 , 4.7 * 10 ** 6,
              5.1 , 51 , 510 , 5.1 * 10 ** 3 , 51 * 10 ** 3 , 510 * 10 ** 3 , 5.1 * 10 ** 6,
              5.6 , 56 , 560 , 5.6 * 10 ** 3 , 56 * 10 ** 3 , 560 * 10 ** 3 , 5.6 * 10 ** 6,
              6.2 , 62 , 620 , 6.2 * 10 ** 3 , 62 * 10 ** 3 , 620 * 10 ** 3 , 6.2 * 10 ** 6,
              6.8 , 68 , 680 , 6.8 * 10 ** 3 , 68 * 10 ** 3 , 680 * 10 ** 3 , 6.8 * 10 ** 6,
              7.5 , 75 , 750 , 7.5 * 10 ** 3 , 75 * 10 ** 3 , 750 * 10 ** 3 , 7.5 * 10 ** 6,
              8.2 , 82 , 820 , 8.2 * 10 ** 3 , 82 * 10 ** 3 , 820 * 10 ** 3 , 8.2 * 10 ** 6,
              9.1 , 91 , 910 , 9.1 * 10 ** 3 , 91 * 10 ** 3 , 910 * 10 ** 3 , 9.1 * 10 ** 6 )

    __E12 = ( 1.0 , 10 , 100 , 1.0 * 10 ** 3 , 10 * 10 ** 3 , 100 * 10 ** 3 , 1.0 * 10 ** 6,
              1.2 , 12 , 120 , 1.2 * 10 ** 3 , 12 * 10 ** 3 , 120 * 10 ** 3 , 1.2 * 10 ** 6,
              1.5 , 15 , 150 , 1.5 * 10 ** 3 , 15 * 10 ** 3 , 150 * 10 ** 3 , 1.5 * 10 ** 6,
              1.8 , 18 , 180 , 1.8 * 10 ** 3 , 18 * 10 ** 3 , 180 * 10 ** 3 , 1.8 * 10 ** 6,
              2.2 , 22 , 220 , 2.2 * 10 ** 3 , 22 * 10 ** 3 , 220 * 10 ** 3 , 2.2 * 10 ** 6,
              2.7 , 27 , 270 , 2.7 * 10 ** 3 , 27 * 10 ** 3 , 270 * 10 ** 3 , 2.7 * 10 ** 6,
              3.3 , 33 , 330 , 3.3 * 10 ** 3 , 33 * 10 ** 3 , 330 * 10 ** 3 , 3.3 * 10 ** 6,
              3.9 , 39 , 330 , 3.9 * 10 ** 3 , 39 * 10 ** 3 , 390 * 10 ** 3 , 3.9 * 10 ** 6,
              4.7 , 47 , 470 , 4.7 * 10 ** 3 , 47 * 10 ** 3 , 470 * 10 ** 3 , 4.7 * 10 ** 6,
              5.6 , 56 , 560 , 5.6 * 10 ** 3 , 56 * 10 ** 3 , 560 * 10 ** 3 , 5.6 * 10 ** 6,
              6.8 , 68 , 680 , 6.8 * 10 ** 3 , 68 * 10 ** 3 , 680 * 10 ** 3 , 6.8 * 10 ** 6,
              8.2 , 82 , 820 , 8.2 * 10 ** 3 , 82 * 10 ** 3 , 820 * 10 ** 3 , 8.2 * 10 ** 6 )

    @property
    def resistance(self):
        return self._resistance

    @property
    def resistanceEng(self, latex=True):
        '''
            Outputs the resistance of the resistor in enginnering notation,
            appending the ohms unit and using the significant number of digits
            defined when the object was created

            The latex argument controls the wrapping of the unit. If latex=False,
            then the unit has no equation latex marker, '$', wrapping the latex command
            for the greek Omega letter. If latex=True, it does and the unit is $\Omega$
        '''
        unit = resistor.__UNIT if latex else '\Omega'
        return engineerNotation(self._resistance, unit, self._digits)

    @property
    def conductance(self):
        return 1.0/self._resistance

    @property
    def conductanceEng(self):
        '''
            Outputs the conductance of the resistor in enginnering notation,
            appending the Siemens unit and using the significant number of digits
            defined when the object was created

            The latex argument is not required. It
        '''
        return engineerNotation(self._resistance, 'S', self._digits)

    @property
    def label(self):
        return self._label

    @label.setter
    def label(self, label):
        assert isinstance(label, str), "The label of the resistor must be a string"
        self._label =  label

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
    def isValidResistor(R):
        '''
            Check if R is a valid value for resistance.
            It must be a positive integer or float
        '''
        if isinstance(R, (int, float)):
            if R > 0:
                return True
        return False


    @staticmethod
    def E24():
        return choice(resistor.__E24)

    @staticmethod
    def E12():
        return choice(resistor.__E12)

    @classmethod
    def schematic(cls):
        return cls.__SCHEMATIC

    @classmethod
    def E24_Eng(cls):
        '''
            Outputs the resistance of a random E24 resistance in enginnering
            notation, appending the ohms unit and using the default number of
            significant digits
        '''
        return engineerNotation(resistor.E24(), resistor.__UNIT)

    @classmethod
    def E12_Eng(cls):
        '''
            Outputs the resistance of a random E12 resistance in enginnering
            notation, appending the ohms unit and using the default number of
            significant digits
        '''
        return engineerNotation(resistor.E12(), resistor.__UNIT)

    @staticmethod
    def unit():
        return resistor.__UNIT

    @staticmethod
    def series(*args, **kwargs):
        '''
            Computes the series association for a undefined number of arguments
            and returns the equivalent resistance in a resistor object
            The arguments can be either resistor objects, either valid resistance
            values
            The output by default is a float which contains the equivalente
            resistance value in ohms. Nevertheless, if one of the arguments is a
            dictionary with the (key, value) pair is specified as ('resistor', True),
            a resistor object is returned with the label $R_{eq}$ and the minimum
            number of significant digits (read SIGNIFICANT DIGITS for more details)

            SIGNIFICANT DIGITS:
            The number of significant digits of the equivalent resistor is the
            minimum of the significant digits specified in the resistor objects.
            If resistance values without that aren't an resistor object are passed
            by argument, it is considered that they are ideal (having maximum
            precision), therefore don't influenciate the significant digits of
            the equivalent resistor.
            If no resistor object is passed by argument, the number of significant
            digits in the equivalent resistor is the default, 3
        '''
        assert len(args) > 1, "A minimum of two resistors is required for a series association"
        flag = isinstance(args[0], resistor)
        if flag:
            req = float(args[0]._resistance)
            digits = args[0]._digits
        else:
            req = float(args[0])
        for arg in args[1::]:
            if isinstance(arg, resistor):
                req = req + arg._resistance
                if not flag:
                    digits = arg._digits
                    flag = True
                elif arg._digits < digits:
                    digits = arg._digits
            elif resistor.isValidResistor(arg):
                req = req + arg
            else:
                raise InvalidResistor
        if not flag:
            digits = 3
        if kwargs:
            if kwargs['resistor'] == True:
                return resistor(req, "$R_{eq}$", digits)
        else:
            return req

    @staticmethod
    def parallel(*args, **kwargs):
        '''
            Computes the parallel association for a undefined number of arguments
            and returns the equivalent resistance in a resistor object
            The arguments can be either resistor objects, either valid resistance
            values.
            The output by default is a float which contains the equivalente
            resistance value in ohms. Nevertheless, if one of the arguments is a
            dictionary with the (key, value) pair is specified as ('resistor', True),
            a resistor object is returned with the label $R_{eq}$ and the minimum
            number of significant digits (read SIGNIFICANT DIGITS for more details)

            SIGNIFICANT DIGITS:
            The number of significant digits of the equivalent resistor is the
            minimum of the significant digits specified in the resistor objects.
            If resistance values without that aren't an resistor object are passed
            by argument, it is considered that they are ideal (having maximum
            precision), therefore don't influenciate the significant digits of
            the equivalent resistor.
            If no resistor object is passed by argument, the number of significant
            digits in the equivalent resistor is the default, 3
        '''
        assert len(args) > 1, "A minimum of two resistors is required for a parallel association"
        flag = isinstance(args[0], resistor)
        if flag:
            req = float(args[0].resistance)
            digits = args[0].digits
        else:
            req = float(args[0])
        for arg in args[1::]:
            if isinstance(arg, resistor):
                req = req * arg._resistance /(req + arg._resistance)
                if not flag:
                    digits = arg.digits
                    flag = True
                elif arg._digits < digits:
                    digits = arg.digits
            elif resistor.isValidResistor(arg):
                req = req * arg /(req + arg)
            else:
                raise InvalidResistor
        if not flag:
            digits = 3
        if kwargs:
            if kwargs['resistor'] == True:
                return resistor(req, "$R_{eq}$", digits)
        else:
            return req

    @staticmethod
    def voltageDivider(V, R1, R2,label="$V_{eq}$", **kwargs):
        '''
            Computes the voltage drop across the resistor R2 in a voltage divider
            formed by the series association of resistances R1 and R2, such as
            shown below
                                    ---V----R1---+--o
                                                 |
                                                 R2
                                                 |
                                    -------GND---+--o
            "V" can either be a vSource object or a valid voltage value
            R1 and R2 can either be a resistor object or a valid resistance value
        '''
        if  isinstance(V, vSource):
            V = V._voltage
        elif vSource.isValidVSource(V):
            V = float(V)
        else:
            raise InvalidIndependentSource

        if  isinstance(R1, resistor):
            R1 = R1._resistance
        elif resistor.isValidResistor(R1):
            R1 = float(R1)
        else:
            raise InvalidResistor

        if  isinstance(R2, resistor):
            R2 = R2._resistance
        elif resistor.isValidResistor(R2):
            R2 = float(R2)
        else:
            raise InvalidResistor

        if  isinstance(V, vSource) or isinstance((R1, R2),  resistor):
            digits = min(V._digits, R1._digits, R2._digits)
        else:
            digits = 3

        if kwargs:
            if kwargs['vSource'] == True:
                return vSource(R2 / (R1 + R2) * float(V), label, digits)
        return R2 / (R1 + R2)  * float(V)

    @staticmethod
    def currentDivider(I, R1, R2, label="$I_{eq}$", **kwargs):
        '''
            Computes the current that flows trough R2 in a current divider
            formed by the parallel association of resistances R1 and R2, such as
            shown below
                                ---I----+--------+--o
                                        |        |
                                        R1      R2
                                        |        |
                                        +--GND---+--o

            "I" can either be a iSource object or a valid current value
            R1 and R2 can either be a resistor object or a valid resistance value
        '''
        if  isinstance(I, iSource):
            I = I._current
        elif iSource.isValidISource(I):
            I = float(I)
        else:
            raise InvalidIndependentSource

        if  isinstance(R1, resistor):
            R1 = R1._resistance
        elif resistor.isValidResistor(R1):
            R1 = float(R1)
        else:
            raise InvalidResistor

        if  isinstance(R2, resistor):
            R2 = R2._resistance
        elif resistor.isValidResistor(R2):
            R2 = float(R2)
        else:
            raise InvalidResistor

        if  isinstance(I, iSource) or isinstance((R1, R2),  resistor):
            digits = min(I._digits, R1._digits, R2._digits)
        else:
            digits = 3

        if kwargs:
            if kwargs['iSource'] == True:
                return iSource((R1 + R2) / R2 * float(I), label, 3)
        return (R1 + R2) / R2 * float(I)

class InvalidResistor(ValueError, TypeError):
    """
        Resistance must a positive values
        Float or integer are acceptable
    """
    pass
