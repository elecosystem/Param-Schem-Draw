'''
    Test the inductor output formatting

'''

# Add module path (parent folder)
import os, sys
sys.path.insert(0,os.path.pardir)

from inductor import *
from ParamSchemDraw import ValueOutsideReasonableBounds

# Test assertions for invalid argument values
try:
    inductor(0)
    print "1. Assertion not caught for inductor with value 0"
except InvalidInductor:
    print "1. Assertion caught for InvalidInductor. inductor value can't be zero"

try:
    inductor(-34)
    print "2. Assertion not caught for a negative value"
except InvalidInductor:
    print "2. Assertion caught for InvalidInductor. inductor value can't be negative"

try:
    inductor(-2323213.232, "", 3)
except InvalidInductor:
    print "3. Assertion caught for InvalidInductor. inductor value can't be negative"

try:
    print inductor(1.111111111111111111, "", 20)
except AssertionError:
    print "4. Assertion caught for required too high precision"

try:
    print inductor(1.111111111111111111, "", 0)
except AssertionError:
    print "5. Assertion caught for required invalid precision"

try:
    print inductor(1.111111111111111111, "", -2)
except AssertionError:
    print "6. Assertion caught for required invalid precision"

# Test for invalid arguments types
try:
    inductor("cant be a string")
except InvalidInductor:
    print "7. Assertion caught for InvalidCesistor. inductor value can't be a string"

try:
    inductor(1, 3)
except AssertionError:
    print "8. Assertion caught for AssertionError. label can't be a number"

try:
    inductor("10", 3, "30")
except AssertionError:
    print "9. Assertion caught for AssertionError. digits can't be a number"

# E24 series
print "\n\n"
print "E24 inductor"
for k in range(1, 10):
    print inductor.E24()

print "E12 inductors"
for k in range(1, 10):
    print inductor.E12()

print "E24 inductors - Eng notation"
for k in range(1, 10):
    print inductor.E24_Eng()

print "E12 inductors - Eng notation"
for k in range(1, 10):
    print inductor.E12_Eng()
print "\n\n"


# inductor testing examples
L0  = inductor(1)
L1  = inductor(10)
L2  = inductor(100)
L3  = inductor(1000)
L4  = inductor(10000)
L5  = inductor(100000)
L6  = inductor(1000000)
L7  = inductor(10000000)
L8  = inductor(100000000)
L9  = inductor(999)
L10 = inductor(9999)
L11 = inductor(6512)
L12 = inductor(10345)
L13 = inductor(1000000003)
L14 = inductor(10000045)
L15 = inductor(0.1)
L16 = inductor(0.01)
L17 = inductor(0.001)
L18 = inductor(0.0001)
L19 = inductor(0.00001)
L20 = inductor(0.000001)
L21 = inductor(0.000231)
L22 = inductor(0.234)
L23 = inductor(0.001234)
L24 = inductor(0.000120)
L25 = inductor(0.99999)
L26 = inductor(0.00999)
L27 = inductor(0.009)
L28 = inductor(0.999999999)
L29 = inductor(0.9200001)
L30 = inductor(0.000001)
L31 = inductor(0.192817)
L32 = inductor(0.6512)
L33 = inductor(0.06512)
L34 = inductor(0.006512)
L35 = inductor(0.0006512)
L36 = inductor(0.009999)
L37 = inductor(0.0009999)

# Caw printing
print L0.inductance
print L1.inductance
print L2.inductance
print L3.inductance
print L4.inductance
print L5.inductance
print L6.inductance
print L7.inductance
print L8.inductance
print L9.inductance
print L10.inductance
print L11.inductance
print L12.inductance
print L13.inductance
print L14.inductance
print L15.inductance
print L16.inductance
print L17.inductance
print L18.inductance
print L19.inductance
print L20.inductance
print L21.inductance
print L22.inductance
print L23.inductance
print L24.inductance
print L25.inductance
print L26.inductance
print L27.inductance
print L28.inductance
print L29.inductance
print L30.inductance
print L31.inductance
print L32.inductance
print L33.inductance
print L34.inductance
print L35.inductance
print L36.inductance
print L37.inductance

