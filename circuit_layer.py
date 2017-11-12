import matplotlib
matplotlib.use('Agg')

#Documentation:  https://bitbucket.org/cdelker/schemdraw
import SchemDraw as schem
import SchemDraw.elements as e

# Import library to parametrize the used of SchemDraw
from ParamSchemDraw import electricComponent, resistor, vSource, iSource

# Image extension
extension = '.png'


from structure_dealer import *


class circuit(object):
    __NODE_NUM = 0
    __CURRENT_NODE = None

    def __init__(self, name):
        assert isinstance(name, str), "The name must be a string"
        assert not name, "The name of the circuit must be a valid string"

        self._name = name

        __CURRENT_NODE = add_gnd_node()

    def add_component(self, component):
        #assert isinstance(finish_node, (node, None)) , "The finish_node must be a valid node or be empty"
        temp_mesh = add_mesh()
        end_node  = add_node()
        link_mesh(__CURRENT_NODE, end_node, temp_mesh)
        __CURRENT_NODE = end_node

        add_component_to_mesh(temp_mesh, component)
