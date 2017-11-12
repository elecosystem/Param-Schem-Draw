from mesh import *

__MESHES = []

def add_mesh(new_mesh):
    __MESHES.append(new_mesh)

def get_mesh(mesh_id):
    assert isValidMeshID, "The mesh ID is invalid"
    temp_mesh = None
    for k in range(0, len(__MESHES)-1):
        if __MESHES[k].id == mesh_id:
            temp_mesh = __MESHES[k]

    return temp_mesh

def add_component_to_mesh(mesh_object, component):
    mesh_object.component = component
    mesh_object.mesh_type = type(component).__name__