# Formated Printing - Engeneering Notation and latex symbols
print("\n\n")
print L0.inductanceEng
print L1.inductanceEng
print L2.inductanceEng
print L3.inductanceEng
print L4.inductanceEng
print L5.inductanceEng
print L6.inductanceEng
print L8.inductanceEng
print L9.inductanceEng
print L7.inductanceEng
print L10.inductanceEng
print L11.inductanceEng
print L13.inductanceEng
print L12.inductanceEng
print L14.inductanceEng
print L15.inductanceEng
print L16.inductanceEng
print L17.inductanceEng
print L18.inductanceEng
print L19.inductanceEng
print L20.inductanceEng
print L21.inductanceEng
print L23.inductanceEng
print L22.inductanceEng
print L24.inductanceEng
print L25.inductanceEng
print L27.inductanceEng
print L26.inductanceEng
print L28.inductanceEng
print L29.inductanceEng
print L30.inductanceEng
print L31.inductanceEng
print L32.inductanceEng
print L33.inductanceEng
print L34.inductanceEng
print L35.inductanceEng
print L36.inductanceEng
print L37.inductanceEng

# susceptance
print("\n\n Susceptance - f1 = 100 Hz")
f1 = 100
print L0.susceptance(f1)
print L1.susceptance(f1)
print L2.susceptance(f1)
print L3.susceptance(f1)
print L4.susceptance(f1)
print L5.susceptance(f1)
print L6.susceptance(f1)
print L7.susceptance(f1)
print L8.susceptance(f1)
print L9.susceptance(f1)
print L10.susceptance(f1)
print L11.susceptance(f1)
print L12.susceptance(f1)
print L13.susceptance(f1)
print L14.susceptance(f1)
print L15.susceptance(f1)
print L16.susceptance(f1)


# Formated Printing - Engeneering Notation and latex symbols
print("\n Susceptance Eng - f1 = 100 Hz")
print L0.susceptanceEng(f1)
print L1.susceptanceEng(f1)
print L2.susceptanceEng(f1)
print L3.susceptanceEng(f1)
print L4.susceptanceEng(f1)
print L5.susceptanceEng(f1)
print L6.susceptanceEng(f1)
print L7.susceptanceEng(f1)
print L8.susceptanceEng(f1)
print L9.susceptanceEng(f1)
print L10.susceptanceEng(f1)
print L11.susceptanceEng(f1)
print L12.susceptanceEng(f1)
print L13.susceptanceEng(f1)
print L14.susceptanceEng(f1)
print L15.susceptanceEng(f1)
print L16.susceptanceEng(f1)


print("\n\n Susceptance - f2 = 1000 Hz")
f2 = 1000
print L0.susceptance(f2)
print L1.susceptance(f2)
print L3.susceptance(f2)
print L2.susceptance(f2)
print L4.susceptance(f2)
print L5.susceptance(f2)
print L6.susceptance(f2)
print L7.susceptance(f2)
print L8.susceptance(f2)
print L9.susceptance(f2)
print L10.susceptance(f2)
print L11.susceptance(f2)
print L12.susceptance(f2)
print L13.susceptance(f2)
print L14.susceptance(f2)
print L15.susceptance(f2)
print L16.susceptance(f2)

print("\n Susceptance Eng - f2 = 1000 Hz")
print L0.susceptanceEng(f2)
print L1.susceptanceEng(f2)
print L3.susceptanceEng(f2)
print L2.susceptanceEng(f2)
print L4.susceptanceEng(f2)
print L5.susceptanceEng(f2)
print L6.susceptanceEng(f2)
print L7.susceptanceEng(f2)
print L8.susceptanceEng(f2)
print L9.susceptanceEng(f2)
print L10.susceptanceEng(f2)
print L11.susceptanceEng(f2)
print L12.susceptanceEng(f2)
try:
    print L13.susceptanceEng(f2)
