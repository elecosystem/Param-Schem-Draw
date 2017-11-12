import matplotlib
matplotlib.use('Agg')

#Documentation:  https://bitbucket.org/cdelker/schemdraw
import SchemDraw as schem
import SchemDraw.elements as e

# Import library to parametrize the used of SchemDraw
from ParamSchemDraw import electricComponent
from resistor import *
from vSource import *

# Image extension
extension = '.png'


from structure_dealer import *


class circuit(object):
    __NODE_NUM = 0
    __CURRENT_NODE = None

    def __init__(self, name):
        assert isinstance(name, str), "The name must be a string"
        assert name, "The name of the circuit must be a valid string"

        self._name = name

        circuit.__CURRENT_NODE = add_gnd_node()
        self._schematic = schem.Drawing()
        self._schematic.add( e.GND )

    def draw(self, show=False):
        self._schematic.draw(showplot=show)
        filename = self._name + extension
        self._schematic.save(filename)
        matplotlib.pyplot.close('all')

        return filename

    def add_component(self, component, direction="", reverse='False'):
        #assert isinstance(finish_node, (node, None)) , "The finish_node must be a valid node or be empty"
        temp_mesh = add_mesh()
        temp_node = node()
        end_node  = add_node(temp_node)
        print(type(temp_mesh))
        print(type(circuit.__CURRENT_NODE))
        print(type(end_node))
        link_mesh(circuit.__CURRENT_NODE, end_node, temp_mesh)
        circuit.__CURRENT_NODE = end_node

        add_component_to_mesh(temp_mesh, component)
        
        self._schematic.add(component.schematic(), d=direction, reverse=reverse, label=component.label)
