'''
    Test the capacitor output formatting

'''

# Add module path (parent folder)
import os, sys
sys.path.insert(0,os.path.pardir)

from capacitor import *
from ParamSchemDraw import ValueOutsideReasonableBounds
# Test assertions for invalid argument values
try:
    capacitor(0)
    print "1. Assertion not caught for capacitor with value 0"
except InvalidCapacitor:
    print "1. Assertion caught for InvalidCapacitor. Capacitor value can't be zero"

try:
    capacitor(-34)
    print "2. Assertion not caught for a negative value"
except InvalidCapacitor:
    print "2. Assertion caught for InvalidCapacitor. Capacitor value can't be negative"

try:
    capacitor(-2323213.232, "", 3)
except InvalidCapacitor:
    print "3. Assertion caught for InvalidCapacitor. Capacitor value can't be negative"

try:
    print capacitor(1.111111111111111111, "", 20)
except AssertionError:
    print "4. Assertion caught for required too high precision"

try:
    print capacitor(1.111111111111111111, "", 0)
except AssertionError:
    print "5. Assertion caught for required invalid precision"

try:
    print capacitor(1.111111111111111111, "", -2)
except AssertionError:
    print "6. Assertion caught for required invalid precision"

# Test for invalid arguments types
try:
    capacitor("cant be a string")
except InvalidCapacitor:
    print "7. Assertion caught for InvalidCesistor. Capacitor value can't be a string"

try:
    capacitor(1, 3)
except AssertionError:
    print "8. Assertion caught for AssertionError. label can't be a number"

try:
    capacitor("10", 3, "30")
except AssertionError:
    print "9. Assertion caught for AssertionError. digits can't be a number"


'''
    Charge Equation tests

'''
print "\n\n Charge Equation"
print capacitor.chargeEq(capacitance=1e-6, charge=2)
print capacitor.chargeEq(capacitance=1e-6, voltage=2)
print capacitor.chargeEq(voltage=1.121, charge=3.5622)
print capacitor.chargeEq(capacitance=1e-6, charge=3)

print capacitor.chargeEqEng(capacitance=1e-6, charge=2)
print capacitor.chargeEqEng(capacitance=1e-6, voltage=2)
print capacitor.chargeEqEng(voltage=1.121, charge=3.5622)
print capacitor.chargeEqEng(capacitance=1e-6, charge=3)

try:
    print capacitor.chargeEq(capacitance=1e-6, charge='r')
except AssertionError:
    print "Assertion caught for charge value that is not a float or integer"
try:
    print capacitor.chargeEq(capacitance=1e-6)
except AssertionError:
    print "Assertion caught for invalid number of arguments"
try:
    print capacitor.chargeEq()
except AssertionError:
    print "Assertion caught for invalid number of arguments"

# E24 series
print "\n\n"
print "E24 Capacitor"
for k in range(1, 10):
    print capacitor.E24()

print "E12 capacitors"
for k in range(1, 10):
    print capacitor.E12()

print "E24 capacitors - Eng notation"
for k in range(1, 10):
    print capacitor.E24_Eng()

print "E12 capacitors - Eng notation"
for k in range(1, 10):
    print capacitor.E12_Eng()
print "\n\n"


# Capacitor testing examples
C0  = capacitor(1)
C1  = capacitor(10)
C2  = capacitor(100)
C3  = capacitor(1000)
C4  = capacitor(10000)
C5  = capacitor(100000)
C6  = capacitor(1000000)
C7  = capacitor(10000000)
C8  = capacitor(100000000)
C9  = capacitor(999)
C10 = capacitor(9999)
C11 = capacitor(6512)
C12 = capacitor(10345)
C13 = capacitor(1000000003)
C14 = capacitor(10000045)
C15 = capacitor(0.1)
C16 = capacitor(0.01)
C17 = capacitor(0.001)
C18 = capacitor(0.0001)
C19 = capacitor(0.00001)
C20 = capacitor(0.000001)
C21 = capacitor(0.000231)
C22 = capacitor(0.234)
C23 = capacitor(0.001234)
C24 = capacitor(0.000120)
C25 = capacitor(0.99999)
C26 = capacitor(0.00999)
C27 = capacitor(0.009)
C28 = capacitor(0.999999999)
C29 = capacitor(0.9200001)
C30 = capacitor(0.000001)
C31 = capacitor(0.192817)
C32 = capacitor(0.6512)
C33 = capacitor(0.06512)
C34 = capacitor(0.006512)
C35 = capacitor(0.0006512)
C36 = capacitor(0.009999)
C37 = capacitor(0.0009999)