except ValueOutsideReasonableBounds:
    print "L13 inductance, " + L13.inductanceEng + ", is too high"

print L14.susceptanceEng(f2)
print L15.susceptanceEng(f2)
print L16.susceptanceEng(f2)

print("\n\n Susceptance - f3 = 100 000 Hz")
f3 = 100000
print L0.susceptance(f3)
print L1.susceptance(f3)
print L2.susceptance(f3)
print L3.susceptance(f3)
print L4.susceptance(f3)
print L5.susceptance(f3)
print L6.susceptance(f3)
print L7.susceptance(f3)
print L8.susceptance(f3)
print L9.susceptance(f3)
print L10.susceptance(f3)
print L11.susceptance(f3)
print L12.susceptance(f3)
print L13.susceptance(f3)
print L14.susceptance(f3)
print L15.susceptance(f3)
print L16.susceptance(f3)

print("\n Susceptance Eng - f3 = 100 000 Hz")
print L0.susceptanceEng(f3)
print L1.susceptanceEng(f3)
print L3.susceptanceEng(f3)
print L2.susceptanceEng(f3)
print L4.susceptanceEng(f3)
print L5.susceptanceEng(f3)
print L6.susceptanceEng(f3)
try:
    print L7.susceptanceEng(f3)
except ValueOutsideReasonableBounds:
    print "L7 inductance, " + L7.inductanceEng + ", is too high"
try:
    print L8.susceptanceEng(f3)
except ValueOutsideReasonableBounds:
    print "L8 inductance, " + L8.inductanceEng + ", is too high"

print L9.susceptanceEng(f3)
print L10.susceptanceEng(f3)
print L11.susceptanceEng(f3)
print L12.susceptanceEng(f3)
try:
    print L13.susceptanceEng(f3)
except ValueOutsideReasonableBounds:
    print "L13 inductance, " + L13.inductanceEng + ", is too high"
try:
    print L14.susceptanceEng(f3)
except ValueOutsideReasonableBounds:
    print "L14 inductance, " + L14.inductanceEng + ", is too high"

print L15.susceptanceEng(f3)
print L16.susceptanceEng(f3)

'''
    ADMITTANCE
'''
# susceptance
print("\n\n Admiittance - f1 = 100 Hz")
f1 = 100
print L0.admittance(f1)
print L1.admittance(f1)
print L2.admittance(f1)
print L3.admittance(f1)
print L4.admittance(f1)
print L5.admittance(f1)
print L6.admittance(f1)
print L7.admittance(f1)
print L8.admittance(f1)
print L9.admittance(f1)
print L10.admittance(f1)
print L11.admittance(f1)
print L12.admittance(f1)
print L13.admittance(f1)
print L14.admittance(f1)
print L15.admittance(f1)
print L16.admittance(f1)


# Formated Printing - Engeneering Notation and latex symbols
print("\n admittance Eng - f1 = 100 Hz")
print L0.admittanceEng(f1)
print L1.admittanceEng(f1)
print L2.admittanceEng(f1)
print L3.admittanceEng(f1)
print L4.admittanceEng(f1)
print L5.admittanceEng(f1)
print L6.admittanceEng(f1)
print L7.admittanceEng(f1)
print L8.admittanceEng(f1)
print L9.admittanceEng(f1)
print L10.admittanceEng(f1)
print L11.admittanceEng(f1)
print L12.admittanceEng(f1)
print L13.admittanceEng(f1)
print L14.admittanceEng(f1)
print L15.admittanceEng(f1)
print L16.admittanceEng(f1)


