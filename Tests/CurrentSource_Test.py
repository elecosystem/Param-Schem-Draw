'''
    Test the iSource output formatting

'''
# Add module path (parent folder)
import os, sys
sys.path.insert(0,os.path.pardir)

from ParamSchemDraw import *

# Voltage Source testing examples
R0  = iSource(1)
R1  = iSource(10)
R2  = iSource(100)
R3  = iSource(1000)
R4  = iSource(10000)
R5  = iSource(100000)
R6  = iSource(1000000)
R7  = iSource(10000000)
R8  = iSource(100000000)
R9  = iSource(999)
R10 = iSource(9999)
R11 = iSource(6512)
R12 = iSource(10345)
R13 = iSource(1000000003)
R14 = iSource(10000045)
R15 = iSource(0.1)
R16 = iSource(0.01)
R17 = iSource(0.001)
R18 = iSource(0.0001)
R19 = iSource(0.00001)
R20 = iSource(0.000001)
R21 = iSource(0.000231)
R22 = iSource(0.234)
R23 = iSource(0.001234)
R24 = iSource(0.000120)
R25 = iSource(0.99999)
R26 = iSource(0.00999)
R27 = iSource(0.009)
R28 = iSource(0.999999999)
R29 = iSource(0.9200001)
R30 = iSource(0.000001)
R31 = iSource(0.192817)
R32 = iSource(0.6512)
R33 = iSource(0.06512)
R34 = iSource(0.006512)
R35 = iSource(0.0006512)
R36 = iSource(0.009999)
R37 = iSource(0.0009999)

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

