'''
    Test the electricComponent random values generator

'''
# Add module path (parent folder)
import os, sys
sys.path.insert(0,os.path.pardir)

from ParamSchemDraw import *

# Test assertions for invalid argument values
try:
    print electricComponent.elecRandom(0, 1)
except AssertionError:
    print "Assertion caught for begin equal to zero"
try:
    print electricComponent.elecRandom(-1, 1)
except AssertionError:
    print "Assertion caught for begin not positive"

try:
    print electricComponent.elecRandom(1, 0)
except AssertionError:
    print "Assertion caught for end equal to zero and lower than begin"
try:
    print electricComponent.elecRandom(1, -1)
except AssertionError:
    print "Assertion caught for end not positive and lower than begin"

try:
    print electricComponent.elecRandom(1, 0.3)
except AssertionError:
    print "Assertion caught for begin bigger than end"
try:
    print electricComponent.elecRandom(5, 1)
except AssertionError:
    print "Assertion caught for begin bigger than end"

try:
    print electricComponent.elecRandom(5, 10, 0)
except AssertionError:
    print "Assertion caught for step equal to zero"
try:
    print electricComponent.elecRandom(5, 10, -1)
except AssertionError:
    print "Assertion caught for step less than zero"
try:
    print electricComponent.elecRandom(5, 10, 100)
except AssertionError:
    print "Assertion caught for step bigger than interval"

try:
    print electricComponent.elecRandom(5, 10, 1, 100)
except ValueOutsideReasonableBounds:
    print "ValueOutsideReasonableBounds Exception caught for expArg bigger than reasonable values"
try:
    print electricComponent.elecRandom(5, 10, 1, -100)
except ValueOutsideReasonableBounds:
    print "ValueOutsideReasonableBounds Exception caught for expArg lower than reasonable values"

try:
    print electricComponent.elecRandom(5, 10, 1, 1.0)
except TypeError:
    print "TypeError caught for expArg beign a float"
try:
    print electricComponent.elecRandom(5, 10, 1, 'h')
except KeyError:
    print "TypeError caught for expArg beign a string not in the dictionary"


for k in range(1, 10):
    print electricComponent.elecRandom(1, 10, 1, 'm')

print "\n"
print electricComponent.elecRandom(0.7, 7.8, 0.01, 'G')
print electricComponent.elecRandom(1, 10, 1, 'K')
print electricComponent.elecRandom(1.1, 4.5, 0.9, '')
print electricComponent.elecRandom(500, 501, 0.1, 'm')
print electricComponent.elecRandom(2.35, 555, 1.3, 'u')
print electricComponent.elecRandom(1.01, 99, 0.9, 'n')
print electricComponent.elecRandom(1.0, 4.5, 0.9, 'p')


print "\n"
print engineerNotation(electricComponent.elecRandom(1.1, 4.5, 0.9, 4))
print engineerNotation(electricComponent.elecRandom(1, 5, 0.1, 'G'))
