'''
    ParamSchemDraw : Parametrized Schematic Draw

    This file describes a set of class and methods to ease the of use of SchewDraw for
    paramerized circuit draw

    Author: Pedro Martins

'''

from numbers import Number, Complex
from decimal import Decimal
from math import floor, log10, pow

def frexp10(x):
    """
    Return mantissa and exponent (base 10), similar to base-2 frexp()
    :param x: floating point number
    :return: tuple (mantissa, exponent)
    """
    exp = floor(log10(x))
    return x/10**exp, exp


def eng_notate(x, d=3, suff=True, neg_ok=False):
    # Practical component suffixes
    _SUFFIX = ["p", "n", "u", "m", "", "k", "M", "G"]
    # Offset to unit multiplier (no suffix)

    _UNIT_OFFSET = 4

    sign = ""
    if neg_ok and x < 0.0:
        sign = "-"
        x = -x
    #if x < 0.0 or not isfinite(x):
    #    return "RangeErr"
    if x == 0:
        return "0.0"
    # Normalize the number and round to get d significant digits
    mant, exp = frexp10(x)
    r = round(mant,d-1)
    # Convert back to original scale
    x = r * pow(10.0, exp)
    # Get integer exponent to group by factors of 1000
    p = int(floor(log10(x)))
    p3 = p // 3
    # Get root value string
    value = x / pow(10.0, 3*p3)
    numStr = "{:f}".format(value)
    # Slice to length, avoid trailing "."
    if numStr[d] != ".":
        numStr = numStr[0:d+1]
    else:
        numStr = numStr[0:d]
    # Prepend '-' if necessary
    numStr = sign + numStr
    if suff:
        # Append units suffix
        p3i = p3 + _UNIT_OFFSET
        if p3i < 0:
            # Smaller than lowest unit
            return "<1{}".format(_SUFFIX[0])
        if p3i > len(_SUFFIX)-1:
            # Larger than largest unit
            return ">999{}".format(_SUFFIX[-1])
        else:
            s = _SUFFIX[p3i]
            return "{}{}".format(numStr, s)
    else:
        # No suffix, return floating point string
        if p3 != 0:
            return "{}e{:d}".format(numStr, 3*p3)
        else:
            return "{}".format(numStr)


def round2Precision(x, p):
    n = floor(log10(x)) + 1 - p
    print n
    return round(10 ** (-n) * x) * 10 ** n

# Classes to work with eletrical components
class electricComponent(object):
    @staticmethod
    def enginnerNotation(value, units="", p=3):
        '''
            Formats a number to engineering notation with p significant digits
        '''
        assert value != 0
        # Practical component suffixes
        _SUFFIX = ["p", "n", "u", "m", "", "k", "M", "G"]
        # Offset to unit multiplier (no suffix)

        _UNIT_OFFSET = 4

        # For negative cases
        sign = ""
        if value < 0:
            sign = "-"
            value = -value

        # Exponent and mantissa
        exp = floor(log10(value))
        mant = value / 10 ** exp

        # Get significant digits
        trunc = round(mant, p-1)
        truncPrec = trunc * 10 ** exp

        engExp = int(exp) // 3
        engValue = truncPrec / (10 ** (3 * engExp))
        engStr = "{:f}".format(engValue)

        # Slice to length, avoid trailing "."
        if engStr[p] != ".":
            engStr = engStr[0:p+1]
        else:
            engStr = engStr[0:p]
        # Prepend '-' if necessary
        engStr = sign + engStr

        engPrefix = engExp + _UNIT_OFFSET
        #if engPrefix < 0:
        #    # Smaller than lowest unit
        #    return "<1{}".format(_SUFFIX[0])
        #if p3i > len(_SUFFIX)-1:
            # Larger than largest unit
        #    return ">999{}".format(_SUFFIX[-1])
        #else:
        s = _SUFFIX[engPrefix]
        return "{}{}{}".format(engStr, s, units)


    '''
            return eng_notate(value) + units



            value = round2Precision(value, 3)
            if( value >= 1 * 10 ** 6 ):
                return str( (value % (1 * 10 ** 6)) * 10 ** -6 + (value / (1 * 10 ** 6)) ) + '$M$'  + units
            elif( value >= 1 * 10 ** 3 ):
                return str( (value % (1 * 10 ** 3)) * 10 ** -3 + (value / (1 * 10 ** 3)) ) + '$K$' + units
            elif( value >= 1 ):
                return str(value) + units
            elif( value >= 1 * 10 ** -3):
                 return str( value / (1 * 10 ** -3) ) + '$m$' + units
            elif( value >= 1 * 10 ** -6):
                 return str( value / (1 * 10 ** -6) ) + '$\mu$' + units
            else:
                raise ValueOutsideReasonableBounds
    '''