# Caw printing
print C0.capacitance
print C1.capacitance
print C2.capacitance
print C3.capacitance
print C4.capacitance
print C5.capacitance
print C6.capacitance
print C7.capacitance
print C8.capacitance
print C9.capacitance
print C10.capacitance
print C11.capacitance
print C12.capacitance
print C13.capacitance
print C14.capacitance
print C15.capacitance
print C16.capacitance
print C17.capacitance
print C18.capacitance
print C19.capacitance
print C20.capacitance
print C21.capacitance
print C22.capacitance
print C23.capacitance
print C24.capacitance
print C25.capacitance
print C26.capacitance
print C27.capacitance
print C28.capacitance
print C29.capacitance
print C30.capacitance
print C31.capacitance
print C32.capacitance
print C33.capacitance
print C34.capacitance
print C35.capacitance
print C36.capacitance
print C37.capacitance

# Formated Printing - Engeneering Notation and latex symbols
print("\n\n")
print C0.capacitanceEng
print C1.capacitanceEng
print C2.capacitanceEng
print C3.capacitanceEng
print C4.capacitanceEng
print C5.capacitanceEng
print C6.capacitanceEng
print C8.capacitanceEng
print C9.capacitanceEng
print C7.capacitanceEng
print C10.capacitanceEng
print C11.capacitanceEng
print C13.capacitanceEng
print C12.capacitanceEng
print C14.capacitanceEng
print C15.capacitanceEng
print C16.capacitanceEng
print C17.capacitanceEng
print C18.capacitanceEng
print C19.capacitanceEng
print C20.capacitanceEng
print C21.capacitanceEng
print C23.capacitanceEng
print C22.capacitanceEng
print C24.capacitanceEng
print C25.capacitanceEng
print C27.capacitanceEng
print C26.capacitanceEng
print C28.capacitanceEng
print C29.capacitanceEng
print C30.capacitanceEng
print C31.capacitanceEng
print C32.capacitanceEng
print C33.capacitanceEng
print C34.capacitanceEng
print C35.capacitanceEng
print C36.capacitanceEng
print C37.capacitanceEng

# susceptance
print("\n\n Susceptance - f1 = 100 Hz")
f1 = 100
print C0.susceptance(f1)
print C1.susceptance(f1)
print C2.susceptance(f1)
print C3.susceptance(f1)
print C4.susceptance(f1)
print C5.susceptance(f1)
print C6.susceptance(f1)
print C7.susceptance(f1)
print C8.susceptance(f1)
print C9.susceptance(f1)
print C10.susceptance(f1)
print C11.susceptance(f1)
print C12.susceptance(f1)
print C13.susceptance(f1)
print C14.susceptance(f1)
print C15.susceptance(f1)
print C16.susceptance(f1)


# Formated Printing - Engeneering Notation and latex symbols
print("\n Susceptance Eng - f1 = 100 Hz")
print C0.susceptanceEng(f1)
print C1.susceptanceEng(f1)
print C2.susceptanceEng(f1)
print C3.susceptanceEng(f1)
print C4.susceptanceEng(f1)
print C5.susceptanceEng(f1)
print C6.susceptanceEng(f1)
print C7.susceptanceEng(f1)
print C8.susceptanceEng(f1)
print C9.susceptanceEng(f1)
print C10.susceptanceEng(f1)
print C11.susceptanceEng(f1)
print C12.susceptanceEng(f1)
print C13.susceptanceEng(f1)
print C14.susceptanceEng(f1)
print C15.susceptanceEng(f1)
print C16.susceptanceEng(f1)


