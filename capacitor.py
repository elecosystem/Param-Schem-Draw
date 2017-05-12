'''
       _____            _____          _____  _____  _______  ____   _____
      / ____|    /\    |  __ \  /\    / ____||_   _||__   __|/ __ \ |  __ \
     | |        /  \   | |__) |/  \  | |       | |     | |  | |  | || |__) |
     | |       / /\ \  |  ___// /\ \ | |       | |     | |  | |  | ||  _  /
     | |____  / ____ \ | |   / ____ \| |____  _| |_    | |  | |__| || | \ \
      \_____|/_/    \_\|_|  /_/    \_\\_____||_____|   |_|   \____/ |_|  \_\



    Capacitor module for ParamSchemDraw

    A set of classes and methods to ease the drawing and manipulation of capacitors.

    Author: Pedro Martins
    version: 0.1.3
'''

from math import floor, log10, pi
from random import randint, choice

from ParamSchemDraw import engineerNotation
from iSource import *
from vSource import *


class capacitor(electricComponent):
    '''
        Class used to define an ideal capacitor
        It provides static methods to compute a parallel/series association of
        n capacitors, a current divider and a voltage divider. It also offers a
        method to check if a number is a valid capacitor value
        It can also format the capacitor value to enginnering notation
    '''

    def __init__(self, capacitance, label= "", digits=3):
        '''
            USAGE: capacitor(capacitance, label, digits)
                   capacitor(capacitance, label)
                   capacitor(capacitance)

            ARGUMENTS:
                capacitance -> capacitance value for the given capacitor element
                label       -> name/identifier of the capacitor (optional)
                digits      -> number of significant digits to use in engineering notation

            OUTPUT: an ideal capacitor object

            CONSTRAINTS:
                capacitance must be a postive number. Float and Integer are supported
                label must be a string
                digits must be a integer in the interval [1, 16]

                other types/values outside the specified will result in
                AssertionError/Exceptions
        '''

        assert isinstance(label, str), "The label element must be a string"
        assert isinstance(digits, int), "The digits element must be an integer"
        assert digits >= 1 and digits <= 16, "The digits element must be between [1, 16]"

        if capacitor.isValidCapacitor(capacitance):
            self._capacitance  = capacitance
            self._label       = label
            self._digits      = digits
        else:
            raise InvalidCapacitor

    __UNIT = '$F$'
    __IMPEDANCE_UNIT = '$\Omega$'
    __ADMITTANCE_UNIT = '$S$'

    # E24 class capacitor values
    __E24 = ( 1.0 * 10 ** -12 , 10 * 10 ** -12 , 100 * 10 ** -12 , 1.0 * 10 ** -9 , 10 * 10 ** -9 , 100 * 10 ** -9 , 1.0 * 10 ** -6 , 10 * 10 ** -6 , 100 * 10 ** -6,
              1.1 * 10 ** -12 , 11 * 10 ** -12 , 110 * 10 ** -12 , 1.1 * 10 ** -9 , 11 * 10 ** -9 , 110 * 10 ** -9 , 1.1 * 10 ** -6 , 11 * 10 ** -6 , 110 * 10 ** -6,
              1.2 * 10 ** -12 , 12 * 10 ** -12 , 120 * 10 ** -12 , 1.2 * 10 ** -9 , 12 * 10 ** -9 , 120 * 10 ** -9 , 1.2 * 10 ** -6 , 12 * 10 ** -6 , 120 * 10 ** -6,
              1.3 * 10 ** -12 , 13 * 10 ** -12 , 130 * 10 ** -12 , 1.3 * 10 ** -9 , 13 * 10 ** -9 , 130 * 10 ** -9 , 1.3 * 10 ** -6 , 13 * 10 ** -6 , 130 * 10 ** -6,
              1.5 * 10 ** -12 , 15 * 10 ** -12 , 150 * 10 ** -12 , 1.5 * 10 ** -9 , 15 * 10 ** -9 , 150 * 10 ** -9 , 1.5 * 10 ** -6 , 15 * 10 ** -6 , 150 * 10 ** -6,
              1.6 * 10 ** -12 , 16 * 10 ** -12 , 160 * 10 ** -12 , 1.6 * 10 ** -9 , 16 * 10 ** -9 , 160 * 10 ** -9 , 1.6 * 10 ** -6 , 16 * 10 ** -6 , 160 * 10 ** -6,
              1.8 * 10 ** -12 , 18 * 10 ** -12 , 180 * 10 ** -12 , 1.8 * 10 ** -9 , 18 * 10 ** -9 , 180 * 10 ** -9 , 1.8 * 10 ** -6 , 18 * 10 ** -6 , 180 * 10 ** -6,
              2.0 * 10 ** -12 , 20 * 10 ** -12 , 200 * 10 ** -12 , 2.0 * 10 ** -9 , 20 * 10 ** -9 , 200 * 10 ** -9 , 2.0 * 10 ** -6 , 20 * 10 ** -6 , 200 * 10 ** -6,
              2.2 * 10 ** -12 , 22 * 10 ** -12 , 220 * 10 ** -12 , 2.2 * 10 ** -9 , 22 * 10 ** -9 , 220 * 10 ** -9 , 2.2 * 10 ** -6 , 22 * 10 ** -6 , 220 * 10 ** -6,
              2.4 * 10 ** -12 , 24 * 10 ** -12 , 240 * 10 ** -12 , 2.4 * 10 ** -9 , 24 * 10 ** -9 , 240 * 10 ** -9 , 2.4 * 10 ** -6 , 24 * 10 ** -6 , 240 * 10 ** -6,
              2.7 * 10 ** -12 , 27 * 10 ** -12 , 270 * 10 ** -12 , 2.7 * 10 ** -9 , 27 * 10 ** -9 , 270 * 10 ** -9 , 2.7 * 10 ** -6 , 27 * 10 ** -6 , 270 * 10 ** -6,
              3.0 * 10 ** -12 , 30 * 10 ** -12 , 300 * 10 ** -12 , 3.0 * 10 ** -9 , 30 * 10 ** -9 , 300 * 10 ** -9 , 3.0 * 10 ** -6 , 30 * 10 ** -6 , 300 * 10 ** -6,
              3.3 * 10 ** -12 , 33 * 10 ** -12 , 330 * 10 ** -12 , 3.3 * 10 ** -9 , 33 * 10 ** -9 , 330 * 10 ** -9 , 3.3 * 10 ** -6 , 33 * 10 ** -6 , 330 * 10 ** -6,
              3.6 * 10 ** -12 , 36 * 10 ** -12 , 360 * 10 ** -12 , 3.6 * 10 ** -9 , 36 * 10 ** -9 , 360 * 10 ** -9 , 3.6 * 10 ** -6 , 36 * 10 ** -6 , 360 * 10 ** -6,
              3.9 * 10 ** -12 , 39 * 10 ** -12 , 390 * 10 ** -12 , 3.9 * 10 ** -9 , 39 * 10 ** -9 , 390 * 10 ** -9 , 3.9 * 10 ** -6 , 39 * 10 ** -6 , 390 * 10 ** -6,
              4.3 * 10 ** -12 , 43 * 10 ** -12 , 430 * 10 ** -12 , 4.3 * 10 ** -9 , 43 * 10 ** -9 , 430 * 10 ** -9 , 4.3 * 10 ** -6 , 43 * 10 ** -6 , 430 * 10 ** -6,
              4.7 * 10 ** -12 , 47 * 10 ** -12 , 470 * 10 ** -12 , 4.7 * 10 ** -9 , 47 * 10 ** -9 , 470 * 10 ** -9 , 4.7 * 10 ** -6 , 47 * 10 ** -6 , 470 * 10 ** -6,
              5.1 * 10 ** -12 , 51 * 10 ** -12 , 510 * 10 ** -12 , 5.1 * 10 ** -9 , 51 * 10 ** -9 , 510 * 10 ** -9 , 5.1 * 10 ** -6 , 51 * 10 ** -6 , 510 * 10 ** -6,
              5.6 * 10 ** -12 , 56 * 10 ** -12 , 560 * 10 ** -12 , 5.6 * 10 ** -9 , 56 * 10 ** -9 , 560 * 10 ** -9 , 5.6 * 10 ** -6 , 56 * 10 ** -6 , 560 * 10 ** -6,
              6.2 * 10 ** -12 , 62 * 10 ** -12 , 620 * 10 ** -12 , 6.2 * 10 ** -9 , 62 * 10 ** -9 , 620 * 10 ** -9 , 6.2 * 10 ** -6 , 62 * 10 ** -6 , 620 * 10 ** -6,
              6.8 * 10 ** -12 , 68 * 10 ** -12 , 680 * 10 ** -12 , 6.8 * 10 ** -9 , 68 * 10 ** -9 , 680 * 10 ** -9 , 6.8 * 10 ** -6 , 68 * 10 ** -6 , 680 * 10 ** -6,
              7.5 * 10 ** -12 , 75 * 10 ** -12 , 750 * 10 ** -12 , 7.5 * 10 ** -9 , 75 * 10 ** -9 , 750 * 10 ** -9 , 7.5 * 10 ** -6 , 75 * 10 ** -6 , 750 * 10 ** -6,
              8.2 * 10 ** -12 , 82 * 10 ** -12 , 820 * 10 ** -12 , 8.2 * 10 ** -9 , 82 * 10 ** -9 , 820 * 10 ** -9 , 8.2 * 10 ** -6 , 82 * 10 ** -6 , 820 * 10 ** -6,
              9.1 * 10 ** -12 , 91 * 10 ** -12 , 910 * 10 ** -12 , 9.1 * 10 ** -9 , 91 * 10 ** -9 , 910 * 10 ** -9 , 9.1 * 10 ** -6 , 91 * 10 ** -6 , 910 * 10 ** -6 )

    # E12 class capacitor values
    __E12 = ( 1.0 * 10 ** -12 , 10 * 10 ** -12 , 100 * 10 ** -12 , 1.0 * 10 ** -9 , 10 * 10 ** -9 , 100 * 10 ** -9 , 1.0 * 10 ** -6 , 10 * 10 ** -6 , 100 * 10 ** -6,
              1.2 * 10 ** -12 , 12 * 10 ** -12 , 120 * 10 ** -12 , 1.2 * 10 ** -9 , 12 * 10 ** -9 , 120 * 10 ** -9 , 1.2 * 10 ** -6 , 12 * 10 ** -6 , 120 * 10 ** -6,
              1.5 * 10 ** -12 , 15 * 10 ** -12 , 150 * 10 ** -12 , 1.5 * 10 ** -9 , 15 * 10 ** -9 , 150 * 10 ** -9 , 1.5 * 10 ** -6 , 15 * 10 ** -6 , 150 * 10 ** -6,
              1.8 * 10 ** -12 , 18 * 10 ** -12 , 180 * 10 ** -12 , 1.8 * 10 ** -9 , 18 * 10 ** -9 , 180 * 10 ** -9 , 1.8 * 10 ** -6 , 18 * 10 ** -6 , 180 * 10 ** -6,
              2.2 * 10 ** -12 , 22 * 10 ** -12 , 220 * 10 ** -12 , 2.2 * 10 ** -9 , 22 * 10 ** -9 , 220 * 10 ** -9 , 2.2 * 10 ** -6 , 22 * 10 ** -6 , 220 * 10 ** -6,
              2.7 * 10 ** -12 , 27 * 10 ** -12 , 270 * 10 ** -12 , 2.7 * 10 ** -9 , 27 * 10 ** -9 , 270 * 10 ** -9 , 2.7 * 10 ** -6 , 27 * 10 ** -6 , 270 * 10 ** -6,
              3.3 * 10 ** -12 , 33 * 10 ** -12 , 330 * 10 ** -12 , 3.3 * 10 ** -9 , 33 * 10 ** -9 , 330 * 10 ** -9 , 3.3 * 10 ** -6 , 33 * 10 ** -6 , 330 * 10 ** -6,
              3.9 * 10 ** -12 , 39 * 10 ** -12 , 330 * 10 ** -12 , 3.9 * 10 ** -9 , 39 * 10 ** -9 , 390 * 10 ** -9 , 3.9 * 10 ** -6 , 39 * 10 ** -6 , 390 * 10 ** -6,
              4.7 * 10 ** -12 , 47 * 10 ** -12 , 470 * 10 ** -12 , 4.7 * 10 ** -9 , 47 * 10 ** -9 , 470 * 10 ** -9 , 4.7 * 10 ** -6 , 47 * 10 ** -6 , 470 * 10 ** -6,
              5.6 * 10 ** -12 , 56 * 10 ** -12 , 560 * 10 ** -12 , 5.6 * 10 ** -9 , 56 * 10 ** -9 , 560 * 10 ** -9 , 5.6 * 10 ** -6 , 56 * 10 ** -6 , 560 * 10 ** -6,
              6.8 * 10 ** -12 , 68 * 10 ** -12 , 680 * 10 ** -12 , 6.8 * 10 ** -9 , 68 * 10 ** -9 , 680 * 10 ** -9 , 6.8 * 10 ** -6 , 68 * 10 ** -6 , 680 * 10 ** -6,
              8.2 * 10 ** -12 , 82 * 10 ** -12 , 820 * 10 ** -12 , 8.2 * 10 ** -9 , 82 * 10 ** -9 , 820 * 10 ** -9 , 8.2 * 10 ** -6 , 82 * 10 ** -6 , 820 * 10 ** -6 )

    @property
    def capacitance(self):
        return self._capacitance

    @property
    def capacitanceEng(self):
        '''
            Outputs the capacitance of the capacitor in enginnering notation,
            appending the Farad unit and using the significant number of digits
            defined when the object was created
        '''
        return engineerNotation(self._capacitance, 'F', self._digits)

    def reactance(self, frequency, angular=False):
        assert frequency >= 0, "The frequency must be a positive value"

        if frequency == 0:
            return float('inf')
        elif angular:
            return -1.0/(frequency*self._capacitance)
        else:
            return -1.0/(2*pi*frequency*self._capacitance)

    def reactanceEng(self, frequency, angular=False, latex=True):
        '''
            Outputs the reactance of the capacitor in engineering notation,
            appending the Ohm unit and using the significant number of digits
            defined when the object was created

            The latex argument controls the wrapping of the unit. If latex=False,
            then the unit has no equation latex marker, '$', wrapping the latex command
            for the greek Omega letter. If latex=True, it does and the unit is $\Omega$
        '''
        unit = capacitor.__IMPEDANCE_UNIT if latex else '\Omega'

        return engineerNotation(self.reactance(frequency, angular=angular), unit, self._digits)

    def impedance(self, frequency, angular=False):
        return complex(0, self.reactance(frequency, angular))

    def impedanceEng(self, frequency, angular=False, latex=True):
        '''
            Outputs the impedance of the capacitor in enginnering notation,
            appending the Ohm unit and using the significant number of digits
            defined when the object was created

            The latex argument controls the wrapping of the unit. If latex=False,
            then the unit has no equation latex marker, '$', wrapping the latex command
            for the greek Omega letter. If latex=True, it does and the unit is $\Omega$
        '''
        unit = capacitor.__IMPEDANCE_UNIT if latex else '\Omega'
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
            return frequency*self._capacitance
        else:
            return 2*pi*frequency*self._capacitance

    def susceptanceEng(self, frequency, angular=False, latex=True):
        '''
            Outputs the susceptance of the capacitor in enginnering notation,
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
            Outputs the susceptance of the capacitor in enginnering notation,
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
        assert isinstance(label, str), "The label of the capacitor must be a string"
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
    def isValidCapacitor(C):
        '''
            Check if C is a valid value for capacitance.
            It must be a positive integer or float
        '''
        if isinstance(C, (int, float)):
            if C > 0:
                return True
        return False

    @staticmethod
    def E24():
        return choice(capacitor.__E24)

    @staticmethod
    def E12():
        return choice(capacitor.__E12)

    @classmethod
    def E24_Eng(cls):
        '''
            Outputs the capacitance of a random E24 capacitor in enginnering
            notation, appending the ohms unit and using the default number of
            significant digits
        '''
        return engineerNotation(capacitor.E24(), capacitor.__UNIT)

    @classmethod
    def E12_Eng(cls):
        '''
            Outputs the capacitance of a random E12 capacitor in enginnering
            notation, appending the ohms unit and using the default number of
            significant digits
        '''
        return engineerNotation(capacitor.E12(), capacitor.__UNIT)

    @classmethod
    def chargeEq(cls, **kwargs):
        '''
            Computes the relation between electric charge, capacitance and voltage
            at the terminals of a capacitor

            The keys must be strings and the values must be integers or floats
            Everything else will return an Assertion error

            The keys must be two of the following: 'charge', 'capacitance' and
            'voltage' and must be strings.
            Everything else will return a KeyError exception

        '''

        assert kwargs
        assert len(kwargs) == 2
        for value in kwargs.values(): assert isinstance(value, (int, float))
        for key in kwargs.keys(): assert isinstance(key, (str))

        if 'charge' in kwargs.keys() and 'capacitance' in kwargs.keys():      # returns Voltage
            value = float(kwargs['charge']) / kwargs['capacitance']
        elif 'charge' in kwargs.keys() and 'voltage' in kwargs.keys():        # returns Capacitance
            value = float(kwargs['charge']) / kwargs['voltage']
        elif 'capacitance' in kwargs.keys() and 'voltage' in kwargs.keys():   # returns charge
            value = float(kwargs['capacitance']) * kwargs['voltage']

        return value

    @classmethod
    def chargeEqEng(cls, **kwargs):
        '''
            Computes the relation between electric charge, capacitance and voltage
            at the terminals of a capacitor and returns the value formatted in
            enginnering Notation using the correspondent unit

            The keys must be strings and the values must be integers or floats
            Everything else will return an Assertion error

            The keys must be two of the following: 'charge', 'capacitance' and
            'voltage' and must be strings.
            Everything else will return a KeyError exception

        '''

        assert kwargs
        assert len(kwargs) == 2
        for value in kwargs.values(): assert isinstance(value, (int, float))
        for key in kwargs.keys(): assert isinstance(key, (str))

        if 'charge' in kwargs.keys() and 'capacitance' in kwargs.keys():      # returns Voltage
            value = float(kwargs['charge']) / kwargs['capacitance']
            unit = 'V'
        elif 'charge' in kwargs.keys() and 'voltage' in kwargs.keys():        # returns Capacitance
            value = float(kwargs['charge']) / kwargs['voltage']
            unit = capacitor.__UNIT
        elif 'capacitance' in kwargs.keys() and 'voltage' in kwargs.keys():   # returns charge
            value = float(kwargs['capacitance']) * kwargs['voltage']
            unit = 'C'

        return engineerNotation(value, unit)

    @staticmethod
    def unit():
        return capacitor.__UNIT

    @staticmethod
    def impedance_unit():
        return capacitor.__IMPEDANCE_UNIT

    @staticmethod
    def admittance_unit():
        return capacitor.__ADMITTANCE_UNIT

    @staticmethod
    def series(*args, **kwargs):
        '''
            Computes the series association for a undefined number of arguments
            and returns the equivalent capacitance in a capacitor object
            The arguments can be either capacitor objects, either valid capacitance
            values
            The output by default is a float which contains the equivalente
            capacitance value in Farads. Nevertheless, if one of the arguments is a
            dictionary with the (key, value) pair is specified as ('capacitor', True),
            a capacitor object is returned with the label $C_{eq}$ and the minimum
            number of significant digits (read SIGNIFICANT DIGITS for more details)

            SIGNIFICANT DIGITS:
            The number of significant digits of the equivalent capacitor is the
            minimum of the significant digits specified in the capacitor objects.
            If capacitance values that aren't an capacitor object are passed
            by argument, it is considered that they are ideal (having maximum
            precision), therefore don't influenciate the significant digits of
            the equivalent capacitance.
            If no capacitor object is passed by argument, the number of significant
            digits in the equivalent capacitance is the default, 3
        '''
        assert len(args) > 1, "A minimum of two capacitors is required for a series association"
        flag = isinstance(args[0], capacitor)
        if flag:
            ceq = float(args[0]._capacitance)
            digits = args[0].digits
        else:
            ceq = float(args[0])
        for arg in args[1::]:
            if isinstance(arg, capacitor):
                ceq = ceq * arg._capacitance /(ceq + arg._capacitance)
                if not flag:
                    digits = arg.digits
                    flag = True
                elif arg._digits < digits:
                    digits = arg.digits
            elif capacitor.isValidCapacitor(arg):
                ceq = ceq * arg /(ceq + arg)
            else:
                raise InvalidCapacitor
        if not flag:
            digits = 3
        if kwargs:
            if kwargs['capacitor'] == True:
                return capacitor(ceq, "$C_{eq}$", digits)
        else:
            return ceq

    @staticmethod
    def parallel(*args, **kwargs):
        '''
            Computes the parallel association for a undefined number of arguments
            and returns the equivalent capacitance in a capacitor object
            The arguments can be either capacitor objects, either valid capacitance
            values.
            The output by default is a float which contains the equivalente
            capacitance value in Farads. Nevertheless, if one of the arguments is a
            dictionary with the (key, value) pair is specified as ('capacitor', True),
            a capacitor object is returned with the label $C_{eq}$ and the minimum
            number of significant digits (read SIGNIFICANT DIGITS for more details)

            SIGNIFICANT DIGITS:
            The number of significant digits of the equivalent capacitor is the
            minimum of the significant digits specified in the capacitor objects.
            If capacitance values that aren't an capacitor object are passed
            by argument, it is considered that they are ideal (having maximum
            precision), therefore don't influenciate the significant digits of
            the equivalent capacitance.
            If no capacitor object is passed by argument, the number of significant
            digits in the equivalent capacitance is the default, 3
        '''
        assert len(args) > 1, "A minimum of two capacitors is required for a parallel association"
        flag = isinstance(args[0], capacitor)
        if flag:
            ceq = float(args[0]._capacitance)
            digits = args[0]._digits
        else:
            ceq = float(args[0])
        for arg in args[1::]:
            if isinstance(arg, capacitor):
                ceq = ceq + arg._capacitance
                if not flag:
                    digits = arg._digits
                    flag = True
                elif arg._digits < digits:
                    digits = arg._digits
            elif capacitor.isValidCapacitor(arg):
                ceq = ceq + arg
            else:
                raise InvalidCapacitor
        if not flag:
            digits = 3
        if kwargs:
            if kwargs['capacitor'] == True:
                return capacitor(ceq, "$C_{eq}$", digits)
        else:
            return ceq

    @staticmethod
    def voltageDivider(V, C1, C2, frequency, angular=False, label="$V_{eq}$", **kwargs):
        '''
            Computes the voltage drop across the impedance of the capacitor C2
            in a voltage divider formed by the series association of the capacitors
            C1 and C2, such as shown below
                                    ---V----C1---+--o
                                                 |
                                                 C2
                                                 |
                                    -------GND---+--o
            "V" can either be a vSource object or a valid voltage value
            C1 and C2 can either be a capacitor object or a valid capacitance value
        '''
        assert frequency > 0, 'The frequency must be a positive value'

        if  isinstance(V, vSource):
            V = V._voltage
        elif vSource.isValidVSource(V):
            V = float(V)
        else:
            raise InvalidIndependentSource

        if  isinstance(C1, capacitor):
            ZC1 = ZC1.impedance(frequency, angular)
        elif capacitor.isValidCapacitor(C1):
            ZC1 = complex(0, -1.0/(2*pi*frequency*C1))
        else:
            raise InvalidCapacitor

        if  isinstance(C2, capacitor):
            ZC2 = C2.impedance(frequency, angular)
        elif capacitor.isValidCapacitor(C2):
            ZC2 = complex(0, -1.0/(2*pi*frequency*C2))
        else:
            raise InvalidCapacitor

        if  isinstance(V, vSource) or isinstance((C1, C2),  capacitor):
            digits = min(V._digits, R1._digits, R2._digits)
        else:
            digits = 3

        if kwargs:
            if kwargs['vSource'] == True:
                return vSource(ZC2 / (ZC1 + ZC2) * float(V), label, digits)
        return ZC2 / (ZC1 + ZC2) * float(V)

    @staticmethod
    def currentDivider(I, C1, C2, frequency, angular=False, label="$I_{eq}$", **kwargs):
        '''
            Computes the current that flows trough C2 in a current divider
            formed by the parallel association of the capacitors C1 and C2, such as
            shown below
                                ---I----+--------+--o
                                        |        |
                                        C1      C2
                                        |        |
                                        +--GND---+--o

            "I" can either be a iSource object or a valid current value
            C1 and C2 can either be a capacitor object or a valid capacitance value
        '''
        assert frequency >= 0, 'The frequency must be a positive value'

        if  isinstance(I, iSource):
            I = I._current
        elif iSource.isValidISource(I):
            I = float(I)
        else:
            raise InvalidIndependentSource

        if  isinstance(C1, capacitor):
            ZC1 = ZC1.impedance(frequency, angular)
        elif capacitor.isValidCapacitor(C1):
            ZC1 = complex(0, -1.0/(2*pi*frequency*C1))
        else:
            raise InvalidCapacitor

        if  isinstance(C2, capacitor):
            ZC2 = C2.impedance(frequency, angular)
        elif capacitor.isValidCapacitor(C2):
            ZC2 = 1.0/complex(0, -1.0/(2*pi*frequency*C2))
        else:
            raise InvalidCapacitor

        if  isinstance(I, iSource) or isinstance((C1, C2),  capacitor):
            digits = min(I._digits, C1._digits, C2._digits)
        else:
            digits = 3

        if kwargs:
            if kwargs['iSource'] == True:
                return iSource((ZC1 + ZC2) / ZC2 * float(I), label, 3)
        return (ZC1 + ZC2) / ZC2 * float(I)


class InvalidCapacitor(ValueError, TypeError):
    """
        Capacitance must be a positive values
        Float or integer are acceptable
    """
    pass

class InvalidKey(KeyError):
    '''

    '''
    pass
