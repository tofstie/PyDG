from src.parameters.mesh_parameters import MeshParameters
import os

class Parameters:
    def __init__(self):
        self.mesh_parameters = None
        self.dg_parameters = None
        self.ode_solver_parameters = None
        self.pde_parameters = None

    def read_parameters(self, file_path: str):
        files = [f for f in os.listdir(file_path) if os.path.isfile(os.path.join(file_path,f)) and os.path.splitext(f)[1] == ".prm"]
        if len(files) > 1:
            raise Exception(f"Multiple .prm files found in {file_path}")
        if len(files) == 0:
            raise Exception(f"No .prm files found in {file_path}")

        ## Read PDE Parameters
        ## Read ODE Parameters
        ## Read Mesh Parameters
        self.mesh_parameters = MeshParameters()
        self.mesh_parameters.read_mesh_parameters(files[0])
        ## Read DG Parameters