print("\n\n admittance - f2 = 1000 Hz")
f2 = 1000
print L0.admittance(f2)
print L1.admittance(f2)
print L3.admittance(f2)
print L2.admittance(f2)
print L4.admittance(f2)
print L5.admittance(f2)
print L6.admittance(f2)
print L7.admittance(f2)
print L8.admittance(f2)
print L9.admittance(f2)
print L10.admittance(f2)
print L11.admittance(f2)
print L12.admittance(f2)
print L13.admittance(f2)
print L14.admittance(f2)
print L15.admittance(f2)
print L16.admittance(f2)

print("\n admittance Eng - f2 = 1000 Hz")
print L0.admittanceEng(f2)
print L1.admittanceEng(f2)
print L3.admittanceEng(f2)
print L2.admittanceEng(f2)
print L4.admittanceEng(f2)
print L5.admittanceEng(f2)
print L6.admittanceEng(f2)
print L7.admittanceEng(f2)
print L8.admittanceEng(f2)
print L9.admittanceEng(f2)
print L10.admittanceEng(f2)
print L11.admittanceEng(f2)
print L12.admittanceEng(f2)
try:
    print L13.admittanceEng(f2)
except ValueOutsideReasonableBounds:
    print "L13 inductance, " + L13.inductanceEng + ", is too high"

print L14.admittanceEng(f2)
print L15.admittanceEng(f2)
print L16.admittanceEng(f2)

print("\n\n admittance - f3 = 100 000 Hz")
f3 = 100000
print L0.admittance(f3)
print L1.admittance(f3)
print L2.admittance(f3)
print L3.admittance(f3)
print L4.admittance(f3)
print L5.admittance(f3)
print L6.admittance(f3)
print L7.admittance(f3)
print L8.admittance(f3)
print L9.admittance(f3)
print L10.admittance(f3)
print L11.admittance(f3)
print L12.admittance(f3)
print L13.admittance(f3)
print L14.admittance(f3)
print L15.admittance(f3)
print L16.admittance(f3)

print("\n admittance Eng - f3 = 100 000 Hz")
print L0.admittanceEng(f3)
print L1.admittanceEng(f3)
print L3.admittanceEng(f3)
print L2.admittanceEng(f3)
print L4.admittanceEng(f3)
print L5.admittanceEng(f3)
print L6.admittanceEng(f3)
try:
    print L7.admittanceEng(f3)
except ValueOutsideReasonableBounds:
    print "L7 inductance, " + L7.inductanceEng + ", is too high"
try:
    print L8.admittanceEng(f3)
except ValueOutsideReasonableBounds:
    print "L8 inductance, " + L8.inductanceEng + ", is too high"

print L9.admittanceEng(f3)
print L10.admittanceEng(f3)
print L11.admittanceEng(f3)
print L12.admittanceEng(f3)
try:
    print L13.admittanceEng(f3)
except ValueOutsideReasonableBounds:
    print "L13 inductance, " + L13.inductanceEng + ", is too high"
try:
    print L14.admittanceEng(f3)
except ValueOutsideReasonableBounds:
    print "L14 inductance, " + L14.inductanceEng + ", is too high"

print L15.admittanceEng(f3)
print L16.admittanceEng(f3)


'''
    REACTANCE
'''
# susceptance
print("\n\n reactance - f1 = 100 Hz")
f1 = 100
print L0.reactance(f1)
print L1.reactance(f1)
print L2.reactance(f1)
print L3.reactance(f1)
print L4.reactance(f1)
print L5.reactance(f1)
print L6.reactance(f1)
print L7.reactance(f1)
print L8.reactance(f1)
print L9.reactance(f1)
print L10.reactance(f1)
print L11.reactance(f1)
print L12.reactance(f1)
print L13.reactance(f1)
print L14.reactance(f1)
print L15.reactance(f1)
print L16.reactance(f1)


