'''
    ParamSchemDraw : Parametrized Schematic Draw

    A set of classes and methods to ease the of use of SchewDraw for paramerized
    circuit draw. Also provides some useful operations, such the as parallel and
    series association

    Also offers a method to format a given number to enginnering notation which
    supports unit appending and number of significant digits

    Author: Pedro Martins
    version: 0.1.2
'''

from math import floor, log10, log
from random import randint
from cmath import *

def engineerNotation(value, units="", p=3, latex=False, isComplex=False):
    '''
        Formats a complex number to engineering notation using p significant
        digits, appending the given unit after the magnitude prefix for the real
        and imaginary part

        USAGE: engineerNotation(value, units, p, kwargs)
               engineerNotation(value, units, p)
               engineerNotation(value, units, kwargs)
               engineerNotation(value, units)
               engineerNotation(value, kwargs)
               engineerNotation(value)

        ARGUMENTS:
            value   -> value to be formatted to enginnering notation
            units   -> units of the measure
            p       -> number of significant digits to use in enginnering notation
            latex   -> indicates if the string is to be embedded in a latex
                       equation (between two $)
            complex -> indicates if the output is forced to have a real and
                       imaginary part

        OUTPUT: a string with the value in enginnering notation with p significant
                digits with physical units

        CONSTRAINTS:
            value must be a Float, Integer or complex number
            units must be a string
            digits must be a integer in the interval [1, 16]
            latex and isComplex must be boolean

            other types/values outside the specified will result in
            AssertionError/Exceptions
    '''

    assert isinstance(value, (int, float, complex))
    assert isinstance(units, str)
    assert isinstance(p, int)
    assert p >= 1 and p <= 16
    assert isinstance(latex, bool)
    assert isinstance(isComplex, bool)


    '''
        If the number is supposed to be complex but the argument indicates
        otherwise, bypasses user intentions (might be some user error that is
        generating complex numbers, etc)
    '''
    if isComplex == False and value.imag != 0:
        isComplex = True
    print "Eng notation debug start"
    print isComplex
    # Format the real part and if required, the imaginary part using __engineerFormat

    print value
    print isinstance(value, complex)
    print "Eng Notation debug end"
    real = __engineerFormat(value.real, units, p, latex, isComplex)
    if isComplex == True:
        imag = __engineerFormat(value.imag, units, p, latex, isComplex)
        return "{} {}".format(real, imag)
    else:
        return real

