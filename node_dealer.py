'''
                     _            _            _
     _ __   ___   __| | ___    __| | ___  __ _| | ___ _ __
    | '_ \ / _ \ / _` |/ _ \  / _` |/ _ \/ _` | |/ _ \ '__|
    | | | | (_) | (_| |  __/ | (_| |  __/ (_| | |  __/ |
    |_| |_|\___/ \__,_|\___|  \__,_|\___|\__,_|_|\___|_|




    A set of functions to manipulate the node class and respective data structure

'''

from node import *
from gnd_node import *

# List of all the node in use
__NODES = []

def add_node(new_node):
    '''
        Add a new node to the circuit
    '''

    temp_node = new_node #node(label, voltage, isgnd)
    __NODES.append(temp_node)
    return temp_node

def get_node(node_id):
    '''
        Get a node from all the nodes in the circuit
    '''
    assert isValidNodeID(node_id), "The node ID is invalid!"
    temp_node = None
    for k in range(0, len(__NODES)-1):
        if __NODES[k].id == node_id:
            temp_node = __NODES[k]

    return temp_node
