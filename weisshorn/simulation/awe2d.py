from simulation import Simulation

class Awe2D(Simulation):
    r"""Acoustic wave propagation in two dimensions


    """

    def __init__(self):

        self.type = 'acoustic'
        self.ndim = 2
    
    def cfl(self):

        pass
    
    def dispersion_check(self):

        pass
    

    def update_stress(self):

        pass

    def update_velocity(self):

        pass

    def inject_stress(self):

        pass

    def inject_velocity(self):

        pass