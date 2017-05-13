'''
       ____  _    _         _____  _____  _____ _____   ____  _      ______  _____
      / __ \| |  | |  /\   |  __ \|  __ \|_   _|  __ \ / __ \| |    |  ____|/ ____|
     | |  | | |  | | /  \  | |  | | |__) | | | | |__) | |  | | |    | |__  | (___
     | |  | | |  | |/ /\ \ | |  | |  _  /  | | |  ___/| |  | | |    |  __|  \___ \
     | |__| | |__| / ____ \| |__| | | \ \ _| |_| |    | |__| | |____| |____ ____) |
      \___\_\\____/_/    \_\_____/|_|  \_\_____|_|     \____/|______|______|_____/


    quadripoles: Two Port Network (Quadripole) module for ParamSchemDraw

    A set of classes and methods to ease the drawing and manipulation of two
    port networks.

    Supports impedance, admittance, hibrid, inverse hibrid, transmission and
    scattering parameters quadripoles

    Author: Pedro Martins
    version: 0.1.3

    Matriz representation shall be like
    \begin{bmatrix}
       0 & 0
       0 & 0
     \end{bmatrix}
'''



'''
    import matplotlib and make it run headless, otherwise in SchewDraw it will
    return an error when tries to connect to Xserver and $Display environmental
    variable matplotlib.pyplot enables controlling the number of active plots
'''

import matplotlib
matplotlib.use('Agg')

# Documentation:  https://bitbucket.org/cdelker/schemdraw
import SchemDraw as schem
import SchemDraw.elements as e

# Import library to parametrize the used of SchemDraw
from ParamSchemDraw import electricComponent, engineerNotation

# Folder to save the schematics in server
path = '/projects/15860edd-0fa5-4a0a-820c-2bb86b4c0cd5/ENUNCIADOS/IMAGENS/'

# Image extension
extension = '.png'




from numpy import linalg, matrix, array
import vSource
import iSource
import resistor

class quadripole(object):
    '''
        Class used to define a generic quadripoles
        It provides static methods to compute xxxx. It also offers a
        method to xxx
        It can also format the quadripole values to enginnering notation
    '''

    def __init__(self, a11, a12, a21, a22, label="", digits=3):
        assert isinstance(a11, (int, float, complex))
        assert isinstance(a12, (int, float, complex))
        assert isinstance(a21, (int, float, complex))
        assert isinstance(a22, (int, float, complex))

    @property
    def label(self):
        return self._label

    @property
    def digits(self):
        return self._digits

    @property
    def schem(self):
        return self._schem

    @label.setter
    def label(self, label):
        assert isinstance(label, str), "The label of the quadripole must be a string"
        self._label =  label

    @schem.setter
    def schem(self, schematic):
        self._schem = schematic



'''
      _____  __  __  _____   ______  _____            _   _   _____  ______
     |_   _||  \/  ||  __ \ |  ____||  __ \    /\    | \ | | / ____||  ____|
       | |  | \  / || |__) || |__   | |  | |  /  \   |  \| || |     | |__
       | |  | |\/| ||  ___/ |  __|  | |  | | / /\ \  | . ` || |     |  __|
      _| |_ | |  | || |     | |____ | |__| |/ ____ \ | |\  || |____ | |____
     |_____||_|  |_||_|     |______||_____//_/    \_\|_| \_| \_____||______|

      _____          _____             __  __  ______  _______  ______  _____    _____
     |  __ \  /\    |  __ \     /\    |  \/  ||  ____||__   __||  ____||  __ \  / ____|
     | |__) |/  \   | |__) |   /  \   | \  / || |__      | |   | |__   | |__) || (___
     |  ___// /\ \  |  _  /   / /\ \  | |\/| ||  __|     | |   |  __|  |  _  /  \___ \
     | |   / ____ \ | | \ \  / ____ \ | |  | || |____    | |   | |____ | | \ \  ____) |
     |_|  /_/    \_\|_|  \_\/_/    \_\|_|  |_||______|   |_|   |______||_|  \_\|_____/

'''

