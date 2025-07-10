from enum import Enum

class Nodes(Enum):
    """Enum for node types
    Current Types:
    - GLL
    - GL
    """
    GLL = "Gauss-Lagrange-Labatto"
    GL = "Gauss-Lagrange"

class MeshParameters:
    """ Parameters for the mesh
    """
    def __init__(self):
        self.left_bound = 0
        self.right_bound = 0
        self.num_grid_elements_per_dim = 0
        self.flux_nodes = None
        self.solution_nodes = None
        self.mesh_file_name = ""

    def set_flux_nodes(self, flux_nodes: Nodes):
        self.flux_nodes = flux_nodes

    def set_solution_nodes(self, solution_nodes: Nodes):
        self.solution_nodes = solution_nodes

    def set_bounds(self, left_bound: float, right_bound: float):
        self.left_bound = left_bound
        self.right_bound = right_bound

    def set_num_grid_elements_per_dim(self, num_grid_elements_per_dim: int):
        self.num_grid_elements_per_dim = num_grid_elements_per_dim

    def set_mesh_file_name(self, mesh_file_name: str):
        self.mesh_file_name = mesh_file_name

    def read_mesh_parameters(self, file: str):
        return
