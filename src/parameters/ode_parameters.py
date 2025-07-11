from enum import Enum

class OdeSolverType(Enum):
    runge_kutta = "runge_kutta"
    implicit = "implicit"

class RungeKuttaMethod(Enum):
    ssprk3 = "ssprk3"
    rk4 = "rk4"
    euler = "euler"

class OdeParameters:
    def __init__(self):
        self.ode_solver_type = OdeSolverType("runge_kutta")
        self.CFL = 0.5
        self.adaptive_time_step = False
        self.runge_kutta_method = RungeKuttaMethod("euler")

    def set_ode_solver_type(self, ode_solver_type: OdeSolverType):
        self.ode_solver_type = ode_solver_type

    def set_CFL(self, CFL: float):
        self.CFL = CFL

    def set_adaptive_time_step(self, adaptive_time_step: bool):
        self.adaptive_time_step = adaptive_time_step

    def set_runge_kutta_method(self, runge_kutta_method: RungeKuttaMethod):
        self.runge_kutta_method = runge_kutta_method

    def read_ode_parameters(self, lines, line_index: int):
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
        if key == "ode_solver_type":
            self.set_ode_solver_type(OdeSolverType(value))
        elif key == "CFL":
            self.set_CFL(float(value))
        elif key == "adaptive_time_step":
            self.set_adaptive_time_step(bool(value))
        elif key == "runge_kutta_method":
            self.set_runge_kutta_method(RungeKuttaMethod(value))
        else:
            raise ValueError("Unknown key '%s'" % key)