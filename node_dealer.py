from node import *

__NODES = []

def add_node(label="", voltage=None, isgnd=False):
    temp_node = node(label, voltage, isgnd)
    __NODES.append(temp_node)
    return temp_node
    
def get_node(node_id):
    assert isValidNodeID, "The node ID is invalid"
    temp_node = None
    for k in range(0, len(__NODES)-1):
        if __NODES[k].id == node_id:
            temp_node = __NODES[k]

    return temp_node