class zQuadripole(quadripole):
    '''
        Class used to define an impedance parameters quadripole

    '''
    def __init__(self, z11, z12, z21, z22, label="", digits=3):
        '''
            USAGE: zQuadripole(z11, z12, z21, z22, label, digits)
                   zQuadripole(z11, z12, z21, z22, label)
                   zQuadripole(z11, z12, z21, z22)

            ARGUMENTS:
                z11    -> V1/I1 when the port 2 is an open circuit (I2 = 0)
                z12    -> V1/I2 when the port 1 is an open circuit (I1 = 0)
                z21    -> V2/I1 when the port 2 is an open circuit (I2 = 0)
                z22    -> V2/I2 when the port 1 is an open circuit (I1 = 0)
                label  -> name/identifier of the quadripole (optional)
                digits -> number of significant digits to use in engineering notation (optional)

            OUTPUT: an impedance quadripole object

            CONSTRAINTS:
                z11, z12, z21, z22 must be a number. Float, Integer and complex
                are supported
                label must be a string
                digits must be a integer in the interval [1, 16]

                other types/values outside the specified will result in
                AssertionError/Exceptions
        '''

        assert isinstance(z11, (int, float, complex))
        assert isinstance(z12, (int, float, complex))
        assert isinstance(z21, (int, float, complex))
        assert isinstance(z22, (int, float, complex))
        assert isinstance(label, str), "The label element must be a string"
        assert isinstance(digits, int), "The digits element must be an integer"
        assert digits >= 1 and digits <= 16, "The digits element must be between [1, 16]"

        self._z11 = z11
        self._z12 = z12
        self._z21 = z21
        self._z22 = z22
        self._z = matrix(array([[z11, z12], [z21, z22]]).reshape(2, 2))

        self._label = label
        self._digits = digits

    @classmethod
    def viInit(cls, V1, V2, I1, I2, label="", digits=3):
        '''
            Another init methode, where the arguments are the voltages and corrents
            at the terminals of the quadripole, in open circuit

            USAGE: viInit(V1, V2, I1, I2, label, digits)
                   viInit(V1, V2, I1, I2, label)
                   viInit(V1, V2, I1, I2)

            ARGUMENTS:
                V1     -> voltage drop between the terminals of the port 1
                V2     -> voltage drop between the terminals of the port 2
                I1     -> current entering the port 1
                I2     -> current entering the port 2
                label  -> name/identifier of the quadripole (optional)
                digits -> number of significant digits to use in engineering notation (optional)

            OUTPUT: an impedance quadripole object

            CONSTRAINTS:
                V1, V2, I1, I2 must be a number. Float, Integer and complex
                are supported
                label must be a string
                digits must be a integer in the interval [1, 16]

                other types/values outside the specified will result in
                AssertionError/Exceptions
        '''

        assert isinstance(V1, (int, float, complex))
        assert isinstance(V2, (int, float, complex))
        assert isinstance(I1, (int, float, complex))
        assert isinstance(I2, (int, float, complex))
        assert isinstance(label, str), "The label element must be a string"
        assert isinstance(digits, int), "The digits element must be an integer"
        assert digits >= 1 and digits <= 16, "The digits element must be between [1, 16]"

        z11 = V1 / I1
        z12 = V1 / I2
        z21 = V2 / I1
        z22 = V2 / I2
        return cls(z11, z12, z21, z22, label, digits)

    @classmethod
    def zInit(cls, Z, label="", digits=3):
        '''
            Another init methode, where the argument is impedance matrix

            USAGE: zInit(Z, label, digits)
                   zInit(Z, label)
                   zInit(Z)

            ARGUMENTS:
                Z      -> impedance matrix [2x2], as a numpy matrix object
                label  -> name/identifier of the quadripole (optional)
                digits -> number of significant digits to use in engineering notation (optional)

            OUTPUT: an impedance quadripole object

            CONSTRAINTS:
                Z must be a numpy matrix with 2x2. Float, Integer and complex
                values are supported
                label must be a string
                digits must be a integer in the interval [1, 16]

                other types/values outside the specified will result in
                AssertionError/Exceptions
        '''
        assert isinstance(Z, matrix), "The impedance matrix must be a numpy matrix"
        assert Z.shape == (2, 2), "The matrix dimensions is incorrect. Must be a 2x2 matrix"
        assert Z.dtype == (int, float, complex)
        assert isinstance(label, str), "The label element must be a string"
        assert isinstance(digits, int), "The digits element must be an integer"
        assert digits >= 1 and digits <= 16, "The digits element must be between [1, 16]"

        return cls(Z[0, 0], Z[0, 1], Z[1, 0], Z[1, 1], label, digits)
        assert isinstance(V1, (int, float, complex))


    __UNIT = '$\Omega$'

    @property
    def z11(self):
        return self._z11

    @property
    def z12(self):
        return self._z12

    @property
    def z21(self):
        return self._z21

    @property
    def z22(self):
        return self._z22

    @property
    def z(self):
        return self._z

    @property
    def isReciprocal(self):
        '''
            Checks if the quadripole object represents reciprocal quadripole
            A quadripole is a reciprocal quadripole if the change of a voltage
            source from port 1 to port 2 and a amperimeter from port 2 to port 1,
            or vice-versa, produces the same reading in the amperimeter

            In this quadripole, only 3 measures are necessary to determine all
            the 4 parameters
        '''
        return self.z_12 == self._z21

    @property
    def isSimetrical(self):
        '''
            Checks if the quadripole object represents simetric quadripole
            A quadripole is a simetrical quadripole if its ports can be changed
            without without alterating the voltages and currents at its terminals
            A simetrical two port network is also reciprocal

            In this quadripole, only 2 measures are necessary to determine all
            the 4 parameters
        '''
        return isReciprocal(self) and self.z_11 == self._z22

    @property
    def zin(self):
        '''
            Input impedance of the quadripole
        '''
        return self._z11

    @property
    def zout(self):
        '''
            Output impedance of the quadripole
        '''
        return self._z22

    @property
    def yin(self):
        '''
            Input admittance of the quadripole
        '''
        return 1.0/self._z11

    @property
    def yout(self):
        '''
            Output admittance of the quadripole
        '''
        return 1.0/self._z22

    @property
    def vGain(self):
        '''
            Voltage gain of the quadripole, Av = V2/V1
        '''
        return (1.0*self._z21)/self._z11

    @property
    def iGain(self):
        '''
            Current gain of the quadripole, Ai = I2/I1
        '''
        return (1.0*self._z21)/self._z22

    @property
    def pGain(self):
        '''
            Power gain of the quadripole, Ap = P2/P1
        '''
        return vGain(self) * iGain(self)

    @property
    def transImpedanceGain(self):
        '''
            Transimpedance gain of the quadripole, A_TI = V2/I1
        '''
        return self._z21

    @property
    def transAdmittanceGain(self):
        '''
            Transadmittance gain of the quadripole, A_TA = I2/V1
        '''
        return 1.0/self._z12


    @z11.setter
    def z11(self, z11):
        assert isinstance(z11, (int, float, complex))
        self._z11 =  z11
        self._z[0,0] = z11

    @z12.setter
    def z12(self, z12):
        assert isinstance(z12, (int, float, complex))
        self._z12 =  z12
        self._z[0,1] = z12

    @z21.setter
    def z21(self, z21):
        assert isinstance(z21, (int, float, complex))
        self._z21 =  z21
        self._z[1,0] = z21

    @z22.setter
    def z22(self, z22):
        assert isinstance(z22, (int, float, complex))
        self._z22 =  z22
        self._z[1,1] = z22

    @property
    def toY(self):
        '''
            Convert the impedance quadripole to an admittance parameters quadripole
        '''
        y = self._z.I
        return yQuadripole.Yinit(y[0, 0], y[0, 1], y[1, 0], y[1, 1])

    @property
    def toH(self):
        '''
            Convert the impedance quadripole to an hibrid parameters quadripole
        '''
        deltaZ = linalg.det(self._z)
        H =  matrix(array([[self._z22, -self._z12], [-self._z21, self._z11]]).reshape(2, 2)) / deltaZ
        return hQuadripole.hInit(self, H)

    @property
    def toG(self):
        '''
            Convert the impedance quadripole to an inverse hibrid parameters quadripole
        '''
        H = toH(self).h
        return gQuadripole.gInit(self, H.I)

    @property
    def toT(self):
        '''
            Convert the impedance quadripole to a transmission parameters quadripole
        '''
        deltaZ = linalg.det(self._z)
        T = matrix(array([[self._z11, deltaZ], [1.0, self._z22]]).reshape(2, 2)) / self._z12
        return tQuadripole.tInit(self, T)

    @property
    def toS(self):
        '''
            Convert the impedance quadripole to an scattering parameters quadripole
        '''
        T = toT(self).t
        return sQuadripole.sInit(self, T.I)

    def outputTh(self, Vth, Rth, outPort=2):
        '''
            Calculate the voltage and current at one port of the quadripole when
            the other is connected to a Thevenin Equivalent with




        '''

        assert vSource.isValidVSource(Vth)
        assert resistor.isValidResistor(Rth)
        assert isinstance(outPort, int)
        assert outPort == 1 or outPort == 2

        raise NotImplementedError

    def zinLoad(self, RL, inPort=1):
        '''
            Input impedance by having a load resistor in the other port
        '''

        assert resistor.isValidResistor(RL) or isinstance(resistor)
        assert isinstance(inPort, int)
        assert inPort == 1 or inPort == 2

        RL_resistance = RL.resistance if isinstance(RL, resistor) else RL

        if inPort == 1:
            return self._z11 + self._z12*float(self._z_21) / (RL_resistance - self._z22)
        elif inPort == 2    :
            return -self._z21 * float(self._z12) / (self._z11 + RL_resistance) + self._z22
        else:
            raise RuntimeError('inPort must be a integer with 1 or 2! Assertion verification failed!')