# Formated Printing - Engeneering Notation and latex symbols
print("\n reactance Eng - f1 = 100 Hz")
print L0.reactanceEng(f1)
print L1.reactanceEng(f1)
print L2.reactanceEng(f1)
print L3.reactanceEng(f1)
print L4.reactanceEng(f1)
print L5.reactanceEng(f1)
print L6.reactanceEng(f1)
print L7.reactanceEng(f1)
print L8.reactanceEng(f1)
print L9.reactanceEng(f1)
print L10.reactanceEng(f1)
print L11.reactanceEng(f1)
print L12.reactanceEng(f1)
print L13.reactanceEng(f1)
print L14.reactanceEng(f1)
print L15.reactanceEng(f1)
print L16.reactanceEng(f1)


print("\n\n reactance - f2 = 1000 Hz")
f2 = 1000
print L0.reactance(f2)
print L1.reactance(f2)
print L3.reactance(f2)
print L2.reactance(f2)
print L4.reactance(f2)
print L5.reactance(f2)
print L6.reactance(f2)
print L7.reactance(f2)
print L8.reactance(f2)
print L9.reactance(f2)
print L10.reactance(f2)
print L11.reactance(f2)
print L12.reactance(f2)
print L13.reactance(f2)
print L14.reactance(f2)
print L15.reactance(f2)
print L16.reactance(f2)

print("\n reactance Eng - f2 = 1000 Hz")
print L0.reactanceEng(f2)
print L1.reactanceEng(f2)
print L3.reactanceEng(f2)
print L2.reactanceEng(f2)
print L4.reactanceEng(f2)
print L5.reactanceEng(f2)
print L6.reactanceEng(f2)
print L7.reactanceEng(f2)
print L8.reactanceEng(f2)
print L9.reactanceEng(f2)
print L10.reactanceEng(f2)
print L11.reactanceEng(f2)
print L12.reactanceEng(f2)
try:
    print L13.reactanceEng(f2)
except ValueOutsideReasonableBounds:
    print "L13 inductance, " + L13.inductanceEng + ", is too high"

print L14.reactanceEng(f2)
print L15.reactanceEng(f2)
print L16.reactanceEng(f2)

print("\n\n reactance - f3 = 100 000 Hz")
f3 = 100000
print L0.reactance(f3)
print L1.reactance(f3)
print L2.reactance(f3)
print L3.reactance(f3)
print L4.reactance(f3)
print L5.reactance(f3)
print L6.reactance(f3)
print L7.reactance(f3)
print L8.reactance(f3)
print L9.reactance(f3)
print L10.reactance(f3)
print L11.reactance(f3)
print L12.reactance(f3)
print L13.reactance(f3)
print L14.reactance(f3)
print L15.reactance(f3)
print L16.reactance(f3)

print("\n reactance Eng - f3 = 100 000 Hz")
print L0.reactanceEng(f3)
print L1.reactanceEng(f3)
print L3.reactanceEng(f3)
print L2.reactanceEng(f3)
print L4.reactanceEng(f3)
print L5.reactanceEng(f3)
print L6.reactanceEng(f3)
try:
    print L7.reactanceEng(f3)
except ValueOutsideReasonableBounds:
    print "L7 inductance, " + L7.inductanceEng + ", is too high"
try:
    print L8.reactanceEng(f3)
except ValueOutsideReasonableBounds:
    print "L8 inductance, " + L8.inductanceEng + ", is too high"

print L9.reactanceEng(f3)
print L10.reactanceEng(f3)
print L11.reactanceEng(f3)
print L12.reactanceEng(f3)
try:
    print L13.reactanceEng(f3)
except ValueOutsideReasonableBounds:
    print "L13 inductance, " + L13.inductanceEng + ", is too high"
try:
    print L14.reactanceEng(f3)
except ValueOutsideReasonableBounds:
    print "L14 inductance, " + L14.inductanceEng + ", is too high"

print L15.reactanceEng(f3)
print L16.reactanceEng(f3)


