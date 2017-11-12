
from node_dealer import *

from mesh_dealer import *

def add_gnd_node():
    gnd = node("GND", 0, True);
    add_node(gnd)
    return gnd

def link_mesh(start_node, end_node, unlinked_mesh):
    unlinked_mesh.start_node = start_node
    unlinked_mesh.end_node = end_node