class resistor(electricComponent):
    def __init__(self, value, label= ""):
        if resistor.isValidResistor(value):
            self._value = value
            self._label = label
        else:
            raise NonPositiveResistance

    @staticmethod
    def isValidResistor(R):
        assert R != None
        if isinstance(R, (Number, Decimal)) and ~isinstance(R, Complex):
            if R > 0:
                return True
        return False

    @property
    def value(self):
        return eng_notate(self._value)
        #return electricComponent.enginnerNotation(self._value, '$\Omega$')

    @property
    def label(self):
        return self._label

    @property
    def schem(self):
        return self._schem

    @schem.setter
    def schem(self, schematic):
        self._schem = schematic

    # E24 class resistor values
    __e24 =( 1.0 , 10 ,	100 , 1.0 * 10 ** 3 , 10 * 10 ** 3 , 100 * 10 ** 3 , 1.0 * 10 ** 6,
             1.1 , 11 ,	110 , 1.1 * 10 ** 3 , 11 * 10 ** 3 , 110 * 10 ** 3 , 1.1 * 10 ** 6,
             1.2 , 12 ,	120 , 1.2 * 10 ** 3 , 12 * 10 ** 3 , 120 * 10 ** 3 , 1.2 * 10 ** 6,
             1.3 , 13 ,	130 , 1.3 * 10 ** 3 , 13 * 10 ** 3 , 130 * 10 ** 3 , 1.3 * 10 ** 6,
             1.5 , 15 ,	150 , 1.5 * 10 ** 3 , 15 * 10 ** 3 , 150 * 10 ** 3 , 1.5 * 10 ** 6,
             1.6 , 16 ,	160 , 1.6 * 10 ** 3 , 16 * 10 ** 3 , 160 * 10 ** 3 , 1.6 * 10 ** 6,
             1.8 , 18 ,	180 , 1.8 * 10 ** 3 , 18 * 10 ** 3 , 180 * 10 ** 3 , 1.8 * 10 ** 6,
             2.0 , 20 ,	200 , 2.0 * 10 ** 3 , 20 * 10 ** 3 , 200 * 10 ** 3 , 2.0 * 10 ** 6,
             2.2 , 22 ,	220 , 2.2 * 10 ** 3 , 22 * 10 ** 3 , 220 * 10 ** 3 , 2.2 * 10 ** 6,
             2.4 , 24 ,	240 , 2.4 * 10 ** 3 , 24 * 10 ** 3 , 240 * 10 ** 3 , 2.4 * 10 ** 6,
             2.7 , 27 ,	270 , 2.7 * 10 ** 3 , 27 * 10 ** 3 , 270 * 10 ** 3 , 2.7 * 10 ** 6,
             3.0 , 30 ,	300 , 3.0 * 10 ** 3 , 30 * 10 ** 3 , 300 * 10 ** 3 , 3.0 * 10 ** 6,
             3.3 , 33 ,	330 , 3.3 * 10 ** 3 , 33 * 10 ** 3 , 330 * 10 ** 3 , 3.3 * 10 ** 6,
             3.6 , 36 ,	360 , 3.6 * 10 ** 3 , 36 * 10 ** 3 , 360 * 10 ** 3 , 3.6 * 10 ** 6,
             3.9 , 39 ,	390 , 3.9 * 10 ** 3 , 39 * 10 ** 3 , 390 * 10 ** 3 , 3.9 * 10 ** 6,
             4.3 , 43 ,	430 , 4.3 * 10 ** 3 , 43 * 10 ** 3 , 430 * 10 ** 3 , 4.3 * 10 ** 6,
             4.7 , 47 ,	470 , 4.7 * 10 ** 3 , 47 * 10 ** 3 , 470 * 10 ** 3 , 4.7 * 10 ** 6,
             5.1 , 51 ,	510 , 5.1 * 10 ** 3 , 51 * 10 ** 3 , 510 * 10 ** 3 , 5.1 * 10 ** 6,
             5.6 , 56 , 560 , 5.6 * 10 ** 3 , 56 * 10 ** 3 , 560 * 10 ** 3 , 5.6 * 10 ** 6,
             6.2 , 62 ,	620 , 6.2 * 10 ** 3 , 62 * 10 ** 3 , 620 * 10 ** 3 , 6.2 * 10 ** 6,
             6.8 , 68 ,	680 , 6.8 * 10 ** 3 , 68 * 10 ** 3 , 680 * 10 ** 3 , 6.8 * 10 ** 6,
             7.5 , 75 ,	750 , 7.5 * 10 ** 3 , 75 * 10 ** 3 , 750 * 10 ** 3 , 7.5 * 10 ** 6,
             8.2 , 82 ,	820 , 8.2 * 10 ** 3 , 82 * 10 ** 3 , 820 * 10 ** 3 , 8.2 * 10 ** 6,
             9.1 , 91 ,	910 , 9.1 * 10 ** 3 , 91 * 10 ** 3 , 910 * 10 ** 3 , 9.1 * 10 ** 6)

    @staticmethod
    def e24():
        return resistor.__e24

    @staticmethod
    def series(*args):
        assert len(args) > 1, "The number of is incorrect. A series association must at least have 2"
        if isinstance(args[0], resistor):
            req = float(args[0]._value)
        else:
            req = float(args[0])
        for arg in args[1::]:
            if isinstance(arg, resistor):
                req = req + arg._value
            else:
                req = req + arg
        return resistor.enginnerNotation(req)

    @staticmethod
    def parallel(*args):
        assert len(args) > 1, "The number of is incorrect. A parallel association must at least have 2"
        if isinstance(args[0], resistor):
            req = float(args[0]._value)
        else:
            req = float(args[0])
        for arg in args[1::]:
            if isinstance(arg, resistor):
                req = req * arg._value /(req + arg._value)
            else:
                req = req * arg /(req + arg)
        return resistor.enginnerNotation(req)

    @staticmethod
    def currentDivider(I, R1, R2):
        '''
            ---I----+--------+--o
                    |        |
                    R1      R2
                    |        |
                    +--GND---+--o

        where the output is the current in the resistor R2
        '''
        if ~isinstance(I, iSource):
            assert iSource.isValidISource(I)
        else:
            I = I.value
        if ~isinstance(R1, resistor):
            assert resistor.isValidResistor(R1)
        else:
            R1 = R1.value
        if ~isinstance(R1, resistor):
            assert resistor.isValidResistor(R2)
        else:
            R2 = R2.values

        return (R1 + R2) / R2 * I

    @staticmethod
    def voltageDivider(V, R1, R2):
        '''
            ---V----R1---+--o
                         |
                         R2
                         |
            -------GND---+--o

        where the output is the voltage drop across the resistor R2
        '''
        if ~isinstance(V, vSource):
            assert vSource.isValidVSource(V)
        else:
            V = V.value
        if ~isinstance(R1, resistor):
            assert resistor.isValidResistor(R1)
        else:
            R1 = R1.value
        if ~isinstance(R1, resistor):
            assert resistor.isValidResistor(R2)
        else:
            R2 = R2.values

        return R2 / (R1 + R2) * V


