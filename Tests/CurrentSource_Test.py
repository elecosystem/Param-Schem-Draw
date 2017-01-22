'''
    Test the iSource output formatting

'''
# Add module path (parent folder)
import os, sys
sys.path.insert(0,os.path.pardir)

from ParamSchemDraw import *

# Test assertions for invalid argument values
try:
    iSource(0)
except InvalidIndepentSource:
    print "Assertion caught for InvalidIndepentSource. iSource value can't be zero"

try:
    iSource(-34)
except InvalidIndepentSource:
    print "There should be no assertion"
finally:
    print "No assertion is generated. source values can be negative"

try:
    print iSource(1.111111111111111111, "", 20)
except AssertionError:
    print "Assertion caught for required to high precision"

try:
    print iSource(1.111111111111111111, "", 0)
except AssertionError:
    print "Assertion caught for required invalid precision"

try:
    print iSource(1.111111111111111111, "", -2)
except AssertionError:
    print "Assertion caught for required invalid precision"

# Test for invalid arguments types
try:
    iSource("cant be a string")
except InvalidIndepentSource:
    print "Assertion caught for InvalidIndepentSource. source value can't be a string"

try:
    iSource(1, 3)
except AssertionError:
    print "Assertion caught for AssertionError. label can't be a number"

try:
    iSource("10", 3, "30")
except AssertionError:
    print "Assertion caught for AssertionError. digits can't be a number"

# current Source testing examples
I0  = iSource(1)
I1  = iSource(10)
I2  = iSource(100, "", 3)
I3  = iSource(1000, "", 2)
I4  = iSource(10000, "", 4)
I5  = iSource(100000)
I6  = iSource(1000000)
I7  = iSource(10000000)
I8  = iSource(100000000)
I9  = iSource(999)
I10 = iSource(9999, "", 2)
I11 = iSource(6512)
I12 = iSource(10345, "", 2)
I13 = iSource(1000000003, "I13", 6)
I14 = iSource(10000045)
I15 = iSource(0.1)
I16 = iSource(0.01)
I17 = iSource(0.001)
I18 = iSource(0.0001)
I19 = iSource(0.00001)
I20 = iSource(0.000001)
I21 = iSource(0.000231)
I22 = iSource(0.234)
I23 = iSource(0.001234)
I24 = iSource(0.000120)
I25 = iSource(0.99999)
I26 = iSource(0.00999)
I27 = iSource(0.009)
I28 = iSource(0.999999999)
I29 = iSource(0.9200001)
I30 = iSource(0.000001)
I31 = iSource(0.192817)
I32 = iSource(0.6512)
I33 = iSource(0.06512)
I34 = iSource(0.006512)
I35 = iSource(0.0006512)
I36 = iSource(0.009999)
I37 = iSource(0.0009999)

# Raw printing
print I0.current
print I1.current
print I2.current
print I3.current
print I4.current
print I5.current
print I6.current
print I7.current
print I8.current
print I9.current
print I10.current
print I11.current
print I12.current
print I13.current
print I14.current
print I15.current
print I16.current
print I17.current
print I18.current
print I19.current
print I20.current
print I21.current
print I22.current
print I23.current
print I24.current
print I25.current
print I26.current
print I27.current
print I28.current
print I29.current
print I30.current
print I31.current
print I32.current
print I33.current
print I34.current
print I35.current
print I36.current
print I37.current

# The printing must be formatted with Engeneering Notation and latex symbols
print I0.currentEng
print I1.currentEng
print I2.currentEng
print I3.currentEng
print I4.currentEng
print I5.currentEng
print I6.currentEng
print I7.currentEng
print I8.currentEng
print I9.currentEng
print I10.currentEng
print I11.currentEng
print I12.currentEng
print I13.currentEng
print I14.currentEng
print I15.currentEng
print I17.currentEng
print I16.currentEng
print I18.currentEng
print I20.currentEng
print I19.currentEng
print I21.currentEng
print I22.currentEng
print I24.currentEng
print I25.currentEng
print I23.currentEng
print I26.currentEng
print I27.currentEng
print I28.currentEng
print I29.currentEng
print I30.currentEng
print I31.currentEng
print I32.currentEng
print I33.currentEng
print I34.currentEng
print I35.currentEng
print I36.currentEng
print I37.currentEng