'''
    IMPEDANCE
'''
# susceptance
print("\n\n Impedance - f1 = 100 Hz")
f1 = 100
print L0.impedance(f1)
print L1.impedance(f1)
print L2.impedance(f1)
print L3.impedance(f1)
print L4.impedance(f1)
print L5.impedance(f1)
print L6.impedance(f1)
print L7.impedance(f1)
print L8.impedance(f1)
print L9.impedance(f1)
print L10.impedance(f1)
print L11.impedance(f1)
print L12.impedance(f1)
print L13.impedance(f1)
print L14.impedance(f1)
print L15.impedance(f1)
print L16.impedance(f1)


# Formated Printing - Engeneering Notation and latex symbols
print("\n impedance Eng - f1 = 100 Hz")
print L0.impedanceEng(f1)
print L1.impedanceEng(f1)
print L2.impedanceEng(f1)
print L3.impedanceEng(f1)
print L4.impedanceEng(f1)
print L5.impedanceEng(f1)
print L6.impedanceEng(f1)
print L7.impedanceEng(f1)
print L8.impedanceEng(f1)
print L9.impedanceEng(f1)
print L10.impedanceEng(f1)
print L11.impedanceEng(f1)
print L12.impedanceEng(f1)
print L13.impedanceEng(f1)
print L14.impedanceEng(f1)
print L15.impedanceEng(f1)
print L16.impedanceEng(f1)


print("\n\n impedance - f2 = 1000 Hz")
f2 = 1000
print L0.impedance(f2)
print L1.impedance(f2)
print L3.impedance(f2)
print L2.impedance(f2)
print L4.impedance(f2)
print L5.impedance(f2)
print L6.impedance(f2)
print L7.impedance(f2)
print L8.impedance(f2)
print L9.impedance(f2)
print L10.impedance(f2)
print L11.impedance(f2)
print L12.impedance(f2)
print L13.impedance(f2)
print L14.impedance(f2)
print L15.impedance(f2)
print L16.impedance(f2)

print("\n impedance Eng - f2 = 1000 Hz")
print L0.impedanceEng(f2)
print L1.impedanceEng(f2)
print L3.impedanceEng(f2)
print L2.impedanceEng(f2)
print L4.impedanceEng(f2)
print L5.impedanceEng(f2)
print L6.impedanceEng(f2)
print L7.impedanceEng(f2)
print L8.impedanceEng(f2)
print L9.impedanceEng(f2)
print L10.impedanceEng(f2)
print L11.impedanceEng(f2)
print L12.impedanceEng(f2)
try:
    print L13.impedanceEng(f2)
except ValueOutsideReasonableBounds:
    print "L13 inductance, " + L13.inductanceEng + ", is too high"

print L14.impedanceEng(f2)
print L15.impedanceEng(f2)
print L16.impedanceEng(f2)

print("\n\n impedance - f3 = 100 000 Hz")
f3 = 100000
print L0.impedance(f3)
print L1.impedance(f3)
print L2.impedance(f3)
print L3.impedance(f3)
print L4.impedance(f3)
print L5.impedance(f3)
print L6.impedance(f3)
print L7.impedance(f3)
print L8.impedance(f3)
print L9.impedance(f3)
print L10.impedance(f3)
print L11.impedance(f3)
print L12.impedance(f3)
print L13.impedance(f3)
print L14.impedance(f3)
print L15.impedance(f3)
print L16.impedance(f3)

print("\n impedance Eng - f3 = 100 000 Hz")
print L0.impedanceEng(f3)
print L1.impedanceEng(f3)
print L3.impedanceEng(f3)
print L2.impedanceEng(f3)
print L4.impedanceEng(f3)
print L5.impedanceEng(f3)
print L6.impedanceEng(f3)
try:
    print L7.impedanceEng(f3)
except ValueOutsideReasonableBounds:
    print "L7 inductance, " + L7.inductanceEng + ", is too high"
try:
    print L8.impedanceEng(f3)
