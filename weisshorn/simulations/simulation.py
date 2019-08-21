# from weisshorn.simulations.awe2d import Awe2D
from weisshorn.parameters.parameter import Parameter

import numba

# import weisshorn.simulations.simulation as wss
# from weisshorn.simulations.simulation import Simulation
# from weisshorn.parameters.parameter import Parameter

import dask.array as da

# from weisshorn.weisshorn_guide import DTYPE
DTYPE = 'float8'

# simulations_dict = {
#     'ACOUSTIC_2D': Awe2D,
# }

# CIAONE = 'CIAONE'

__all__ = ['Simulation']

class Simulation():

    def __init__(self):
        pass

    def MakeSimulation(self, scheme: str='ACOUSTIC_2D', parameters: Parameter=None):

        return 0
        # return simulations_dict[scheme](parameters)

# import numba

# # import weisshorn.simulations.simulation as wss
# # from weisshorn.simulations.simulation import Simulation
# # from weisshorn.parameters.parameter import Parameter

# import dask.array as da

# from weisshorn.weisshorn_guide import DTYPE

# __all__ = ['Awe2D']

class Awe2D(Simulation):
    r"""Acoustic wave propagation in two dimensions


    """

    def __init__(self, parameters: Parameter=None):

        self._type = 'acoustic'
        self._ndim = 2
        self._nx, self._nz = parameters['number-of-cells'][0], parameters['number-of-cells'][1]

        self._sxx = da.zeros((self._nx, self._nz), dtype=DTYPE)
        self._vx = da.zeros_like(self._sxx)
        self._vz = da.zeros_like(self._sxx)
    
    def cfl(self):

        pass
    
    def dispersion_check(self):

        pass

    # @numba.guvectorize(
    #     [(numba.int8[:, :], numba.int8[:, :])],
    #     '(n, m) -> (n, m)'
    # )
    def update_stress(self):

        pass

    def update_velocity(self):

        pass

    def inject_stress(self):

        pass

    def inject_velocity(self):

        pass