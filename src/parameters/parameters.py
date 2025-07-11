from src.parameters.mesh_parameters import MeshParameters
from src.parameters.pde_parameters import PdeParameters
from src.parameters.dg_parameters import DgParameters
from src.parameters.ode_parameters import OdeParameters
import os

class Parameters:
    def __init__(self):
        self.mesh_parameters = MeshParameters()
        self.dg_parameters = DgParameters()
        self.ode_parameters = OdeParameters()
        self.pde_parameters = PdeParameters()

    def read_parameters(self, file_path: str):
        files = [f for f in os.listdir(file_path) if os.path.isfile(os.path.join(file_path,f)) and os.path.splitext(f)[1] == ".prm"]
        if len(files) > 1:
            raise Exception(f"Multiple .prm files found in {file_path}")
        if len(files) == 0:
            raise Exception(f"No .prm files found in {file_path}")
        with open(os.path.join(file_path,files[0]), 'r') as param_file:
            lines  = param_file.readlines()
            line_idx = 0
            while line_idx < len(lines):
                line = lines[line_idx].strip()
                if "subsection" in line:
                    if "mesh" in line:
                        line_idx += self.mesh_parameters.read_mesh_parameters(lines, line_idx)
                    elif "dg" in line:
                        line_idx += self.dg_parameters.read_dg_parameters(lines, line_idx)
                    elif "ode" in line:
                        line_idx += self.ode_parameters.read_ode_parameters(lines, line_idx)
                    elif "pde" in line:
                        line_idx += self.pde_parameters.read_pde_parameters(lines, line_idx)
                line_idx += 1
