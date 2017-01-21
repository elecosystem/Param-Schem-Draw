'''
    Test the Enginnering output formatting

'''
# Add module path (parent folder)
import os, sys
sys.path.insert(0,os.path.pardir)

import ParamSchemDraw
print ParamSchemDraw.enginnerNotation(0.233)
print "\n"
print ParamSchemDraw.enginnerNotation(2.33)
print "\n"
print ParamSchemDraw.enginnerNotation(23.3)
print "\n"
print ParamSchemDraw.enginnerNotation(233)
print "\n"
print "----------------------------------------"
print ParamSchemDraw.enginnerNotation(0.230)
print "\n"
print ParamSchemDraw.enginnerNotation(2.30)
print "\n"
print ParamSchemDraw.enginnerNotation(23.0)
print "\n"
print ParamSchemDraw.enginnerNotation(230)
print "\n"
