'''

      _____ _   _ _____  _    _  _____ _______ ____  _____
     |_   _| \ | |  __ \| |  | |/ ____|__   __/ __ \|  __ \
       | | |  \| | |  | | |  | | |       | | | |  | | |__) |
       | | | . ` | |  | | |  | | |       | | | |  | |  _  /
      _| |_| |\  | |__| | |__| | |____   | | | |__| | | \ \
     |_____|_| \_|_____/ \____/ \_____|  |_|  \____/|_|  \_\


    Inductor module for ParamSchemDraw

    A set of classes and methods to ease the drawing and manipulation of inductors.

    Author: Pedro Martins
    version: 0.1.3
'''

from math import floor, log10, pi
from random import randint, choice

from ParamSchemDraw import engineerNotation
from iSource import *
from vSource import *


class inductor(electricComponent):
    '''
        Class used to define an ideal inductor
        It provides static methods to compute a parallel/series association of
        n inductors, a current divider and a voltage divider. It also offers a
        method to check if a number is a valid inductor value
        It can also format the inductor value to enginnering notation
    '''

    def __init__(self, inductance, label= "", digits=3):
        '''
            USAGE: inductor(inductance, label, digits)
                   inductor(inductance, label)
                   inductor(inductance)

            ARGUMENTS:
                inductance -> inductance value for the given inductor element
                label      -> name/identifier of the inductor (optional)
                digits     -> number of significant digits to use in engineering notation

            OUTPUT: an ideal inductor object

            CONSTRAINTS:
                inductance must be a postive number. Float and Integer are supported
                label must be a string
                digits must be a integer in the interval [1, 16]

                other types/values outside the specified will result in
                AssertionError/Exceptions
        '''

        assert isinstance(label, str), "The label element must be a string"
        assert isinstance(digits, int), "The digits element must be an integer"
        assert digits >= 1 and digits <= 16, "The digits element must be between [1, 16]"

        if inductor.isValidInductor(inductance):
            self._inductance = inductance
            self._label      = label
            self._digits     = digits
        else:
            raise InvalidInductor

    __UNIT = '$H$'
    __IMPEDANCE_UNIT = '$\Omega$'
    __ADMITTANCE_UNIT = '$S$'

    # E24 class inductor values
    __E24 = ( 1.0 * 10 ** -9 , 10 * 10 ** -9 , 100 * 10 ** -9 , 1.0 * 10 ** -6 , 10 * 10 ** -6 , 100 * 10 ** -6 , 1.0 * 10 ** -3 , 10 * 10 ** -3 , 100 * 10 ** -3 ,
              1.1 * 10 ** -9 , 11 * 10 ** -9 , 110 * 10 ** -9 , 1.1 * 10 ** -6 , 11 * 10 ** -6 , 110 * 10 ** -6 , 1.1 * 10 ** -3 , 11 * 10 ** -3 , 110 * 10 ** -3 ,
              1.2 * 10 ** -9 , 12 * 10 ** -9 , 120 * 10 ** -9 , 1.2 * 10 ** -6 , 12 * 10 ** -6 , 120 * 10 ** -6 , 1.2 * 10 ** -3 , 12 * 10 ** -3 , 120 * 10 ** -3 ,
              1.3 * 10 ** -9 , 13 * 10 ** -9 , 130 * 10 ** -9 , 1.3 * 10 ** -6 , 13 * 10 ** -6 , 130 * 10 ** -6 , 1.3 * 10 ** -3 , 13 * 10 ** -3 , 130 * 10 ** -3 ,
              1.5 * 10 ** -9 , 15 * 10 ** -9 , 150 * 10 ** -9 , 1.5 * 10 ** -6 , 15 * 10 ** -6 , 150 * 10 ** -6 , 1.5 * 10 ** -3 , 15 * 10 ** -3 , 150 * 10 ** -3 ,
              1.6 * 10 ** -9 , 16 * 10 ** -9 , 160 * 10 ** -9 , 1.6 * 10 ** -6 , 16 * 10 ** -6 , 160 * 10 ** -6 , 1.6 * 10 ** -3 , 16 * 10 ** -3 , 160 * 10 ** -3 ,
              1.8 * 10 ** -9 , 18 * 10 ** -9 , 180 * 10 ** -9 , 1.8 * 10 ** -6 , 18 * 10 ** -6 , 180 * 10 ** -6 , 1.8 * 10 ** -3 , 18 * 10 ** -3 , 180 * 10 ** -3 ,
              2.0 * 10 ** -9 , 20 * 10 ** -9 , 200 * 10 ** -9 , 2.0 * 10 ** -6 , 20 * 10 ** -6 , 200 * 10 ** -6 , 2.0 * 10 ** -3 , 20 * 10 ** -3 , 200 * 10 ** -3 ,
              2.2 * 10 ** -9 , 22 * 10 ** -9 , 220 * 10 ** -9 , 2.2 * 10 ** -6 , 22 * 10 ** -6 , 220 * 10 ** -6 , 2.2 * 10 ** -3 , 22 * 10 ** -3 , 220 * 10 ** -3 ,
              2.4 * 10 ** -9 , 24 * 10 ** -9 , 240 * 10 ** -9 , 2.4 * 10 ** -6 , 24 * 10 ** -6 , 240 * 10 ** -6 , 2.4 * 10 ** -3 , 24 * 10 ** -3 , 240 * 10 ** -3 ,
              2.7 * 10 ** -9 , 27 * 10 ** -9 , 270 * 10 ** -9 , 2.7 * 10 ** -6 , 27 * 10 ** -6 , 270 * 10 ** -6 , 2.7 * 10 ** -3 , 27 * 10 ** -3 , 270 * 10 ** -3 ,
              3.0 * 10 ** -9 , 30 * 10 ** -9 , 300 * 10 ** -9 , 3.0 * 10 ** -6 , 30 * 10 ** -6 , 300 * 10 ** -6 , 3.0 * 10 ** -3 , 30 * 10 ** -3 , 300 * 10 ** -3 ,
              3.3 * 10 ** -9 , 33 * 10 ** -9 , 330 * 10 ** -9 , 3.3 * 10 ** -6 , 33 * 10 ** -6 , 330 * 10 ** -6 , 3.3 * 10 ** -3 , 33 * 10 ** -3 , 330 * 10 ** -3 ,
              3.6 * 10 ** -9 , 36 * 10 ** -9 , 360 * 10 ** -9 , 3.6 * 10 ** -6 , 36 * 10 ** -6 , 360 * 10 ** -6 , 3.6 * 10 ** -3 , 36 * 10 ** -3 , 360 * 10 ** -3 ,
              3.9 * 10 ** -9 , 39 * 10 ** -9 , 390 * 10 ** -9 , 3.9 * 10 ** -6 , 39 * 10 ** -6 , 390 * 10 ** -6 , 3.9 * 10 ** -3 , 39 * 10 ** -3 , 390 * 10 ** -3 ,
              4.3 * 10 ** -9 , 43 * 10 ** -9 , 430 * 10 ** -9 , 4.3 * 10 ** -6 , 43 * 10 ** -6 , 430 * 10 ** -6 , 4.3 * 10 ** -3 , 43 * 10 ** -3 , 430 * 10 ** -3 ,
              4.7 * 10 ** -9 , 47 * 10 ** -9 , 470 * 10 ** -9 , 4.7 * 10 ** -6 , 47 * 10 ** -6 , 470 * 10 ** -6 , 4.7 * 10 ** -3 , 47 * 10 ** -3 , 470 * 10 ** -3 ,
              5.1 * 10 ** -9 , 51 * 10 ** -9 , 510 * 10 ** -9 , 5.1 * 10 ** -6 , 51 * 10 ** -6 , 510 * 10 ** -6 , 5.1 * 10 ** -3 , 51 * 10 ** -3 , 510 * 10 ** -3 ,
              5.6 * 10 ** -9 , 56 * 10 ** -9 , 560 * 10 ** -9 , 5.6 * 10 ** -6 , 56 * 10 ** -6 , 560 * 10 ** -6 , 5.6 * 10 ** -3 , 56 * 10 ** -3 , 560 * 10 ** -3 ,
              6.2 * 10 ** -9 , 62 * 10 ** -9 , 620 * 10 ** -9 , 6.2 * 10 ** -6 , 62 * 10 ** -6 , 620 * 10 ** -6 , 6.2 * 10 ** -3 , 62 * 10 ** -3 , 620 * 10 ** -3 ,
              6.8 * 10 ** -9 , 68 * 10 ** -9 , 680 * 10 ** -9 , 6.8 * 10 ** -6 , 68 * 10 ** -6 , 680 * 10 ** -6 , 6.8 * 10 ** -3 , 68 * 10 ** -3 , 680 * 10 ** -3 ,
              7.5 * 10 ** -9 , 75 * 10 ** -9 , 750 * 10 ** -9 , 7.5 * 10 ** -6 , 75 * 10 ** -6 , 750 * 10 ** -6 , 7.5 * 10 ** -3 , 75 * 10 ** -3 , 750 * 10 ** -3 ,
              8.2 * 10 ** -9 , 82 * 10 ** -9 , 820 * 10 ** -9 , 8.2 * 10 ** -6 , 82 * 10 ** -6 , 820 * 10 ** -6 , 8.2 * 10 ** -3 , 82 * 10 ** -3 , 820 * 10 ** -3 ,
              9.1 * 10 ** -9 , 91 * 10 ** -9 , 910 * 10 ** -9 , 9.1 * 10 ** -6 , 91 * 10 ** -6 , 910 * 10 ** -6 , 9.1 * 10 ** -3 , 91 * 10 ** -3 , 910 * 10 ** -3 )

    # E12 class inductor values
    __E12 = ( 1.0 * 10 ** -9 , 10 * 10 ** -9 , 100 * 10 ** -9 , 1.0 * 10 ** -6 , 10 * 10 ** -6 , 100 * 10 ** -6 , 1.0 * 10 ** -3 , 10 * 10 ** -3 , 100 * 10 ** -3 ,
              1.2 * 10 ** -9 , 12 * 10 ** -9 , 120 * 10 ** -9 , 1.2 * 10 ** -6 , 12 * 10 ** -6 , 120 * 10 ** -6 , 1.2 * 10 ** -3 , 12 * 10 ** -3 , 120 * 10 ** -3 ,
              1.5 * 10 ** -9 , 15 * 10 ** -9 , 150 * 10 ** -9 , 1.5 * 10 ** -6 , 15 * 10 ** -6 , 150 * 10 ** -6 , 1.5 * 10 ** -3 , 15 * 10 ** -3 , 150 * 10 ** -3 ,
              1.8 * 10 ** -9 , 18 * 10 ** -9 , 180 * 10 ** -9 , 1.8 * 10 ** -6 , 18 * 10 ** -6 , 180 * 10 ** -6 , 1.8 * 10 ** -3 , 18 * 10 ** -3 , 180 * 10 ** -3 ,
              2.2 * 10 ** -9 , 22 * 10 ** -9 , 220 * 10 ** -9 , 2.2 * 10 ** -6 , 22 * 10 ** -6 , 220 * 10 ** -6 , 2.2 * 10 ** -3 , 22 * 10 ** -3 , 220 * 10 ** -3 ,
              2.7 * 10 ** -9 , 27 * 10 ** -9 , 270 * 10 ** -9 , 2.7 * 10 ** -6 , 27 * 10 ** -6 , 270 * 10 ** -6 , 2.7 * 10 ** -3 , 27 * 10 ** -3 , 270 * 10 ** -3 ,
              3.3 * 10 ** -9 , 33 * 10 ** -9 , 330 * 10 ** -9 , 3.3 * 10 ** -6 , 33 * 10 ** -6 , 330 * 10 ** -6 , 3.3 * 10 ** -3 , 33 * 10 ** -3 , 330 * 10 ** -3 ,
              3.9 * 10 ** -9 , 39 * 10 ** -9 , 390 * 10 ** -9 , 3.9 * 10 ** -6 , 39 * 10 ** -6 , 390 * 10 ** -6 , 3.9 * 10 ** -3 , 39 * 10 ** -3 , 330 * 10 ** -3 ,
              4.7 * 10 ** -9 , 47 * 10 ** -9 , 470 * 10 ** -9 , 4.7 * 10 ** -6 , 47 * 10 ** -6 , 470 * 10 ** -6 , 4.7 * 10 ** -3 , 47 * 10 ** -3 , 470 * 10 ** -3 ,
              5.6 * 10 ** -9 , 56 * 10 ** -9 , 560 * 10 ** -9 , 5.6 * 10 ** -6 , 56 * 10 ** -6 , 560 * 10 ** -6 , 5.6 * 10 ** -3 , 56 * 10 ** -3 , 560 * 10 ** -3 ,
              6.8 * 10 ** -9 , 68 * 10 ** -9 , 680 * 10 ** -9 , 6.8 * 10 ** -6 , 68 * 10 ** -6 , 680 * 10 ** -6 , 6.8 * 10 ** -3 , 68 * 10 ** -3 , 680 * 10 ** -3 ,
              8.2 * 10 ** -9 , 82 * 10 ** -9 , 820 * 10 ** -9 , 8.2 * 10 ** -6 , 82 * 10 ** -6 , 820 * 10 ** -6 , 8.2 * 10 ** -3 , 82 * 10 ** -3 , 820 * 10 ** -3 )

    @property
    def inductance(self):
        return self._inductance

    @property
    def inductanceEng(self):
        '''
            Outputs the inductance of the inductor in enginnering notation,
            appending the Henry unit and using the significant number of digits
            defined when the object was created
        '''
        return engineerNotation(self._inductance, 'H', self._digits)

    def reactance(self, frequency, angular=False):
        assert frequency >= 0, "The frequency must be a positive value"

        if frequency == float('inf'):
            return float('inf')
        elif angular:
            return frequency*self._inductance
        else:
            return 2*pi*frequency*self._inductance

    def reactanceEng(self, frequency, angular=False, latex=True):
        '''
            Outputs the reactance of the inductor in engineering notation,
            appending the Ohm unit and using the significant number of digits
            defined when the object was created

            The latex argument controls the wrapping of the unit. If latex=False,
            then the unit has no equation latex marker, '$', wrapping the latex command
            for the greek Omega letter. If latex=True, it does and the unit is $\Omega$
        '''
        unit = inductor.__IMPEDANCE_UNIT if latex else '\Omega'

        return engineerNotation(self.reactance(frequency, angular=angular), unit, self._digits)

    def impedance(self, frequency, angular=False):
        return complex(0, self.reactance(frequency, angular))

    def impedanceEng(self, frequency, angular=False, latex=True):
        '''
            Outputs the impedance of the inductor in enginnering notation,
            appending the Ohm unit and using the significant number of digits
            defined when the object was created

            The latex argument controls the wrapping of the unit. If latex=False,
            then the unit has no equation latex marker, '$', wrapping the latex command
            for the greek Omega letter. If latex=True, it does and the unit is $\Omega$
        '''
        unit = inductor.__IMPEDANCE_UNIT if latex else '\Omega'
        value = self.impedance(frequency, angular=angular)
        if value == complex(0, float('inf')):
            return '$\inf$' if latex else '\inf'
        else:
            return engineerNotation(value, unit, self._digits)

    def susceptance(self, frequency, angular=False):
        assert frequency > 0, "The frequency must be a positive value"

        if frequency == 0:
            return 0
        elif angular:
            return -1.0/(frequency*self._inductance)
        else:
            return -1.0/(2*pi*frequency*self._inductance)

    def susceptanceEng(self, frequency, angular=False, latex=True):
        '''
            Outputs the susceptance of the inductor in enginnering notation,
            appending the Siemens unit and using the significant number of digits
            defined when the object was created

            The latex argument controls the wrapping of the unit. If latex=False,
            then the unit has no equation latex marker, '$', wrapping the latex command
            for the greek Omega letter. If latex=True, it does and the unit is $\Omega$
        '''

        value = self.susceptance(frequency, angular)
        if value == complex(0, float('inf')):
            return '$\inf$' if latex else '\inf'
        else:
            return engineerNotation(value, 'S', self._digits)

    def admittance(self, frequency, angular=False):
        assert frequency > 0, "The frequency must be a positive value"

        return complex(0, self.susceptance(frequency, angular))

    def admittanceEng(self, frequency, angular=False, latex=True):
        '''
            Outputs the susceptance of the inductor in enginnering notation,
            appending the Siemens unit and using the significant number of digits
            defined when the object was created

            The latex argument controls the wrapping of the unit. If latex=False,
            then the unit has no equation latex marker, '$', wrapping the latex command
            for the greek Omega letter. If latex=True, it does and the unit is $\Omega$
        '''

        value = self.admittance(frequency, angular)
        if value == complex(0, float('inf')):
            return '$\inf$' if latex else '\inf'
        else:
            return engineerNotation(value, 'S', self._digits)

    @property
    def label(self):
        return self._label

    @label.setter
    def label(self, label):
        assert isinstance(label, str), "The label of the inductor must be a string"
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
    def isValidInductor(L):
        '''
            Check if L is a valid value for inductance.
            It must be a positive integer or float
        '''
        if isinstance(L, (int, float)):
            if L > 0:
                return True
        return False

    @staticmethod
    def E24():
        return choice(inductor.__E24)

    @staticmethod
    def E12():
        return choice(inductor.__E12)

    @classmethod
    def E24_Eng(cls):
        '''
            Outputs the inductance of a random E24 inductor in enginnering
            notation, appending the ohms unit and using the default number of
            significant digits
        '''
        return engineerNotation(inductor.E24(), inductor.__UNIT)

    @classmethod
    def E12_Eng(cls):
        '''
            Outputs the inductance of a random E12 inductor in enginnering
            notation, appending the ohms unit and using the default number of
            significant digits
        '''
        return engineerNotation(inductor.E12(), inductor.__UNIT)

    @staticmethod
    def unit():
        return inductor.__UNIT

    @staticmethod
    def impedance_unit():
        return inductor.__IMPEDANCE_UNIT

    @staticmethod
    def admittance_unit():
        return inductor.__ADMITTANCE_UNIT

    @staticmethod
    def series(*args, **kwargs):
        '''
            Computes the series association for a undefined number of arguments
            and returns the equivalent inductance in a inductor object
            The arguments can be either inductor objects, either valid inductance
            values.
            The output by default is a float which contains the equivalent
            inductance value in Farads. Nevertheless, if one of the arguments is a
            dictionary with the (key, value) pair is specified as ('inductor', True),
            a inductor object is returned with the label $L_{eq}$ and the minimum
            number of significant digits (read SIGNIFICANT DIGITS for more details)

            SIGNIFICANT DIGITS:
            The number of significant digits of the equivalent inductor is the
            minimum of the significant digits specified in the inductor objects.
            If inductance values that aren't an inductor object are passed
            by argument, it is considered that they are ideal (having maximum
            precision), therefore don't influenciate the significant digits of
            the equivalent inductance.
            If no inductor object is passed by argument, the number of significant
            digits in the equivalent inductance is the default, 3
        '''

        assert len(args) > 1, "A minimum of two inductors is required for a parallel association"
        flag = isinstance(args[0], inductor)
        if flag:
            Leq = float(args[0]._inductance)
            digits = args[0]._digits
        else:
            Leq = float(args[0])
        for arg in args[1::]:
            if isinstance(arg, inductor):
                Leq = Leq + arg._inductance
                if not flag:
                    digits = arg._digits
                    flag = True
                elif arg._digits < digits:
                    digits = arg._digits
            elif inductor.isValidInductor(arg):
                Leq = Leq + arg
            else:
                raise InvalidInductor
        if not flag:
            digits = 3
        if kwargs:
            if kwargs['inductor'] == True:
                return inductor(Leq, "$L_{eq}$", digits)
        else:
            return Leq

    @staticmethod
    def parallel(*args, **kwargs):
        '''
            Computes the parallel association for a undefined number of arguments
            and returns the equivalent inductance in a inductor object
            The arguments can be either inductor objects, either valid inductance
            values
            The output by default is a float which contains the equivalente
            inductance value in Farads. Nevertheless, if one of the arguments is a
            dictionary with the (key, value) pair is specified as ('inductor', True),
            a inductor object is returned with the label $L_{eq}$ and the minimum
            number of significant digits (read SIGNIFICANT DIGITS for more details)

            SIGNIFICANT DIGITS:
            The number of significant digits of the equivalent inductor is the
            minimum of the significant digits specified in the inductor objects.
            If inductance values that aren't an inductor object are passed
            by argument, it is considered that they are ideal (having maximum
            precision), therefore don't influenciate the significant digits of
            the equivalent inductance.
            If no inductor object is passed by argument, the number of significant
            digits in the equivalent inductance is the default, 3
        '''
        assert len(args) > 1, "A minimum of two inductors is required for a series association"
        flag = isinstance(args[0], inductor)
        if flag:
            Leq = float(args[0]._inductance)
            digits = args[0].digits
        else:
            Leq = float(args[0])
        for arg in args[1::]:
            if isinstance(arg, inductor):
                Leq = Leq * arg._inductance /(Leq + arg._inductance)
                if not flag:
                    digits = arg.digits
                    flag = True
                elif arg._digits < digits:
                    digits = arg.digits
            elif inductor.isValidInductor(arg):
                Leq = Leq * arg /(Leq + arg)
            else:
                raise InvalidInductor
        if not flag:
            digits = 3
        if kwargs:
            if kwargs['inductor'] == True:
                return inductor(Leq, "$L_{eq}$", digits)
        else:
            return Leq

    @staticmethod
    def voltageDivider(V, L1, L2, frequency, angular=False, label="$V_{eq}$", **kwargs):
        '''
            Computes the voltage drop across the impedance of the inductor L2
            in a voltage divider formed by the series association of the inductors
            L1 and L2, such as shown below
                                    ---V----L1---+--o
                                                 |
                                                 L2
                                                 |
                                    -------GND---+--o
            "V" can either be a vSource object or a valid voltage value
            L1 and L2 can either be a inductor object or a valid inductance value
        '''
        assert frequency > 0, 'The frequency must be a positive value'

        if  isinstance(V, vSource):
            V = V._voltage
        elif vSource.isValidVSource(V):
            V = float(V)
        else:
            raise InvalidIndependentSource

        if  isinstance(L1, inductor):
            ZL1 = ZL1.impedance(frequency, angular)
        elif inductor.isValidInductor(L1):
            ZL1 = complex(0, (2*pi*frequency*L1))
        else:
            raise InvalidInductor

        if  isinstance(L2, inductor):
            ZL2 = L2.impedance(frequency, angular)
        elif inductor.isValidInductor(L2):
            ZL2 = complex(0, (2*pi*frequency*L2))
        else:
            raise InvalidInductor

        if  isinstance(V, vSource) or isinstance((L1, L2),  inductor):
            digits = min(V._digits, R1._digits, R2._digits)
        else:
            digits = 3

        if kwargs:
            if kwargs['vSource'] == True:
                return vSource(ZL2 / (ZL1 + ZL2) * float(V), label, digits)
        return ZL2 / (ZL1 + ZL2) * float(V)

    @staticmethod
    def currentDivider(I, L1, L2, frequency, angular=False, label="$I_{eq}$", **kwargs):
        '''
            Computes the current that flows trough L2 in a current divider
            formed by the parallel association of the inductors L1 and L2, such as
            shown below
                                ---I----+--------+--o
                                        |        |
                                        L1      L2
                                        |        |
                                        +--GND---+--o

            "I" can either be a iSource object or a valid current value
            L1 and L2 can either be a inductor object or a valid inductance value
        '''
        assert frequency >= 0, 'The frequency must be a positive value'

        if  isinstance(I, iSource):
            I = I._current
        elif iSource.isValidISource(I):
            I = float(I)
        else:
            raise InvalidIndependentSource

        if  isinstance(L1, inductor):
            ZL1 = ZL1.impedance(frequency, angular)
        elif inductor.isValidInductor(L1):
            ZL1 = complex(0, -1.0/(2*pi*frequency*L1))
        else:
            raise InvalidInductor

        if  isinstance(L2, inductor):
            ZL2 = L2.impedance(frequency, angular)
        elif inductor.isValidInductor(L2):
            ZL2 = 1.0/complex(0, -1.0/(2*pi*frequency*L2))
        else:
            raise InvalidInductor

        if  isinstance(I, iSource) or isinstance((L1, L2),  inductor):
            digits = min(I._digits, L1._digits, L2._digits)
        else:
            digits = 3

        if kwargs:
            if kwargs['iSource'] == True:
                return iSource((ZL1 + ZL2) / ZL2 * float(I), label, 3)
        return (ZL1 + ZL2) / ZL2 * float(I)


class InvalidInductor(ValueError, TypeError):
    """
        Inductance must be a positive values
        Float or integer are acceptable
    """
    pass