print("\n\n Susceptance - f2 = 1000 Hz")
f2 = 1000
print C0.susceptance(f2)
print C1.susceptance(f2)
print C3.susceptance(f2)
print C2.susceptance(f2)
print C4.susceptance(f2)
print C5.susceptance(f2)
print C6.susceptance(f2)
print C7.susceptance(f2)
print C8.susceptance(f2)
print C9.susceptance(f2)
print C10.susceptance(f2)
print C11.susceptance(f2)
print C12.susceptance(f2)
print C13.susceptance(f2)
print C14.susceptance(f2)
print C15.susceptance(f2)
print C16.susceptance(f2)

print("\n Susceptance Eng - f2 = 1000 Hz")
print C0.susceptanceEng(f2)
print C1.susceptanceEng(f2)
print C3.susceptanceEng(f2)
print C2.susceptanceEng(f2)
print C4.susceptanceEng(f2)
print C5.susceptanceEng(f2)
print C6.susceptanceEng(f2)
print C7.susceptanceEng(f2)
print C8.susceptanceEng(f2)
print C9.susceptanceEng(f2)
print C10.susceptanceEng(f2)
print C11.susceptanceEng(f2)
print C12.susceptanceEng(f2)
try:
    print C13.susceptanceEng(f2)
except ValueOutsideReasonableBounds:
    print "C13 capacitance, " + C13.capacitanceEng + ", is too high"

print C14.susceptanceEng(f2)
print C15.susceptanceEng(f2)
print C16.susceptanceEng(f2)

print("\n\n Susceptance - f3 = 100 000 Hz")
f3 = 100000
print C0.susceptance(f3)
print C1.susceptance(f3)
print C2.susceptance(f3)
print C3.susceptance(f3)
print C4.susceptance(f3)
print C5.susceptance(f3)
print C6.susceptance(f3)
print C7.susceptance(f3)
print C8.susceptance(f3)
print C9.susceptance(f3)
print C10.susceptance(f3)
print C11.susceptance(f3)
print C12.susceptance(f3)
print C13.susceptance(f3)
print C14.susceptance(f3)
print C15.susceptance(f3)
print C16.susceptance(f3)

print("\n Susceptance Eng - f3 = 100 000 Hz")
print C0.susceptanceEng(f3)
print C1.susceptanceEng(f3)
print C3.susceptanceEng(f3)
print C2.susceptanceEng(f3)
print C4.susceptanceEng(f3)
print C5.susceptanceEng(f3)
print C6.susceptanceEng(f3)
try:
    print C7.susceptanceEng(f3)
except ValueOutsideReasonableBounds:
    print "C7 capacitance, " + C7.capacitanceEng + ", is too high"
try:
    print C8.susceptanceEng(f3)
except ValueOutsideReasonableBounds:
    print "C8 capacitance, " + C8.capacitanceEng + ", is too high"

print C9.susceptanceEng(f3)
print C10.susceptanceEng(f3)
print C11.susceptanceEng(f3)
print C12.susceptanceEng(f3)
try:
    print C13.susceptanceEng(f3)
except ValueOutsideReasonableBounds:
    print "C13 capacitance, " + C13.capacitanceEng + ", is too high"
try:
    print C14.susceptanceEng(f3)
except ValueOutsideReasonableBounds:
    print "C14 capacitance, " + C14.capacitanceEng + ", is too high"

print C15.susceptanceEng(f3)
print C16.susceptanceEng(f3)

'''
    ADMITTANCE
'''
# susceptance
print("\n\n Susceptance - f1 = 100 Hz")
f1 = 100
print C0.admittance(f1)
print C1.admittance(f1)
print C2.admittance(f1)
print C3.admittance(f1)
print C4.admittance(f1)
print C5.admittance(f1)
print C6.admittance(f1)
print C7.admittance(f1)
print C8.admittance(f1)
print C9.admittance(f1)
print C10.admittance(f1)
print C11.admittance(f1)
print C12.admittance(f1)
print C13.admittance(f1)
print C14.admittance(f1)
print C15.admittance(f1)
print C16.admittance(f1)


