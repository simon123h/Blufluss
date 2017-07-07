from compartment import Compartment
import numpy as np
from heartPulse import dPulse_dt

# the heart, inherits from the Compartment class


class Heart(Compartment):

    # constructor
    def __init__(self,
                 R=100.,            # viscosity
                 L=1.,               # inertia
                 C=0.001,          # compliance
                 P1=800.,             # initial P1
                 P2=800.,             # boundary P
                 Q2=0.0003,             # initial Q2
                 Q1=0.0003              # boundary Q  0.3 mm/s
                 ):
        self.V_max = 0.13  # Liter
        self.V_min = 0.06  # Liter
        self.E = 300000  # Pacal, fuer Arterien 150000 (die Haelfte)
        # C = 20. / 3 / self.E * (self.V_max + self.V_min) / 2            # compliance
        self.Qs = 0.0003
        self.alpha = 0.002
        # call parent constructor with default values
        super(Heart, self).__init__(R=R, L=L, C=C, P1=P1, Q2=Q2, P2=P2, Q1=Q1)
        self.y = [P1]
        self.r.set_initial_value(self.y, Compartment.t0)

    # output flow is determined by Ohm's law (reduced form of the rhs)
    @property
    def Q2(self):
        # if (self.P1 - self.P2) < 0:
        #     return 0
        return self.Qs * (np.exp(self.alpha * (self.P1 - self.P2)) - 1)


    # the rhs of terminal vessel, reduced form of the Compartment rhs
    def rhs(self, t, y):
        return [(self.Q1 - self.Q2) / self.C]


class Vorhof(Heart):

    # constructor
    def __init__(self, R=0., L=0., C=0., P1=0., Q2=0., P2=0., Q1=0.):
        # physical inital values
        self.V_max = 0.13  # Liter
        self.V_min = 0.06  # Liter
        self.E = 300000  # Pacal, fuer Arterien 150000 (die Haelfte)
        self.C = 0.001           # compliance
        Q1 = 0.0003             # boundary Q  0.3 mm/s
        Q2 = 0.0003             # initial Q2
        P1 = 2500.              # initial P1
        P2 = 2500.              # boundary P
        # call parent constructor with default values
        super(Vorhof, self).__init__(R=R, L=L, C=C, P1=P1, Q2=Q2, P2=P2, Q1=Q1)


class Herzkammer(Heart):
    def rhs(self, t, y):
        return [(self.Q1 - self.Q2) / self.C + dPulse_dt(t)]
