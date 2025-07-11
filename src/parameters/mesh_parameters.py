from enum import Enum

class Nodes(Enum):
    """Enum for node types
    Current Types:
    - GLL
    - GL
    """
    GLL = "GLL" # Gauss-Lagrange-Labatto
    GL = "GL" # Gauss-Lagrange

class MeshParameters:
    """ Parameters for the mesh
    """
    def __init__(self):
        self.left_bound = -1
        self.right_bound = 1
        self.num_grid_elements_per_dim = 8
        self.dimension = 1
        self.flux_nodes = Nodes("GLL")
        self.solution_nodes = Nodes("GLL")
        self.mesh_file_name = ""

    def set_flux_nodes(self, flux_nodes: Nodes):
        self.flux_nodes = flux_nodes

    def set_solution_nodes(self, solution_nodes: Nodes):
        self.solution_nodes = solution_nodes

    def set_left_bound(self, left_bound: float):
        self.left_bound = left_bound

    def set_right_bound(self, right_bound: float):
        self.right_bound = right_bound

    def set_num_grid_elements_per_dim(self, num_grid_elements_per_dim: int):
        self.num_grid_elements_per_dim = num_grid_elements_per_dim

    def set_mesh_file_name(self, mesh_file_name: str):
        self.mesh_file_name = mesh_file_name

    def set_dimension(self, dimension: int):
        self.dimension = dimension

    def read_mesh_parameters(self, lines, line_index: int):
        line_index += 1
        while line_index < len(lines):
            line = lines[line_index].strip()
            if line == "end":
                break
            elif line.startswith("set"):
                key_value = line[4:].split("=")
                if len(key_value) == 2:
                    key, value  = key_value
                    self._store_parameter(key.strip(),value.strip())
            line_index += 1
        return line_index

    def _store_parameter(self, key, value):
        if key == "left_bound":
            self.set_left_bound(float(value))
        elif key == "right_bound":
            self.set_right_bound(float(value))
        elif key == "num_grid_elements_per_dim":
            self.set_num_grid_elements_per_dim(int(value))
        elif key == "mesh_file_name":
            self.set_mesh_file_name(value)
        elif key == "flux_nodes":
            self.set_flux_nodes(Nodes(value))
        elif key == "solution_nodes":
            self.set_solution_nodes(Nodes(value))
        elif key == "dimension":
            self.set_dimension(int(value))
        else:
            raise ValueError("Unknown key '%s'" % key)



