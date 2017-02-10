'''
    Test the electricComponent random values generator

'''
# Add module path (parent folder)
import os, sys
sys.path.insert(0,os.path.pardir)

from ParamSchemDraw import electricComponent

for k in range(1, 10):
    print "Very Low Random [Integer] (1 - 100 with steps of 1): " + str(electricComponent.ultraLowUniformRandom())
    print "Very Low Random [Integer] (100 - 500 with steps of 10): " + str(electricComponent.veryLowUniformRandom())
    print "Low Random [Integer] (500 - 1000 with steps of 50): " + str(electricComponent.lowUniformRandom())
    print "Middle Random [Integer] (1000 - 10K with steps of 100): " + str(electricComponent.middleUniformRandom())
    print "High Random [Integer] (10K - 100K with steps of 1K): " + str(electricComponent.highUniformRandom())
    print "Very High Random [Integer] (100K - 1M with steps of 10K): " + str(electricComponent.veryHighUniformRandom())
    print "Ultra Low Random [Integer] (1M - 100M with steps of 1M): " + str(electricComponent.ultraHighUniformRandom())
    print "\n"
