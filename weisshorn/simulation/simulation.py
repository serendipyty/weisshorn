from awe2d import Awe2D

simulations_dict = {
    'ACOUSTIC_2D': Awe2D,
}

class Simulation():

    def MakeSimulation(self, scheme: str='ACOUSTIC_2D'):

        return simulations_dict[scheme]