from node import *
import SchemDraw.elements as e

class gnd_node(node):
    def __init__(self):
        gnd = super(gnd_node, self).__init__("GND", 0, True)
        super(gnd_node, self).__SCHEMATIC = e.GND
        __SCHEMATIC = e.GND