# Formated Printing - Engeneering Notation and latex symbols
print("\n admittance Eng - f1 = 100 Hz")
print C0.admittanceEng(f1)
print C1.admittanceEng(f1)
print C2.admittanceEng(f1)
print C3.admittanceEng(f1)
print C4.admittanceEng(f1)
print C5.admittanceEng(f1)
print C6.admittanceEng(f1)
print C7.admittanceEng(f1)
print C8.admittanceEng(f1)
print C9.admittanceEng(f1)
print C10.admittanceEng(f1)
print C11.admittanceEng(f1)
print C12.admittanceEng(f1)
print C13.admittanceEng(f1)
print C14.admittanceEng(f1)
print C15.admittanceEng(f1)
print C16.admittanceEng(f1)


print("\n\n admittance - f2 = 1000 Hz")
f2 = 1000
print C0.admittance(f2)
print C1.admittance(f2)
print C3.admittance(f2)
print C2.admittance(f2)
print C4.admittance(f2)
print C5.admittance(f2)
print C6.admittance(f2)
print C7.admittance(f2)
print C8.admittance(f2)
print C9.admittance(f2)
print C10.admittance(f2)
print C11.admittance(f2)
print C12.admittance(f2)
print C13.admittance(f2)
print C14.admittance(f2)
print C15.admittance(f2)
print C16.admittance(f2)

print("\n admittance Eng - f2 = 1000 Hz")
print C0.admittanceEng(f2)
print C1.admittanceEng(f2)
print C3.admittanceEng(f2)
print C2.admittanceEng(f2)
print C4.admittanceEng(f2)
print C5.admittanceEng(f2)
print C6.admittanceEng(f2)
print C7.admittanceEng(f2)
print C8.admittanceEng(f2)
print C9.admittanceEng(f2)
print C10.admittanceEng(f2)
print C11.admittanceEng(f2)
print C12.admittanceEng(f2)
try:
    print C13.admittanceEng(f2)
except ValueOutsideReasonableBounds:
    print "C13 capacitance, " + C13.capacitanceEng + ", is too high"

print C14.admittanceEng(f2)
print C15.admittanceEng(f2)
print C16.admittanceEng(f2)

print("\n\n admittance - f3 = 100 000 Hz")
f3 = 100000
print C0.admittance(f3)
print C1.admittance(f3)
print C2.admittance(f3)
print C3.admittance(f3)
print C4.admittance(f3)
print C5.admittance(f3)
print C6.admittance(f3)
print C7.admittance(f3)
print C8.admittance(f3)
print C9.admittance(f3)
print C10.admittance(f3)
print C11.admittance(f3)
print C12.admittance(f3)
print C13.admittance(f3)
print C14.admittance(f3)
print C15.admittance(f3)
print C16.admittance(f3)

print("\n admittance Eng - f3 = 100 000 Hz")
print C0.admittanceEng(f3)
print C1.admittanceEng(f3)
print C3.admittanceEng(f3)
print C2.admittanceEng(f3)
print C4.admittanceEng(f3)
print C5.admittanceEng(f3)
print C6.admittanceEng(f3)
try:
    print C7.admittanceEng(f3)
except ValueOutsideReasonableBounds:
    print "C7 capacitance, " + C7.capacitanceEng + ", is too high"
try:
    print C8.admittanceEng(f3)
except ValueOutsideReasonableBounds:
    print "C8 capacitance, " + C8.capacitanceEng + ", is too high"

print C9.admittanceEng(f3)
print C10.admittanceEng(f3)
print C11.admittanceEng(f3)
print C12.admittanceEng(f3)
try:
    print C13.admittanceEng(f3)
except ValueOutsideReasonableBounds:
    print "C13 capacitance, " + C13.capacitanceEng + ", is too high"
try:
    print C14.admittanceEng(f3)
except ValueOutsideReasonableBounds:
    print "C14 capacitance, " + C14.capacitanceEng + ", is too high"

print C15.admittanceEng(f3)
print C16.admittanceEng(f3)