'''
    def series(self, *args):
        assert len(args) > 0, "The number of is incorrect."
        req = float(self._value)
        for arg in args[1::]:
            if ~isinstance(arg, resistor):
                raise TypeError
            req = req + arg._value
        return resistor.enginnerNotation(req)

    def parallel(self, *args):
        assert len(args) > 0, "The number of is incorrect."
        req = float(self._value)
        for arg in args[1::]:
            if ~isinstance(arg, resistor):
                raise TypeError
            req = req + arg._value
        return resistor.enginnerNotation(req)
'''

class vSource(electricComponent):
    def __init__(self, value, label= ""):
        if vSource.isValidVSource(value):
            self._value = value
            self._label = label
        else:
            raise InvalidIndepentSource

    @staticmethod
    def isValidVSource(V):
        assert V != None
        if isinstance(V, (Number, Decimal)):
            if V != 0:
                return True
        return False

    @property
    def value(self):
        if( self._value >= 1 * 10 ** 6 ):
            return str( (self._value % (1 * 10 ** 6)) * 10 ** -6 + (self._value / (1 * 10 ** 6)) ) + '$M V$'
        elif( self._value >= 1 * 10 ** 3 ):
            return str( (self._value % (1 * 10 ** 3)) * 10 ** -3 + (self._value / (1 * 10 ** 3)) ) + '$K V$'
        elif( self._value >= 1 ):
            return str(self._value) + '$V$'
        elif( self._value >= 1 * 10 ** -3):
             return str( self._value / (1 * 10 ** -3) ) + '$m V$'
        elif( self._value >= 1 * 10 ** -6):
             return str( self._value / (1 * 10 ** -6) ) + '$\mu V$'
        else:
            raise ValueError

    @property
    def label(self):
        return self._label

    @property
    def schem(self):
        return self._schem

    @schem.setter
    def schem(self, schematic):
        self._schem = schematic


