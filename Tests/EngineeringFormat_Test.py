'''
    Test the Enginnering output formatting

'''
# Add module path (parent folder)
import os, sys
sys.path.insert(0,os.path.pardir)

import ParamSchemDraw

# Test assertions for invalid argument values
try:
    ParamSchemDraw.enginnerNotation(0.23362323, "", -1)
except AssertionError:
    print "Assertion caught for p={}".format(-1)

try:
    ParamSchemDraw.enginnerNotation(0.23362323, "", 0)
except AssertionError:
    print "Assertion caught for p={}".format(0)

try:
    print ParamSchemDraw.enginnerNotation(1.111111111111111111, "", 20)
except AssertionError:
    print "Assertion caught for p={}".format(20)

# Test for invalid arguments types
try:
    print ParamSchemDraw.enginnerNotation("cant be a string", "", 3)
except AssertionError:
    print "Assertion caught if value is a string"

try:
    print ParamSchemDraw.enginnerNotation(2323114, "", "must be a integer")
except AssertionError:
    print "Assertion caught if p is a string"

try:
    print ParamSchemDraw.enginnerNotation(2323114, "", 3.4)
except AssertionError:
    print "Assertion caught if p is a float"

try:
    print ParamSchemDraw.enginnerNotation(2323114, 4, 3)
except AssertionError:
    print "Assertion caught if units is not a string"


# Test various values of numbers for different precisions
for p in range(1, 7, 1):
    print "P = {}".format(p)
    print ParamSchemDraw.enginnerNotation(0.23362323, "", p)
    print ParamSchemDraw.enginnerNotation(2.378973, "", p)
    print ParamSchemDraw.enginnerNotation(2323.32313, "V", p)
    print ParamSchemDraw.enginnerNotation(233.213123, "A", p)
    print ParamSchemDraw.enginnerNotation(0.230123123, "$\omega$", p)
    print ParamSchemDraw.enginnerNotation(2.3023123, "$\omega$", p)
    print ParamSchemDraw.enginnerNotation(23.02312312, "A", p)
    print ParamSchemDraw.enginnerNotation(230.213123123, "A", p)
    print ParamSchemDraw.enginnerNotation(1.111111111, "V", p)
    print ParamSchemDraw.enginnerNotation(-23.02312312, "V", p)
    print ParamSchemDraw.enginnerNotation(-230.213123123, "V", p)
    print ParamSchemDraw.enginnerNotation(-1.111111111, "$\omega$", p)
    print ParamSchemDraw.enginnerNotation(1234567890.1234565, "$\omega$", p)
    print ParamSchemDraw.enginnerNotation(-1234567890.1234565, "", p)
    print ParamSchemDraw.enginnerNotation(0, "", p)
    print ParamSchemDraw.enginnerNotation(-0, "", p)
    print "\n"


