from compartment import Compartment
import numpy as np
from heartPulse import dPulse_dt


# the heart, inherits from the Compartment class
class Heart(Compartment):
    # constructor
    def __init__(self,
                 R=100.,            # viscosity
                 L=1.,              # inertia
                 C=0.001,           # compliance
                 P1=800.,           # initial P1
                 Q2=0.0003,         # initial Q2
                 P2=800.,           # boundary P
                 Q1=0.0003          # boundary Q  0.3 mm/s
                 ):
        self.Qs = 0.0003
        self.alpha = 0.002
        # call parent constructor with default values
        super(Heart, self).__init__(R=R, L=L, C=C, P1=P1, P2=P2, Q1=Q1, Q2=Q2)
        self.y = [P1]
        self.r.set_initial_value(self.y, Compartment.t0)

    # Herzklappe
    @property
    def Q2(self):
        return self.Qs * (np.exp(self.alpha * (self.P1 - self.P2)) - 1)

    # the rhs of terminal vessel, reduced form of the Compartment rhs
    def rhs(self, t, y):
        return [(self.Q1 - self.Q2) / self.C]


class Vorhof(Heart):
    # constructor
    def __init__(self,
                 R=100.,            # viscosity
                 L=1.,               # inertia
                 C=0.001,          # compliance
                 P1=800.,             # initial P1
                 Q2=0.0003,             # initial Q2
                 P2=800.,             # boundary P
                 Q1=0.0003              # boundary Q  0.3 mm/s
                 ):
        super(Vorhof, self).__init__(R=R, L=L, C=C, P1=P1, P2=P2, Q1=Q1, Q2=Q2)


class Herzkammer(Heart):
    # constructor
    def __init__(self,
                 R=100.,              # viscosity
                 L=1.,                # inertia
                 C=0.001,             # compliance
                 P1=800.,             # initial P1
                 P2=800.,             # boundary P
                 Q1=0.0003,           # boundary Q  0.3 mm/s
                 Q2=0.0003            # initial Q2
                 ):
        super(Herzkammer, self).__init__(R=R, L=L, C=C, P1=P1, P2=P2, Q1=Q1, Q2=Q2)

    def rhs(self, t, y):
        return [(self.Q1 - self.Q2) / self.C + dPulse_dt(t)]