'''
    REACTANCE
'''
# susceptance
print("\n\n reactance - f1 = 100 Hz")
f1 = 100
print C0.reactance(f1)
print C1.reactance(f1)
print C2.reactance(f1)
print C3.reactance(f1)
print C4.reactance(f1)
print C5.reactance(f1)
print C6.reactance(f1)
print C7.reactance(f1)
print C8.reactance(f1)
print C9.reactance(f1)
print C10.reactance(f1)
print C11.reactance(f1)
print C12.reactance(f1)
print C13.reactance(f1)
print C14.reactance(f1)
print C15.reactance(f1)
print C16.reactance(f1)


# Formated Printing - Engeneering Notation and latex symbols
print("\n reactance Eng - f1 = 100 Hz")
print C0.reactanceEng(f1)
print C1.reactanceEng(f1)
print C2.reactanceEng(f1)
print C3.reactanceEng(f1)
print C4.reactanceEng(f1)
print C5.reactanceEng(f1)
print C6.reactanceEng(f1)
print C7.reactanceEng(f1)
print C8.reactanceEng(f1)
print C9.reactanceEng(f1)
print C10.reactanceEng(f1)
print C11.reactanceEng(f1)
print C12.reactanceEng(f1)
print C13.reactanceEng(f1)
print C14.reactanceEng(f1)
print C15.reactanceEng(f1)
print C16.reactanceEng(f1)


print("\n\n reactance - f2 = 1000 Hz")
f2 = 1000
print C0.reactance(f2)
print C1.reactance(f2)
print C3.reactance(f2)
print C2.reactance(f2)
print C4.reactance(f2)
print C5.reactance(f2)
print C6.reactance(f2)
print C7.reactance(f2)
print C8.reactance(f2)
print C9.reactance(f2)
print C10.reactance(f2)
print C11.reactance(f2)
print C12.reactance(f2)
print C13.reactance(f2)
print C14.reactance(f2)
print C15.reactance(f2)
print C16.reactance(f2)

print("\n reactance Eng - f2 = 1000 Hz")
print C0.reactanceEng(f2)
print C1.reactanceEng(f2)
print C3.reactanceEng(f2)
print C2.reactanceEng(f2)
print C4.reactanceEng(f2)
print C5.reactanceEng(f2)
print C6.reactanceEng(f2)
print C7.reactanceEng(f2)
print C8.reactanceEng(f2)
print C9.reactanceEng(f2)
print C10.reactanceEng(f2)
print C11.reactanceEng(f2)
print C12.reactanceEng(f2)
try:
    print C13.reactanceEng(f2)
except ValueOutsideReasonableBounds:
    print "C13 capacitance, " + C13.capacitanceEng + ", is too high"

print C14.reactanceEng(f2)
print C15.reactanceEng(f2)
print C16.reactanceEng(f2)

print("\n\n reactance - f3 = 100 000 Hz")
f3 = 100000
print C0.reactance(f3)
print C1.reactance(f3)
print C2.reactance(f3)
print C3.reactance(f3)
print C4.reactance(f3)
print C5.reactance(f3)
print C6.reactance(f3)
print C7.reactance(f3)
print C8.reactance(f3)
print C9.reactance(f3)
print C10.reactance(f3)
print C11.reactance(f3)
print C12.reactance(f3)
print C13.reactance(f3)
print C14.reactance(f3)
print C15.reactance(f3)
print C16.reactance(f3)

print("\n reactance Eng - f3 = 100 000 Hz")
print C0.reactanceEng(f3)
print C1.reactanceEng(f3)
print C3.reactanceEng(f3)
print C2.reactanceEng(f3)
print C4.reactanceEng(f3)
print C5.reactanceEng(f3)
print C6.reactanceEng(f3)
try:
    print C7.reactanceEng(f3)
except ValueOutsideReasonableBounds:
    print "C7 capacitance, " + C7.capacitanceEng + ", is too high"
try:
    print C8.reactanceEng(f3)
except ValueOutsideReasonableBounds:
    print "C8 capacitance, " + C8.capacitanceEng + ", is too high"

print C9.reactanceEng(f3)
print C10.reactanceEng(f3)
print C11.reactanceEng(f3)
print C12.reactanceEng(f3)
try:
    print C13.reactanceEng(f3)
