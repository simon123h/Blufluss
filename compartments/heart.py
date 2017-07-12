
from __future__ import print_function
try:
    import numpy as np
except ImportError, e:
    raise ImportError("Module 'numpy' is not installed, type 'pip install numpy' to install it.")
from compartment import Compartment
from heartPulse import dPulse_dt


# the heart, inherits from the Compartment class
class Heart(Compartment):
    # constructor
    def __init__(self, R, L, C, P1, P2, Q1, Q2):
        super(Heart, self).__init__(R=R, L=L, C=C, P1=P1, P2=P2, Q1=Q1, Q2=Q2)
        self.alpha = 0.0005
        self.Qs = 0.005
        self.Qs = 1 / (self.alpha * self.R)
        self.y = [self.P1]
        self.r.set_initial_value(self.y, 0)

    # Herzklappe
    @property
    def Q2(self):
        ideal = True
        if not ideal:
            return self.Qs * (np.exp(self.alpha * (self.P1 - self.P2)) - 1)
        elif self.P1 - self.P2 < 0:
            return 0
        else:
            return self.Qs * (np.exp(self.alpha * (self.P1 - self.P2)) - 1)
            return (self.P1 - self.P2) / self.R

    # the rhs of terminal vessel, reduced form of the Compartment rhs
    def rhs(self, t, y):
        return [(self.Q1 - self.Q2) / self.C]


class Vorhof(Heart):
    label = "Vorhof"

    # constructor
    def __init__(self,
                 R=400000.,              # viscosity
                 L=1.,                # inertia
                 C=0.000005,         # compliance
                 P1=10000.,             # initial P1
                 P2=10000.,              # boundary P
                 Q1=0.000,            # boundary Q  0.3 mm/s
                 Q2=0.000             # initial Q2
                 ):
        super(Vorhof, self).__init__(R=R, L=L, C=C, P1=P1, P2=P2, Q1=Q1, Q2=Q2)


class Herzkammer(Heart):
    label = "-kammer"

    # constructor
    def __init__(self,
                 R=400000.,              # viscosity
                 L=300.,                # inertia
                 C=0.0000001,         # compliance, smaller than usual, otherwise heart wont pump
                 P1=15000.,             # initial P1
                 P2=15000.,              # boundary P
                 Q1=0.0000,            # boundary Q  0.3 mm/s
                 Q2=0.0000             # initial Q2
                 ):
        super(Herzkammer, self).__init__(
            R=R, L=L, C=C, P1=P1, P2=P2, Q1=Q1, Q2=Q2)
        self.amp = 60   # needed? how big is this factor?? TODO!

    def rhs(self, t, y):
        return [(self.Q1 - self.Q2) / self.C + self.amp * dPulse_dt(t)]