def __engineerFormat(value, units="", p=3, latex=False, isComplex=False):
    '''
        Formats a real number to engineering notation using p significant
        digits, appending the given unit after the magnitude prefix for the real
        and imaginary part.


        ********************************NOTE************************************
            This methode is intended to be private, as it is called by
            engineerNotation. If you are looking for a way to format numbers to
            enginnering notation, please use the engineerNotation methode above
        ************************************************************************

    '''

    assert isinstance(value, (int, float))
    assert isinstance(units, str)
    assert isinstance(p, int)
    assert p >= 1 and p <= 16
    assert isinstance(latex, bool)
    assert isinstance(isComplex, bool)

    # Engineering units prefixes and offset to unitary prefix
    if latex == True:
        _PREFIX = ('p', 'n', '$\mu$', 'm', "", 'K', 'M', 'G')
    else:
        _PREFIX = ('p', 'n', '\mu{}', 'm', "", 'K', 'M', 'G')

    _UNIT_OFFSET = 4

    # Handling negative numbers and zero
    sign = ""
    if value < 0:
        sign = "-"
        value = -value
    elif value == 0:
        return '0'

    # Exponent and mantissa
    print "Eng debug start"
    print value
    print isinstance(value, complex)
    print isinstance(value, (int, float))
    print "Eng debug end"
    exp = floor(log10(value))
    mant = value / 10 ** exp

    # Round number to significant number of digits
    mantPrecise = round(mant, p-1)
    valuePrecise = mantPrecise * 10 ** exp

    # Convert number to engineer Notation
    engExp = int(exp) // 3
    mantEng = valuePrecise / (10 ** (3 * engExp))
    mantEngStr = "{:f}".format(float(mantEng))

    '''
        Text Formatting
        Count the number of zeros at the right side of the number to remove.
        If the first non-zero char is a dot, means that there is no decimal part, so remove it
        NOTE: A number in enginner notation must have at max 3 numbers after the decimal dot.
              So for example, if the precision is set to 2 (p=2) and the number is 0.230, the result must be
              230m, because the exponent must be multiple of 3. If you considered the trailing zeros has
              not part of the number, then you only have 2 significant digits, like desired
    '''
    char2rm = 0
    for k in range(len(mantEngStr)-1, 0, -1):
        if mantEngStr[k] == '0':
            char2rm = char2rm + 1
        else:
            if mantEngStr[k] == '.':
                char2rm = char2rm + 1
            break;


    # for debug
    # print "{}{}{}{}{}{}{}{}".format('Input Value: ',str(value), " | Mantissa :", str(mant), " | Mantissa Rounded: ", mantEngStr, ' ! Char:', str(char2rm))

    # Formated mantissa
    mantEngStr = mantEngStr[0:len(mantEngStr) - char2rm]

    engPrefix = engExp + _UNIT_OFFSET
    if (engPrefix < 0) or (engExp > len(_PREFIX)-1):
        # Smaller than lowest unit or higher than higher unit
        raise ValueOutsideReasonableBounds

    if isComplex == True:
        complexID = 'j'
    else:
        complexID = ''

    return "{}{}{}{}{}".format(sign, complexID, mantEngStr, _PREFIX[engPrefix], units)



class electricComponent(object):
    '''
        Generic Mother Class for eletrical components
    '''

    @staticmethod
    def elecRandom(begin, end, step=1, expArg=""):
        '''
            USAGE: elecRandom(begin, end, step, expArg)
                   relecRandom(begin, end, step)
                   relecRandom(begin, end)

            ARGUMENTS:
                begin  -> begin of the interval
                end    -> end of the interval
                step   -> minimum distance between one number and the next
                expArg -> magnitude of the random number.

            OUTPUT: random number between [begin, end] with the desired step and
                    10^expArg magnitude

            CONSTRAINTS:
                * begin must be a postive number. Float and Integer are supported
                * end must be a postive number, bigger than begin. Float and
                  Integer are supported
                * step must be a postive number, smaller than the interval
                  (begin - end). Float and Integer are supported
                * expArg must be a integer in the interval [-12, 9] or a string
                  containing the enginner magnitude identifier:
                    - p, for pico
                    - n, for nano
                    - u, for micro
                    - m, for mili
                    - '' (empty string), for unit
                    - K, for Kilo
                    - M, for Mega
                    - G, for Giga

                other types/values outside the specified will result in
                AssertionError/Exceptions
        '''
        assert begin > 0
        assert end  > 0 and end > begin
        assert step > 0 and step <= (end - begin)

        EngPrefix = {'p':-12, 'n':-9, 'u':-6, 'm':-3, "":0, 'K':3, 'M':6, 'G':9}

        if type(expArg) == str:
            try:
                exponent = 10 ** EngPrefix[expArg]
            except KeyError:
                raise KeyError('The enginner prefix accepted are p, n, u, m, K, M, G')
        elif type(expArg) == int:
            if(expArg >= -12 and expArg <= 9):
                exponent = 10 ** expArg
            else:
                raise ValueOutsideReasonableBounds
        else:
            raise TypeError

        return (randint(0, int((end - begin) / step)) * step + begin) * exponent



'''
    Exceptions that could be thrown by the classes
'''



class ValueOutsideReasonableBounds(ValueError):
    '''
        The value is not reasonable for the envised applications
    '''
    pass
