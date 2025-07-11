from enum import Enum

class FRParameter(Enum):
    cDG = "cDG"
    cPlus = "cPlus"
    cHu = "cHu"

class ConvNumFlux(Enum):
    none = "none"
    LF = "lax_friedrichs"

class FluxType(Enum):
    CH = "CH"

class DgParameters:
    """ Parameters for DG
    """
    def __init__(self):
        self.weak_form = False
        self.use_split_form = True
        self.flux_reconstruction = FRParameter("cDG")
        self.convective_numerical_flux = ConvNumFlux("none")
        self.two_point_flux_type = FluxType("CH")

    def set_weak_form(self, use_weak_form: bool):
        self.weak_form = use_weak_form

    def set_use_split_form(self, use_split_form: bool):
        self.use_split_form = use_split_form

    def set_flux_reconstruction(self, flux_reconstruction: FRParameter):
        self.flux_reconstruction = flux_reconstruction

    def set_convective_numerical_flux(self, convective_numerical_flux: ConvNumFlux):
        self.convective_numerical_flux = convective_numerical_flux

    def set_two_point_flux_type(self, two_point_flux_type: FluxType):
        self.two_point_flux_type = two_point_flux_type

    def read_dg_parameters(self, lines, line_index: int):
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
        if key == "use_weak_form":
            self.set_weak_form(bool(value))
        elif key == "use_split_form":
            self.set_use_split_form(bool(value))
        elif key == "flux_reconstruction":
            self.set_flux_reconstruction(FRParameter(value))
        elif key == "convective_numerical_flux":
            self.set_convective_numerical_flux(ConvNumFlux(value))
        elif key == "two_point_flux_type":
            self.set_two_point_flux_type(FluxType(value))
        else:
            raise ValueError("Unknown key '%s'" % key)