except ValueOutsideReasonableBounds:
    print "L8 inductance, " + L8.inductanceEng + ", is too high"

print L9.impedanceEng(f3)
print L10.impedanceEng(f3)
print L11.impedanceEng(f3)
print L12.impedanceEng(f3)
try:
    print L13.impedanceEng(f3)
except ValueOutsideReasonableBounds:
    print "L13 inductance, " + L13.inductanceEng + ", is too high"
try:
    print L14.impedanceEng(f3)
except ValueOutsideReasonableBounds:
    print "L14 inductance, " + L14.inductanceEng + ", is too high"

print L15.impedanceEng(f3)
print L16.impedanceEng(f3)



# Parallel inductor association
print "\n\n Parallel Association"
print inductor.parallel(L1, L2)
print inductor.parallel(L1, 30, 40, L2, 1)
print inductor.parallel(L1, L1, L2, L2, 10**9)
print inductor.parallel(1, 2)
print inductor.parallel(1, 1, 1, 1, 1)
print inductor.parallel(20000, 2, 2000, 20)
L38 = inductor(2, "L38", 7)
print inductor.parallel(1000000, 2)
print inductor.parallel(1000000, L38)
print inductor.parallel(1, 2)
print inductor.parallel(1, 2, 3)
print inductor.parallel(1, 2, 3, 4)

# Series inductor association
print "\n\n Series Association"
print inductor.series(L1, L2)
print inductor.series(L1, 30, 40, L2, 1)
print inductor.series(L1, L1, L2, L2, 10**9)
print inductor.series(1, 2)
print inductor.series(1, 1, 1, 1, 1)
print inductor.series(20000, 2, 2000, 20)
L38 = inductor(2, "L38", 7)
print inductor.series(1000000, 2)
print inductor.series(1000000, L38)
print inductor.series(1, 2)
print inductor.series(1, 2, 3)
print inductor.series(1, 2, 3, 4)
print inductor.series(1, 0.1, 0.01, 0.001)
L39 = inductor(0.001, "$L_39$", 4)
print inductor.series(1, 0.1, 0.01, L39)
print inductor.series(1, 0.1, 0.01, 0.0001)
L40 = inductor(0.0001, "$L_40$", 5)
print inductor.series(1, 0.1, 0.01, L40)
print inductor.series(1, 10, 100)
print inductor.series(1, 10, 100, 1000)
print inductor.series(10, 100, 1000)
print inductor.series(100, 1000, 10000)
print inductor.series(100, 1000, 100000)

L40 = inductor(0.00121434, "$L_40$", 5)
L41 = inductor(0.00121434, "$L_41$", 2)
print L40.inductanceEng
print L41.inductanceEng

# Making series return a inductor
print('\n')
L42 = inductor.series(100, 1000, 100000, inductor=True)
print L42
print L42.digits
print L42.label
print L42.inductance
print L42.inductanceEng
L43 = inductor(1213.1212, 'L43', 5)
L44 = inductor.series(100, 1000, L43, inductor=True)
print L44
print L44.digits
print L44.label
print L44.inductance
print L44.inductanceEng

# Voltage Divider
print "\n\n Voltage Divider"
print inductor.voltageDivider(10, 2, 2, 100)
Veq = inductor.voltageDivider(10, 2, 2, 100, vSource=True)
print Veq.voltageEng
print inductor.voltageDivider(10, 2, 2, 100*10**6)
print inductor.voltageDivider(10, 2, 5, 100*10**6)
print inductor.voltageDivider(10, 10000, 5, 100*10**6)

# Lurrent Divider
print "\n\n Current Divider"
aux = inductor.currentDivider(10, 200, 5, 87*10**3)
print aux
aux2 = inductor.currentDivider(10, 200, 5, 87*10**3, iSource=True)
print aux2.currentEng
print engineerNotation(aux, 'A')
print inductor.currentDivider(10, 2, 5, 10)
