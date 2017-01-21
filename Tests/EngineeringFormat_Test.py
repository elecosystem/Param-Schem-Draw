'''
    Test the Enginnering output formatting

'''
# Add module path (parent folder)
import os, sys
sys.path.insert(0,os.path.pardir)

import ParamSchemDraw

for p in range(1, 7, 1):
    print "P = {}".format(p)
    print ParamSchemDraw.enginnerNotation(0.23362323, "", p)
    print ParamSchemDraw.enginnerNotation(2.378973, "", p)
    print ParamSchemDraw.enginnerNotation(2323.32313, "", p)
    print ParamSchemDraw.enginnerNotation(233.213123, "", p)
    print ParamSchemDraw.enginnerNotation(0.230123123, "", p)
    print ParamSchemDraw.enginnerNotation(2.3023123, "", p)
    print ParamSchemDraw.enginnerNotation(23.02312312, "", p)
    print ParamSchemDraw.enginnerNotation(230.213123123, "", p)
    print "\n"
