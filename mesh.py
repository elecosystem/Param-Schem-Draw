
from ParamSchemDraw import electricComponent

class mesh(object):

    # Mesh label and ID
    __LABEL = 1
    __MESH_ID = 0
    __MESH_LABELS = []

    def __init__(self, component=None, label="", current=None):
        #assert isinstance(component, (electricComponent, None)), "The component must be a valid component"
        assert isinstance(label, str), "The label element must be a string"


        # Asign mesh ID
        self._id = mesh.__MESH_ID
        mesh.__MESH_ID += 1

        # Assign mesh label. If label isn't specified, assign new label
        if not label:
            label = "I" + str(mesh.__LABEL)
            mesh.__LABEL += 1

            while label in mesh.__MESH_LABELS:
                label = "I" + str(mesh.__LABEL)
                mesh.__LABEL += 1
            self._label = label

        elif label not in mesh.__MESH_LABELS:
            self._label = label
        else:
            raise LabelAlreadyInUse

        mesh.__MESH_LABELS.append(label)

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
    def id(self):
        return self._id

    @property
    def label(self):
        return self._label

    @property
    def node(self):
        return self._node

    @property
    def start_node(self):
        return self._node[0]

    @property
    def end_node(self):
        return self._node[1]

    @property
    def component(self):
        return self._component

    @property
    def mesh_type(self):
        return self._mesh_type

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
        self.__node[mesh_node_id] = node_id

    @start_node.setter
    def start_node(self, node_id):
        self._node[0] = node_id
        #self.node(0, node_id)

    @end_node.setter
    def end_node(self, node_id):
        self._node[1] = node_id
        #self.node(1, node_id)

    @component.setter
    def component(self, component):
        print(type(component))
        print(isinstance(component, electricComponent))
        #assert isinstance(component, electricComponent), "Componente is not a valid electrical component"
        self._component = component

    @mesh_type.setter
    def mesh_type(self, mesh_type):
        assert isinstance(mesh_type, str), "The mesh type must be avalid string"
        self._mesh_type = mesh_type


    @classmethod
    def isValidMeshID(mesh_id):
        if isinstance(mesh_id, int):
            if mesh_id >= 0:
                return True
        return False

    def remove_node_from_mesh(self, mesh_node_id):
        assert isinstance(mesh_node_id, int), "The mesh ID must be a integer"
        assert mesh_node_id in [0, 1], "The node to set in the mesh must be 0 or 1"

        idx = self._mesh.index(mesh_node_id)
        self._mesh[idx] = None
