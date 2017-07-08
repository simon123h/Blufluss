from compartment import Compartment


# a terminal compartment, such as a set of muscle arteries
class TerminalVessel(Compartment):
    label = "Muskel"

    # constructor
    def __init__(self,
                 R=10000000.,           # viscosity
                 L=300.,                  # inertia
                 C=0.0000001,          # compliance
                 P1=10000.,              # initial P1
                 P2=10000.,              # boundary P
                 Q1=0.000,             # boundary Q  0.3 mm/s
                 Q2=0.000              # initial Q2
                 ):
        # call parent constructor with default values
        super(TerminalVessel, self).__init__(
            R=R, L=L, C=C, P1=P1, P2=P2, Q1=Q1, Q2=Q2)
        self.y = [P1]
        self.r.set_initial_value(self.y, 0)

    # output flow is determined by Ohm's law (reduced form of the rhs)
    @property
    def Q2(self):
        return (self.P1 - self.P2) / self.R

    # the rhs of terminal vessel, reduced form of the Compartment rhs
    def rhs(self, t, y):
        return [(self.Q1 - self.Q2) / self.C]
