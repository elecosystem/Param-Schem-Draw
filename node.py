
from ParamSchemDraw import *

class node(object):

    # Node label counter, ID and array of used labels
    __LABEL = 1
    __NODE_ID = 0
    __NODE_LABELS = []

    def __init__(self, label="", voltage=None, isgnd=False):
        assert isinstance(label, str), "The label element must be a string"

        # Asign node ID
        self._id = __NODE_ID
        __NODE_ID += 1

        # Asign node label. If label isn't specified, assign new label
        if not label:
            label = "V" + __LABEL
            __LABEL += 1

            while label in __NODE_LABELS:
                label = "V" + __LABEL
                __LABEL += 1
            self._label = label

        elif label not in __NODE_LABELS:
            self._label = label
        else:
            raise LabelAlreadyInUse
        __NODE_LABELS.append(label)

        # Empty mesh array
        self._mesh = []

        # Voltage in the node
        self._voltage = None

        # Check if the Node is ground
        self._isGND = isgnd

    '''
        GETTERS
    '''
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

#    @staticmethod
#    def getNode(node_id)