class iSource(electricComponent):
    def __init__(self, value, label= ""):
        if iSource.isValidISource(value):
            self._value = value
            self._label = label
        else:
            raise InvalidIndepentSource

    @staticmethod
    def isValidISource(I):
        assert I != None
        if isinstance(I, (Number, Decimal)):
            if I != 0:
                return True
        return False

    @property
    def value(self):
        if( self._value >= 1 * 10 ** 6 ):
            return str( (self._value % (1 * 10 ** 6)) * 10 ** -6 + (self._value / (1 * 10 ** 6)) ) + '$M A$'
        elif( self._value >= 1 * 10 ** 3 ):
            return str( (self._value % (1 * 10 ** 3)) * 10 ** -3 + (self._value / (1 * 10 ** 3)) ) + '$K A$'
        elif( self._value >= 1 ):
            return str(self._value) + '$A$'
        elif( self._value >= 1 * 10 ** -3):
             return str( self._value / (1 * 10 ** -3) ) + '$m A$'
        elif( self._value >= 1 * 10 ** -6):
             return str( self._value / (1 * 10 ** -6) ) + '$\mu A$'
        else:
            raise ValueError

    @property
    def label(self):
        return self._label

    @property
    def schem(self):
        return self._schem

    @schem.setter
    def schem(self, schematic):
        self._schem = schematic


# Exceptions throw by class
class NonPositiveResistance(ValueError):
    """ Resistance is not a positive value """
    pass

class ValueOutsideReasonableBounds(ValueError):
    """ The value is not reasonable """
    pass

class InvalidIndepentSource(ValueError):
    """ The independent voltage/current source value can't be zero """
    pass
