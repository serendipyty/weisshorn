import numba

from simulation import Simulation
from parameter.parameter import Parameters

import dask.array as da

from main import DTYPE

class Awe2D(Simulation):
    r"""Acoustic wave propagation in two dimensions


    """

    def __init__(self, parameters: Parameters=None):

        self.type = 'acoustic'
        self.ndim = 2
        self.nx, self.nz = nx, nz

        self._sxx = da.zeros((nx, nz), dtype=DTYPE)
        self._vx = da.zeros_like(self._sxx)
        self._vz = da.zeros_like(self._sxx)
    
    def cfl(self):

        pass
    
    def dispersion_check(self):

        pass

    @numba.guvectorize(
        [(numba.int8[:, :], numba.int8[:, :])],
        '(n, m) -> (n, m)'
    )
    def update_stress(self):

        pass

    def update_velocity(self):

        pass

    def inject_stress(self):

        pass

    def inject_velocity(self):

        pass