'''
            _____   __  __  _____  _______  _______         _   _   _____  ______
     /\    |  __ \ |  \/  ||_   _||__   __||__   __| /\    | \ | | / ____||  ____|
    /  \   | |  | || \  / |  | |     | |      | |   /  \   |  \| || |     | |__
   / /\ \  | |  | || |\/| |  | |     | |      | |  / /\ \  | . ` || |     |  __|
  / ____ \ | |__| || |  | | _| |_    | |      | | / ____ \ | |\  || |____ | |____
 /_/    \_\|_____/ |_|  |_||_____|   |_|      |_|/_/    \_\|_| \_| \_____||______|


  _____          _____             __  __  ______  _______  ______  _____    _____
 |  __ \  /\    |  __ \     /\    |  \/  ||  ____||__   __||  ____||  __ \  / ____|
 | |__) |/  \   | |__) |   /  \   | \  / || |__      | |   | |__   | |__) || (___
 |  ___// /\ \  |  _  /   / /\ \  | |\/| ||  __|     | |   |  __|  |  _  /  \___ \
 | |   / ____ \ | | \ \  / ____ \ | |  | || |____    | |   | |____ | | \ \  ____) |
 |_|  /_/    \_\|_|  \_\/_/    \_\|_|  |_||______|   |_|   |______||_|  \_\|_____/

'''

