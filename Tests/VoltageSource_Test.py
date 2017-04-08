'''
    Test the vSource output formatting

'''
# Add module path (parent folder)
import os, sys
sys.path.insert(0,os.path.pardir)

from vSource import *

# Test assertions for invalid argument values
try:
    vSource(0)  
except InvalidIndepentSource:
    print "Assertion caught for InvalidIndepentSource. vSource value can't be zero"

try:
    vSource(-34)
except InvalidIndepentSource:
    print "There should be no assertion"
finally:
    print "No assertion is generated. source values can be negative"

try:
    print vSource(1.111111111111111111, "", 20)
except AssertionError:
    print "Assertion caught for required to high precision"

try:
    print vSource(1.111111111111111111, "", 0)
except AssertionError:
    print "Assertion caught for required invalid precision"

try:
    print vSource(1.111111111111111111, "", -2)
except AssertionError:
    print "Assertion caught for required invalid precision"

# Test for invalid arguments types
try:
    vSource("cant be a string")
except InvalidIndepentSource:
    print "Assertion caught for InvalidIndepentSource. source value can't be a string"

try:
    vSource(1, 3)
except AssertionError:
    print "Assertion caught for AssertionError. label can't be a number"

try:
    vSource("10", 3, "30")
except AssertionError:
    print "Assertion caught for AssertionError. digits can't be a number"

# voltage Source testing examples
V0  = vSource(1)
V1  = vSource(10)
V2  = vSource(100)
V3  = vSource(1000)
V4  = vSource(10000)
V5  = vSource(100000)
V6  = vSource(1000000)
V7  = vSource(10000000)
V8  = vSource(100000000)
V9  = vSource(999)
V10 = vSource(9999)
V11 = vSource(6512)
V12 = vSource(10345)
V13 = vSource(1000000003)
V14 = vSource(10000045)
V15 = vSource(0.1)
V16 = vSource(0.01)
V17 = vSource(0.001)
V18 = vSource(0.0001)
V19 = vSource(0.00001)
V20 = vSource(0.000001)
V21 = vSource(0.000231)
V22 = vSource(0.234)
V23 = vSource(0.001234)
V24 = vSource(0.000120)
V25 = vSource(0.99999)
V26 = vSource(0.00999)
V27 = vSource(0.009)
V28 = vSource(0.999999999)
V29 = vSource(0.9200001)
V30 = vSource(0.000001)
V31 = vSource(0.192817)
V32 = vSource(0.6512)
V33 = vSource(0.06512)
V34 = vSource(0.006512)
V35 = vSource(0.0006512)
V36 = vSource(0.009999)
V37 = vSource(0.0009999)

# Raw printing
print V0.voltage
print V1.voltage
print V2.voltage
print V3.voltage
print V4.voltage
print V5.voltage
print V6.voltage
print V7.voltage
print V8.voltage
print V9.voltage
print V10.voltage
print V11.voltage
print V12.voltage
print V13.voltage
print V14.voltage
print V15.voltage
print V16.voltage
print V17.voltage
print V18.voltage
print V19.voltage
print V20.voltage
print V21.voltage
print V22.voltage
print V23.voltage
print V24.voltage
print V25.voltage
print V26.voltage
print V27.voltage
print V28.voltage
print V29.voltage
print V30.voltage
print V31.voltage
print V32.voltage
print V33.voltage
print V34.voltage
print V35.voltage
print V36.voltage
print V37.voltage

# The printing must be formatted with Engeneering Notation and latex symbols
print V0.voltageEng
print V1.voltageEng
print V2.voltageEng
print V3.voltageEng
print V4.voltageEng
print V5.voltageEng
print V6.voltageEng
print V7.voltageEng
print V8.voltageEng
print V9.voltageEng
print V10.voltageEng
print V11.voltageEng
print V12.voltageEng
print V13.voltageEng
print V14.voltageEng
print V15.voltageEng
print V17.voltageEng
print V16.voltageEng
print V18.voltageEng
print V20.voltageEng
print V19.voltageEng
print V21.voltageEng
print V22.voltageEng
print V24.voltageEng
print V25.voltageEng
print V23.voltageEng
print V26.voltageEng
print V27.voltageEng
print V28.voltageEng
print V29.voltageEng
print V30.voltageEng
print V31.voltageEng
print V32.voltageEng
print V33.voltageEng
print V34.voltageEng
print V35.voltageEng
print V36.voltageEng
print V37.voltageEng
