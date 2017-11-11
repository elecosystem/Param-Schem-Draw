
from ParamSchemDraw import electricComponent

class mesh(object):

    # Mesh label and ID
    __LABEL = 1
    __MESH_ID = 0
    __MESH_LABELS = []

    def __init__(self, component, label="", current=None):
        assert isinstance(component, electricComponent), "The component must be a valid component"
        assert isinstance(label, str), "The label element must be a string"


        # Asign mesh ID
        self._id = __MESH_ID
        __MESH_ID += 1

        # Assign mesh label. If label isn't specified, assign new label
        if not label:
            label = "I" + __LABEL
            __LABEL += 1

            while label in __MESH_LABELS:
                label = "I" + __LABEL
                __LABEL += 1
            self._label = label

        elif label not in __MESH_LABELS:
            self._label = label
        else:
            raise LabelAlreadyInUse
        __MESH_LABELS.append(label)

        # Two element node array
        self._node = [None] * 2

        # Electrical Component Placeholder
        self._component = component
        self._mesh_type = type(component).__name__

        # Current in the node
        self._current = None

    '''
        GETTERS
    '''
    @property
    def label(self):
        return self._label

    @property
    def node(self):
        return self._node

    '''
        SETTERS
    '''
    @label.setter
    def label(self, label):
        assert isinstance(label, str), "The label of the mesh must be a string"
        assert label, "The label cannot be empty"

        if label not in __MESH_LABELS:
            self._label = label
        else:
            raise LabelAlreadyInUse

    @node.setter
    def node(self, mesh_node_id, node_id):
        assert isinstance(node_id, int), "The node ID must be a integer"
        assert node_id >= 0, "The node ID must be positive"
        assert isinstance(mesh_node_id, int), "The node ID must be a integer"
        assert mesh_node_id in [0, 1], "The node to set in the mesh must be 0 or 1"

        # Edit mesh association to nodes
        self._mesh[mesh_node_id] = node_id

        #if None not in self._node:

    def remove_node_from_mesh(self, mesh_node_id):
        assert isinstance(mesh_node_id, int), "The mesh ID must be a integer"
        assert mesh_node_id in [0, 1], "The node to set in the mesh must be 0 or 1"

        idx = self._mesh.index(mesh_node_id)
        self._mesh[idx] = None
