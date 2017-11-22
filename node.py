'''
                     _
     _ __   ___   __| | ___   _ __  _   _
    | '_ \ / _ \ / _` |/ _ \ | '_ \| | | |
    | | | | (_) | (_| |  __/_| |_) | |_| |
    |_| |_|\___/ \__,_|\___(_) .__/ \__, |
                             |_|    |___/


'''
from ParamSchemDraw import *

class node(object):
    '''
        Class used to define a node in a circuit layout
    '''

    # Class parameters
    __LABEL = 1             # Node label counter
    __NODE_ID = 0           # Node ID counter
    __NODE_LABELS = []      # Array of used labels


    def __init__(self, label="", voltage=None, isgnd=False):
        assert isinstance(label, str), "The label element must be a string"

        # Assign node ID and increment node counter
        self._id = node.__NODE_ID
        node.__NODE_ID += 1

        # Assign node label. If a label isn't provided, auto-assign a label
        if not label:
            label = "V" + str(node.__LABEL)
            node.__LABEL += 1

            # check if label is already in use
            while label in node.__NODE_LABELS:
                label = "V" + str(node.__LABEL)
                node.__LABEL += 1

            self._label = label

        elif label not in node.__NODE_LABELS:
            self._label = label
        else:
            raise LabelAlreadyInUse

        # save label as in use
        node.__NODE_LABELS.append(label)


        # Empty mesh array
        self._mesh = []

        # Voltage in the node
        self._voltage = None

        # Define Node as ground
        self._isGND = isgnd


    '''
        GETTERS
    '''
    @property
    def id(self):
        return self._id

    @property
    def label(self):
        return self._label

    @property
    def mesh(self):
        return self._mesh

    '''
        SETTERS
    '''
    @label.setter
    def label(self, label):
        assert isinstance(label, str), "The label of the node must be a string"
        assert label, "The label cannot be empty"

        if label not in __NODE_LABELS:
            self._label = label
        else:
            raise LabelAlreadyInUse

    @mesh.setter
    def mesh(self, mesh_id):
        assert isinstance(mesh_id, int), "The mesh ID must be a integer"
        assert mesh_id >= 0, "The mesh ID must be positive"

        self._mesh.append(mesh_id)


    def remove_mesh_from_node(self, mesh_id):
        assert isinstance(mesh_id, int), "The mesh ID must be a integer"
        assert mesh_id in self._mesh, "The mesh ID must exist in the mesh list associated with the node"

        self._mesh.remove(mesh_id)

    @classmethod
    def isValidNodeID(node_id):
        '''
            An inode ID is valid if is a postive integer already assigned to a node in used
        '''

        if isinstance(node_id, int):
            if (node_id >= 0) and (node_id < __NODE_ID):
                return True
        return False

#    @staticmethod
#    def getNode(node_id)
