from compartment import Compartment
from numpy import sin, cos, pi


# the heart %TODO implement
class Heart(Compartment):

    # constructor
    def __init__(self, R=0., L=0., C=0., P1=0., Q2=0., P2=0., Q1=0.):
        # physical inital values
        R = 800000.             # viscosity
        L = R                 # inertia
        C = 1. / R              # compliance
        Q1 = 0.             # boundary Q  0.3 mm/s
        Q2 = 0.             # initial Q2
        P1 = 2500.              # initial P1
        P2 = 2500.              # boundary P
        # call parent constructor with default values
        super(Heart, self).__init__(R=R, L=L, C=C, P1=P1, Q2=Q2, P2=P2, Q1=Q1)
        # non oscillatory part of the parameters
        self.R0 = self.R
        self.C0 = self.C
        self.L0 = self.L
        self.freq = 1.   # pulses per second
        self.amp = 0.01

    # same rhs as in Compartment class (unaltered), but modify the
    # diameter of the heart (and thus R, L, C) in each step
    def rhs(self, t, y):
        # self.R = self.R0 * (1. + self.amp * sin(self.freq * 2 * pi * self.t))
        # self.C = self.C0 * (1. + self.amp * cos(self.freq * 2 * pi * self.t))
        P1 = y[0] * (1. + self.amp * sin(self.freq * 2 * pi * self.t))
        Q2 = y[1]  # valve
        # self.Q1 = min(self.Q1, 0.)
        return [(self.Q1 - Q2) / self.C,
                (P1 - self.P2 - self.R * Q2) / self.L]