except ValueOutsideReasonableBounds:
    print "C13 capacitance, " + C13.capacitanceEng + ", is too high"
try:
    print C14.reactanceEng(f3)
except ValueOutsideReasonableBounds:
    print "C14 capacitance, " + C14.capacitanceEng + ", is too high"

print C15.reactanceEng(f3)
print C16.reactanceEng(f3)


'''
    IMPEDANCE
'''
# susceptance
print("\n\n Impedance - f1 = 100 Hz")
f1 = 100
print C0.impedance(f1)
print C1.impedance(f1)
print C2.impedance(f1)
print C3.impedance(f1)
print C4.impedance(f1)
print C5.impedance(f1)
print C6.impedance(f1)
print C7.impedance(f1)
print C8.impedance(f1)
print C9.impedance(f1)
print C10.impedance(f1)
print C11.impedance(f1)
print C12.impedance(f1)
print C13.impedance(f1)
print C14.impedance(f1)
print C15.impedance(f1)
print C16.impedance(f1)


# Formated Printing - Engeneering Notation and latex symbols
print("\n impedance Eng - f1 = 100 Hz")
print C0.impedanceEng(f1)
print C1.impedanceEng(f1)
print C2.impedanceEng(f1)
print C3.impedanceEng(f1)
print C4.impedanceEng(f1)
print C5.impedanceEng(f1)
print C6.impedanceEng(f1)
print C7.impedanceEng(f1)
print C8.impedanceEng(f1)
print C9.impedanceEng(f1)
print C10.impedanceEng(f1)
print C11.impedanceEng(f1)
print C12.impedanceEng(f1)
print C13.impedanceEng(f1)
print C14.impedanceEng(f1)
print C15.impedanceEng(f1)
print C16.impedanceEng(f1)


print("\n\n impedance - f2 = 1000 Hz")
f2 = 1000
print C0.impedance(f2)
print C1.impedance(f2)
print C3.impedance(f2)
print C2.impedance(f2)
print C4.impedance(f2)
print C5.impedance(f2)
print C6.impedance(f2)
print C7.impedance(f2)
print C8.impedance(f2)
print C9.impedance(f2)
print C10.impedance(f2)
print C11.impedance(f2)
print C12.impedance(f2)
print C13.impedance(f2)
print C14.impedance(f2)
print C15.impedance(f2)
print C16.impedance(f2)

print("\n impedance Eng - f2 = 1000 Hz")
print C0.impedanceEng(f2)
print C1.impedanceEng(f2)
print C3.impedanceEng(f2)
print C2.impedanceEng(f2)
print C4.impedanceEng(f2)
print C5.impedanceEng(f2)
print C6.impedanceEng(f2)
print C7.impedanceEng(f2)
print C8.impedanceEng(f2)
print C9.impedanceEng(f2)
print C10.impedanceEng(f2)
print C11.impedanceEng(f2)
print C12.impedanceEng(f2)
try:
    print C13.impedanceEng(f2)
except ValueOutsideReasonableBounds:
    print "C13 capacitance, " + C13.capacitanceEng + ", is too high"

print C14.impedanceEng(f2)
print C15.impedanceEng(f2)
print C16.impedanceEng(f2)

print("\n\n impedance - f3 = 100 000 Hz")
f3 = 100000
print C0.impedance(f3)
print C1.impedance(f3)
print C2.impedance(f3)
print C3.impedance(f3)
print C4.impedance(f3)
print C5.impedance(f3)
print C6.impedance(f3)
print C7.impedance(f3)
print C8.impedance(f3)
print C9.impedance(f3)
print C10.impedance(f3)
print C11.impedance(f3)
print C12.impedance(f3)
print C13.impedance(f3)
print C14.impedance(f3)
print C15.impedance(f3)
print C16.impedance(f3)

print("\n impedance Eng - f3 = 100 000 Hz")
print C0.impedanceEng(f3)
print C1.impedanceEng(f3)
print C3.impedanceEng(f3)
print C2.impedanceEng(f3)
print C4.impedanceEng(f3)
print C5.impedanceEng(f3)
print C6.impedanceEng(f3)
try:
    print C7.impedanceEng(f3)