def yQuadripole(y11, y12, y21, y22):
    assert isinstance(y11, (int, float))
    assert isinstance(y12, (int, float))
    assert isinstance(y21, (int, float))
    assert isinstance(y22, (int, float))


'''
      _    _  _____  ____   _____   _____  _____
     | |  | ||_   _||  _ \ |  __ \ |_   _||  __ \
     | |__| |  | |  | |_) || |__) |  | |  | |  | |
     |  __  |  | |  |  _ < |  _  /   | |  | |  | |
     | |  | | _| |_ | |_) || | \ \  _| |_ | |__| |
     |_|  |_||_____||____/ |_|  \_\|_____||_____/


      _____          _____             __  __  ______  _______  ______  _____    _____
     |  __ \  /\    |  __ \     /\    |  \/  ||  ____||__   __||  ____||  __ \  / ____|
     | |__) |/  \   | |__) |   /  \   | \  / || |__      | |   | |__   | |__) || (___
     |  ___// /\ \  |  _  /   / /\ \  | |\/| ||  __|     | |   |  __|  |  _  /  \___ \
     | |   / ____ \ | | \ \  / ____ \ | |  | || |____    | |   | |____ | | \ \  ____) |
     |_|  /_/    \_\|_|  \_\/_/    \_\|_|  |_||______|   |_|   |______||_|  \_\|_____/

'''

