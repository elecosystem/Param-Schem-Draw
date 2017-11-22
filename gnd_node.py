'''
      ____ _   _ ____                    _
     / ___| \ | |  _ \   _ __   ___   __| | ___
    | |  _|  \| | | | | | '_ \ / _ \ / _` |/ _ \
    | |_| | |\  | |_| | | | | | (_) | (_| |  __/
     \____|_| \_|____/  |_| |_|\___/ \__,_|\___|

'''

from node import *
import SchemDraw.elements as e

class gnd_node(node):
    def __init__(self):
        # create the node using the parent class init
        gnd = super(gnd_node, self).__init__("GND", 0)

        # replace the Schematic icon for the ground
        super(gnd_node, self).__SCHEMATIC = e.GND
