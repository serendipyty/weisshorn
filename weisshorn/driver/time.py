from weisshorn.parameters.parameter import Parameter
from weisshorn.simulations import simulation
# from weisshorn.simulations.simulation import Simulation

__all__ = ['TimeStepping']

class TimeStepping():

    def __init__(self, parameters: Parameter=None):

        self._parameters = parameters

        self._simulation = simulation.Simulation().MakeSimulation(scheme='ACOUSTIC_2D', parameters = self._parameters)


    def go(self, parameters: Parameter=None):

        print('Go!')
        return 0