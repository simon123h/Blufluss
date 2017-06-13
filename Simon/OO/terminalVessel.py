from compartment import Compartment


# a terminal compartment, such as a set of muscle arteries
class terminalVessel(Compartment):

    # constructor
    def __init__(self, R=0., L=0., C=0., P1=0., Q2=0., P2=0., Q1=0.):
        # physical inital values
        R = 8333333             # viscosity
        L = 0.0                 # inertia
        C = 1. / R              # compliance
        Q1 = 0.0003             # boundary Q  0.3 mm/s
        Q2 = 0.0003             # initial Q2
        P1 = 2500.              # initial P1
        P2 = 2500.              # boundary P
        # call parent constructor with default values
        super(terminalVessel, self).__init__(R=R, L=L, C=C, P1=P1, Q2=Q2, P2=P2, Q1=Q1)
        self.y = [self.P1]

    # reduced rhs of the equation of the terminal vessel
    def rhs(self, t, P1):
        return [(self.Q1 - self.Q2) / self.C]

    @property
    def Q2(self):
        return (self.P1 - self.P2) / self.R