def hQuadripole(h11, h12, h21, h22):
    assert isinstance(h11, (int, float))
    assert isinstance(h12, (int, float))
    assert isinstance(h21, (int, float))
    assert isinstance(h22, (int, float))


'''
  _____  _   _ __      __ ______  _____    _____  ______
 |_   _|| \ | |\ \    / /|  ____||  __ \  / ____||  ____|
   | |  |  \| | \ \  / / | |__   | |__) || (___  | |__
   | |  | . ` |  \ \/ /  |  __|  |  _  /  \___ \ |  __|
  _| |_ | |\  |   \  /   | |____ | | \ \  ____) || |____
 |_____||_| \_|    \/    |______||_|  \_\|_____/ |______|


  _    _  _____  ____   _____   _____  _____
 | |  | ||_   _||  _ \ |  __ \ |_   _||  __ \
 | |__| |  | |  | |_) || |__) |  | |  | |  | |
 |  __  |  | |  |  _ < |  _  /   | |  | |  | |
 | |  | | _| |_ | |_) || | \ \  _| |_ | |__| |
 |_|  |_||_____||____/ |_|  \_\|_____||_____/


  _____          _____             __  __  ______  _______  ______  _____    _____
 |  __ \  /\    |  __ \     /\    |  \/  ||  ____||__   __||  ____||  __ \  / ____|
 | |__) |/  \   | |__) |   /  \   | \  / || |__      | |   | |__   | |__) || (___
 |  ___// /\ \  |  _  /   / /\ \  | |\/| ||  __|     | |   |  __|  |  _  /  \___ \
 | |   / ____ \ | | \ \  / ____ \ | |  | || |____    | |   | |____ | | \ \  ____) |
 |_|  /_/    \_\|_|  \_\/_/    \_\|_|  |_||______|   |_|   |______||_|  \_\|_____/

'''

def gQuadripole(g11, g12, g21, g22):
    assert isinstance(h11, (int, float))
    assert isinstance(h12, (int, float))
    assert isinstance(h21, (int, float))
    assert isinstance(h22, (int, float))



# Transmission Parameters
def tQuadripole(g11, g12, g21, g22):
    assert isinstance(h11, (int, float))
    assert isinstance(h12, (int, float))
    assert isinstance(h21, (int, float))
    assert isinstance(h22, (int, float))

# Scattering Parameters
def sQuadripole(g11, g12, g21, g22):
    assert isinstance(h11, (int, float))
    assert isinstance(h12, (int, float))
    assert isinstance(h21, (int, float))
    assert isinstance(h22, (int, float))
