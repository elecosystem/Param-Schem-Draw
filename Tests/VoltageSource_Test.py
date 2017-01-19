'''
    Test the vSource output formatting

'''
# Add module path (parent folder)
import os, sys
sys.path.insert(0,os.path.pardir)

from ParamSchemDraw import *

# Voltage Source testing examples
R0  = vSource(1)
R1  = vSource(10)
R2  = vSource(100)
R3  = vSource(1000)
R4  = vSource(10000)
R5  = vSource(100000)
R6  = vSource(1000000)
R7  = vSource(10000000)
R8  = vSource(100000000)
R9  = vSource(999)
R10 = vSource(9999)
R11 = vSource(6512)
R12 = vSource(10345)
R13 = vSource(1000000003)
R14 = vSource(10000045)
R15 = vSource(0.1)
R16 = vSource(0.01)
R17 = vSource(0.001)
R18 = vSource(0.0001)
R19 = vSource(0.00001)
R20 = vSource(0.000001)
R21 = vSource(0.000231)
R22 = vSource(0.234)
R23 = vSource(0.001234)
R24 = vSource(0.000120)
R25 = vSource(0.99999)
R26 = vSource(0.00999)
R27 = vSource(0.009)
R28 = vSource(0.999999999)
R29 = vSource(0.9200001)
R30 = vSource(0.000001)
R31 = vSource(0.192817)
R32 = vSource(0.6512)
R33 = vSource(0.06512)
R34 = vSource(0.006512)
R35 = vSource(0.0006512)
R36 = vSource(0.009999)
R37 = vSource(0.0009999)

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

