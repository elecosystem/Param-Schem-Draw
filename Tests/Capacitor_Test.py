'''
    Test the capacitor output formatting

'''

# Add module path (parent folder)
import os, sys
sys.path.insert(0,os.path.pardir)

from capacitor import *

# Test assertions for invalid argument values
try:
    capacitor(0)
except InvalidCapacitor:
    print "Assertion caught for InvalidCapacitor. Capacitor value can't be zero"

try:
    capacitor(-34)
except InvalidCapacitor:
    print "Assertion caught for InvalidCapacitor. Capacitor value can't be negative"

try:
    capacitor(-2323213.232, "", 3)
except InvalidCapacitor:
    print "Assertion caught for InvalidCapacitor. Capacitor value can't be negative"

try:
    print capacitor(1.111111111111111111, "", 20)
except AssertionError:
    print "Assertion caught for required to high precision"

try:
    print capacitor(1.111111111111111111, "", 0)
except AssertionError:
    print "Assertion caught for required invalid precision"

try:
    print capacitor(1.111111111111111111, "", -2)
except AssertionError:
    print "Assertion caught for required invalid precision"

# Test for invalid arguments types
try:
    capacitor("cant be a string")
except InvalidCapacitor:
    print "Assertion caught for InvalidCesistor. Capacitor value can't be a string"

try:
    capacitor(1, 3)
except AssertionError:
    print "Assertion caught for AssertionError. label can't be a number"

try:
    capacitor("10", 3, "30")
except AssertionError:
    print "Assertion caught for AssertionError. digits can't be a number"

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

# susceptance
print("\n\nConductance")
print C0.susceptance
print C1.susceptance
print C2.susceptance
print C3.susceptance
print C4.susceptance
print C5.susceptance
print C6.susceptance
print C7.susceptance
print C8.susceptance
print C9.susceptance

# Formated Printing - Engeneering Notation and latex symbols
print("\n\nConductance Eng")
print C0.susceptanceEng
print C1.susceptanceEng
print C2.susceptanceEng
print C3.susceptanceEng
print C4.susceptanceEng
print C5.susceptanceEng
print C6.susceptanceEng
print C7.susceptanceEng
print C8.susceptanceEng
print C9.susceptanceEng


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

# Parallel capacitor association
print "\n\n"
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
print "\n\n"
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
print "\n\n"
print capacitor.voltageDivider(10, 2, 2, 100*10**6)
print capacitor.voltageDivider(10, 2, 5, 100*10**6)
print capacitor.voltageDivider(10, 10000, 5, 100*10**6)

# Current Divider
print "\n\n"
aux = capacitor.currentDivider(10, 200, 5, 87*10**3)
print aux
print engineerNotation(aux, capacitor.unit())
print capacitor.currentDivider(10, 2, 5, 10)