except ValueOutsideReasonableBounds:
    print "C7 capacitance, " + C7.capacitanceEng + ", is too high"
try:
    print C8.impedanceEng(f3)
except ValueOutsideReasonableBounds:
    print "C8 capacitance, " + C8.capacitanceEng + ", is too high"

print C9.impedanceEng(f3)
print C10.impedanceEng(f3)
print C11.impedanceEng(f3)
print C12.impedanceEng(f3)
try:
    print C13.impedanceEng(f3)
except ValueOutsideReasonableBounds:
    print "C13 capacitance, " + C13.capacitanceEng + ", is too high"
try:
    print C14.impedanceEng(f3)
except ValueOutsideReasonableBounds:
    print "C14 capacitance, " + C14.capacitanceEng + ", is too high"

print C15.impedanceEng(f3)
print C16.impedanceEng(f3)



# Parallel capacitor association
print "\n\n Parallel Association"
print capacitor.parallel(C1, C2)
print capacitor.parallel(C1, 30, 40, C2, 1)
print capacitor.parallel(C1, C1, C2, C2, 10**9)
print capacitor.parallel(1, 2)
print capacitor.parallel(1, 1, 1, 1, 1)
print capacitor.parallel(20000, 2, 2000, 20)
C38 = capacitor(2, "C38", 7)
print capacitor.parallel(1000000, 2)
print capacitor.parallel(1000000, C38)
print capacitor.parallel(1, 2)
print capacitor.parallel(1, 2, 3)
print capacitor.parallel(1, 2, 3, 4)

# Series capacitor association
print "\n\n Series Association"
print capacitor.series(C1, C2)
print capacitor.series(C1, 30, 40, C2, 1)
print capacitor.series(C1, C1, C2, C2, 10**9)
print capacitor.series(1, 2)
print capacitor.series(1, 1, 1, 1, 1)
print capacitor.series(20000, 2, 2000, 20)
C38 = capacitor(2, "C38", 7)
print capacitor.series(1000000, 2)
print capacitor.series(1000000, C38)
print capacitor.series(1, 2)
print capacitor.series(1, 2, 3)
print capacitor.series(1, 2, 3, 4)
print capacitor.series(1, 0.1, 0.01, 0.001)
C39 = capacitor(0.001, "$C_39$", 4)
print capacitor.series(1, 0.1, 0.01, C39)
print capacitor.series(1, 0.1, 0.01, 0.0001)
C40 = capacitor(0.0001, "$C_40$", 5)
print capacitor.series(1, 0.1, 0.01, C40)
print capacitor.series(1, 10, 100)
print capacitor.series(1, 10, 100, 1000)
print capacitor.series(10, 100, 1000)
print capacitor.series(100, 1000, 10000)
print capacitor.series(100, 1000, 100000)

C40 = capacitor(0.00121434, "$C_40$", 5)
C41 = capacitor(0.00121434, "$C_41$", 2)
print C40.capacitanceEng
print C41.capacitanceEng

# Making series return a capacitor
print('\n')
C42 = capacitor.series(100, 1000, 100000, capacitor=True)
print C42
print C42.digits
print C42.label
print C42.capacitance
print C42.capacitanceEng
C43 = capacitor(1213.1212, 'C43', 5)
C44 = capacitor.series(100, 1000, C43, capacitor=True)
print C44
print C44.digits
print C44.label
print C44.capacitance
print C44.capacitanceEng

# Voltage Divider
print "\n\n Voltage Divider"
print capacitor.voltageDivider(10, 2, 2, 100)
print capacitor.voltageDivider(10, 2, 2, 100*10**6)
print capacitor.voltageDivider(10, 2, 5, 100*10**6)
print capacitor.voltageDivider(10, 10000, 5, 100*10**6)

# Current Divider
print "\n\n Current Divider"
aux = capacitor.currentDivider(10, 200, 5, 87*10**3)
print aux
print engineerNotation(aux, capacitor.unit())
print capacitor.currentDivider(10, 2, 5, 10)
