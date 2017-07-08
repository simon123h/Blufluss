from compartment import Compartment
import numpy as np
from heartPulse import dPulse_dt


# the heart, inherits from the Compartment class
class Heart(Compartment):
    # constructor
    def __init__(self, R, L, C, P1, P2, Q1, Q2):
        super(Heart, self).__init__(R=R, L=L, C=C, P1=P1, P2=P2, Q1=Q1, Q2=Q2)
        self.Qs = 0.005
        self.alpha = 0.0005
        self.y = [self.P1]
        self.r.set_initial_value(self.y, Compartment.t0)

    # Herzklappe
    @property
    def Q2(self):
        dicht = True
        if self.P1 - self.P2 < 0 and dicht:
            return 0
        else:
            return self.Qs * (np.exp(self.alpha * (self.P1 - self.P2)) - 1)

    # the rhs of terminal vessel, reduced form of the Compartment rhs
    def rhs(self, t, y):
        return [(self.Q1 - self.Q2) / self.C]


class Vorhof(Heart):
    # constructor
    def __init__(self,
                 R=500.,              # viscosity
                 L=1.,                # inertia
                 C=0.000005,         # compliance
                 P1=10000.,             # initial P1
                 P2=10000.,              # boundary P
                 Q1=0.000,            # boundary Q  0.3 mm/s
                 Q2=0.000             # initial Q2
                 ):
        super(Vorhof, self).__init__(R=R, L=L, C=C, P1=P1, P2=P2, Q1=Q1, Q2=Q2)
        self.Qs = 0.005
        self.alpha = 0.0005


class Herzkammer(Heart):
    # constructor
    def __init__(self,
                 R=500.,              # viscosity
                 L=300.,                # inertia
                 C=0.0000001,         # compliance, smaller than usual, otherwise heart wont pump
                 P1=15000.,             # initial P1
                 P2=15000.,              # boundary P
                 Q1=0.0000,            # boundary Q  0.3 mm/s
                 Q2=0.0000             # initial Q2
                 ):
        super(Herzkammer, self).__init__(R=R, L=L, C=C, P1=P1, P2=P2, Q1=Q1, Q2=Q2)
        self.amp = 50   # needed? how big is this factor?? TODO!
        self.Qs = 0.005
        self.alpha = 0.0005

    def rhs(self, t, y):
        return [(self.Q1 - self.Q2) / self.C + self.amp * dPulse_dt(t)]
