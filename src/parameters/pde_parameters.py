from enum import Enum

class PDEType(Enum):
    Euler = "euler"
    Burgers = "burgers"
    Advection = "advection"

class CaseType(Enum):
    sin_wave = "sin_wave"
    cos_wave = "cos_wave"

class PdeParameters:
    """ Parameters for the PDE
    """

    def __init__(self):
        self.pde_type = PDEType("advection")
        self.case = CaseType("sin_wave")
        self.output_file_name = ""
        self.final_time = 1.0
        self.advection_wave_speed = 1.0

    def set_pde_type(self, pde_type: PDEType):
        self.pde_type = pde_type

    def set_case(self, case: CaseType):
        self.case = case

    def set_output_file(self, output_file_name: str):
        self.output_file_name = output_file_name

    def set_final_time(self, final_time: float):
        self.final_time = final_time

    def set_advection_wave_speed(self, advection_wave_speed: float):
        self.advection_wave_speed = advection_wave_speed

    def read_pde_parameters(self, lines, line_index: int):
        line_index += 1
        while line_index < len(lines):
            line = lines[line_index].strip()
            if line == "end":
                break
            elif line.startswith("set"):
                key_value = line[4:].split("=")
                if len(key_value) == 2:
                    key, value = key_value
                    self._store_parameter(key.strip(), value.strip())
            line_index += 1
        return line_index

    def _store_parameter(self, key, value):
        if key == "pde_type":
            self.set_pde_type(PDEType(value.lower()))
        elif key == "case":
            self.set_case(CaseType(value.lower()))
        elif key == "output_file":
            self.set_output_file(value)
        elif key == "final_time":
            self.set_final_time(value)
        elif key == "advection_wave_speed":
            self.set_advection_wave_speed(value)
        else:
            raise ValueError("Unknown key '%s'" % key)


