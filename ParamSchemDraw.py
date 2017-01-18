'''
    ParamSchemDraw : Parametrized Schem Draw

    This file describes a set of class and methods to ease the of use of SchewDraw for
    paramerized circuit draw

    Author: Pedro Martins

'''
# Classes to work with eletrical components
class electricComponent(object):
    def __init__(self, value, label = ""):
        self._value = value
        self._label = label

class resistor(electricComponent):
    def __init__(self, value, label= ""):
        if value > 0:
            super(resistor, self).__init__(value, label)
        else:
            raise ValueError

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
    def e24(cls):
        return resistor.__e24

    @property
    def value(self):
        if( self._value >= 1 * 10 ** 6 ):
            return str( (self._value % (1 * 10 ** 6)) * 10 ** -6 + (self._value / (1 * 10 ** 6)) ) + '$M \Omega$'
        elif( self._value >= 1 * 10 ** 3 ):
            return str( (self._value % (1 * 10 ** 3)) * 10 ** -3 + (self._value / (1 * 10 ** 3)) ) + '$K \Omega$'
        elif( self._value >= 1 ):
            return str(self._value) + '$\Omega$'
        elif( self._value >= 1 * 10 ** -3):
             return str( self._value / (1 * 10 ** -3) ) + '$m \Omega$'
        elif( self._value >= 1 * 10 ** -6):
             return str( self._value / (1 * 10 ** -6) ) + '$\mu \Omega$'
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


class vSource(electricComponent):
    def __init__(self, value, label= ""):
        if value != 0:
            super(vSource, self).__init__(value, label)
        else:
            raise ValueError

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



