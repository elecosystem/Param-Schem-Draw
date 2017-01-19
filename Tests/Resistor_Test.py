'''
    Test the resistor output formatting

'''

# Add module path (parent folder)
import os, sys
sys.path.insert(0,os.path.pardir)

from ParamSchemDraw import *

# Resistor testing examples
R0  = resistor(1)
R1  = resistor(10)
R2  = resistor(100)
R3  = resistor(1000)
R4  = resistor(10000)
R5  = resistor(100000)
R6  = resistor(1000000)
R7  = resistor(10000000)
R8  = resistor(100000000)
R9  = resistor(999)
R10 = resistor(9999)
R11 = resistor(6512)
R12 = resistor(10345)
R13 = resistor(1000000003)
R14 = resistor(10000045)
R15 = resistor(0.1)
R16 = resistor(0.01)
R17 = resistor(0.001)
R18 = resistor(0.0001)
R19 = resistor(0.00001)
R20 = resistor(0.000001)
R21 = resistor(0.000231)
R22 = resistor(0.234)
R23 = resistor(0.001234)
R24 = resistor(0.000120)
R25 = resistor(0.99999)
R26 = resistor(0.00999)
R27 = resistor(0.009)
R28 = resistor(0.999999999)
R29 = resistor(0.9200001)
R30 = resistor(0.000001)
R31 = resistor(0.192817)
R32 = resistor(0.6512)
R33 = resistor(0.06512)
R34 = resistor(0.006512)
R35 = resistor(0.0006512)
R36 = resistor(0.009999)
R37 = resistor(0.0009999)

# The printing must be formatted with Engeneering Notation and latex symbols
print R0.value
print R1.value
print R2.value
print R3.value
print R4.value
print R5.value
print R6.value
print R7.value
print R8.value
print R9.value
print R10.value
print R11.value
print R12.value
print R13.value
print R14.value
print R15.value
print R16.value
print R17.value
print R18.value
print R19.value
print R20.value
print R21.value
print R22.value
print R23.value
print R24.value
print R25.value
print R26.value
print R27.value
print R28.value
print R29.value
print R30.value
print R31.value
print R32.value
print R33.value
print R34.value
print R35.value
print R36.value
print R37.value

