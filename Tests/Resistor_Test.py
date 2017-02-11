'''
    Test the resistor output formatting

'''

# Add module path (parent folder)
import os, sys
sys.path.insert(0,os.path.pardir)

from ParamSchemDraw import *

# Test assertions for invalid argument values
try:
    resistor(0)
except InvalidResistor:
    print "Assertion caught for InvalidResistor. Resistor value can't be zero"

try:
    resistor(-34)
except InvalidResistor:
    print "Assertion caught for InvalidResistor. Resistor value can't be negative"

try:
    resistor(-2323213.232, "", 3)
except InvalidResistor:
    print "Assertion caught for InvalidResistor. Resistor value can't be negative"

try:
    print resistor(1.111111111111111111, "", 20)
except AssertionError:
    print "Assertion caught for required to high precision"

try:
    print resistor(1.111111111111111111, "", 0)
except AssertionError:
    print "Assertion caught for required invalid precision"

try:
    print resistor(1.111111111111111111, "", -2)
except AssertionError:
    print "Assertion caught for required invalid precision"

# Test for invalid arguments types
try:
    resistor("cant be a string")
except InvalidResistor:
    print "Assertion caught for InvalidResistor. Resistor value can't be a string"

try:
    resistor(1, 3)
except AssertionError:
    print "Assertion caught for AssertionError. label can't be a number"

try:
    resistor("10", 3, "30")
except AssertionError:
    print "Assertion caught for AssertionError. digits can't be a number"

# E24 series
print "\n\n"
print "E24 resistors"
for k in range(1, 10):
    print resistor.E24()

print "E12 resistors"
for k in range(1, 10):
    print resistor.E12()

print "E24 resistors - Eng notation"
for k in range(1, 10):
    print resistor.E24_Eng()

print "E12 resistors - Eng notation"
for k in range(1, 10):
    print resistor.E12_Eng()
print "\n\n"


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

# Raw printing
print R0.resistance
print R1.resistance
print R2.resistance
print R3.resistance
print R4.resistance
print R5.resistance
print R6.resistance
print R7.resistance
print R8.resistance
print R9.resistance
print R10.resistance
print R11.resistance
print R12.resistance
print R13.resistance
print R14.resistance
print R15.resistance
print R16.resistance
print R17.resistance
print R18.resistance
print R19.resistance
print R20.resistance
print R21.resistance
print R22.resistance
print R23.resistance
print R24.resistance
print R25.resistance
print R26.resistance
print R27.resistance
print R28.resistance
print R29.resistance
print R30.resistance
print R31.resistance
print R32.resistance
print R33.resistance
print R34.resistance
print R35.resistance
print R36.resistance
print R37.resistance

# Formated Printing - Engeneering Notation and latex symbols
print("\n\n")
print R0.resistanceEng
print R1.resistanceEng
print R2.resistanceEng
print R3.resistanceEng
print R4.resistanceEng
print R5.resistanceEng
print R6.resistanceEng
print R8.resistanceEng
print R9.resistanceEng
print R7.resistanceEng
print R10.resistanceEng
print R11.resistanceEng
print R13.resistanceEng
print R12.resistanceEng
print R14.resistanceEng
print R15.resistanceEng
print R16.resistanceEng
print R17.resistanceEng
print R18.resistanceEng
print R19.resistanceEng
print R20.resistanceEng
print R21.resistanceEng
print R23.resistanceEng
print R22.resistanceEng
print R24.resistanceEng
print R25.resistanceEng
print R27.resistanceEng
print R26.resistanceEng
print R28.resistanceEng
print R29.resistanceEng
print R30.resistanceEng
print R31.resistanceEng
print R32.resistanceEng
print R33.resistanceEng
print R34.resistanceEng
print R35.resistanceEng
print R36.resistanceEng
print R37.resistanceEng

# Parallel resistor association
print "\n\n"
print resistor.parallel(R1, R2)
print resistor.parallel(R1, 30, 40, R2, 1)
print resistor.parallel(R1, R1, R2, R2, 10**9)
print resistor.parallel(1, 2)
print resistor.parallel(1, 1, 1, 1, 1)
print resistor.parallel(20000, 2, 2000, 20)
R38 = resistor(2, "R38", 7)
print resistor.parallel(1000000, 2)
print resistor.parallel(1000000, R38)
print resistor.parallel(1, 2)
print resistor.parallel(1, 2, 3)
print resistor.parallel(1, 2, 3, 4)

# Series resistor association
print "\n\n"
print resistor.series(R1, R2)
print resistor.series(R1, 30, 40, R2, 1)
print resistor.series(R1, R1, R2, R2, 10**9)
print resistor.series(1, 2)
print resistor.series(1, 1, 1, 1, 1)
print resistor.series(20000, 2, 2000, 20)
R38 = resistor(2, "R38", 7)
print resistor.series(1000000, 2)
print resistor.series(1000000, R38)
print resistor.series(1, 2)
print resistor.series(1, 2, 3)
print resistor.series(1, 2, 3, 4)
print resistor.series(1, 0.1, 0.01, 0.001)
R39 = resistor(0.001, "$R_39$", 4)
print resistor.series(1, 0.1, 0.01, R39)
print resistor.series(1, 0.1, 0.01, 0.0001)
R40 = resistor(0.0001, "$R_40$", 5)
print resistor.series(1, 0.1, 0.01, R40)
print resistor.series(1, 10, 100)
print resistor.series(1, 10, 100, 1000)
print resistor.series(10, 100, 1000)
print resistor.series(100, 1000, 10000)
print resistor.series(100, 1000, 100000)
R40 = resistor(0.00121434, "$R_40$", 5)
R41 = resistor(0.00121434, "$R_41$", 2)
print R40.resistanceEng
print R41.resistanceEng

# Making series return a resistor
print('\n')
R42 = resistor.series(100, 1000, 100000, resistor= True)
print R42
print R42.digits
print R42.label
print R42.resistance
print R42.resistanceEng
R43 = resistor(1213.1212, 'R43', 5)
R44 = resistor.series(100, 1000, R43, resistor= True)
print R44
print R44.digits
print R44.label
print R44.resistance
print R44.resistanceEng

# Voltage Divider
print "\n\n"
print resistor.voltageDivider(10, 2, 2)
print resistor.voltageDivider(10, 2, 5)
print resistor.voltageDivider(10, 10000, 5)

# Current Divider
print "\n\n"
aux = resistor.currentDivider(10, 200, 5)
print aux
print engineerNotation(aux, resistor.unit())
print resistor.currentDivider(10, 2, 5)
