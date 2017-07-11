
from __future__ import print_function
try:
    from scipy.integrate import ode
except ImportError, e:
    raise ImportError("Module 'scipy' is not installed, type 'pip install scipy' to install it.")


"""
Class for a single compartment. It contains all related
physical variables and the integration method. Also it provides
some functionality for interaction with neighboring compartments.
"""


class Compartment(object):
    # mathematical configuration
    integrator = "dopri5"
    nsteps = 500        # intermediate integration steps
    label = "Compartment"

    def __init__(self, R=0., L=0., C=0., P1=0., P2=0., Q1=0., Q2=0.):
        # physical property values
        self.R = R              # viscosity
        self.L = L              # inertia
        self.C = C              # compliance

        # initial values (pressure P, flow rate Q)
        # after integration, this vector is updated with new values
        # extract state variable data from this variable
        self.y = [P1, Q2]

        # boundary values (pressure P, flow rate Q)
        # if compartments are connected, these are overwritten
        # by neighboring P1 and Q2 variables
        self.Q1 = Q1             # boundary Q1
        self.P2 = P2             # boundary P2

        # integration configuration: dopri5 --> Runge-Kutta 4, nsteps: number
        # of intermediate steps
        self.r = ode(self.rhs).set_integrator(
            Compartment.integrator, nsteps=Compartment.nsteps)
        self.r.set_initial_value(self.y, 0)

        # to each end connected compartments
        self.neighbours1 = []
        self.neighbours2 = []

    # Setter
    # TODO: ersetze mit formel durch setDiameter...
    def setR(self, val):
        self.R = val

    def setL(self, val):
        self.L = val

    def setC(self, val):
        self.C = val

    def setBounds(self, Q1, P2):
        self.Q1 = Q1
        self.P2 = P2

    # if not connected already, add compartment to the list of neighbours
    # always connects to end #1 of self to end #2 of other
    def addNeighbour(self, other):
        if other not in self.neighbours1:
            self.neighbours1 += [other]
        if self not in other.neighbours2:
            other.neighbours2 += [self]
        self.communicate()
        other.communicate()

    # generate new boundary variables P2 and Q1 from connected compartments
    # TODO: passt das so gut fuer Verzweigungen?
    # TODO: ggf. eigene Connector-Klasse fuer besondere Verzweigungen
    def communicate(self):
        if len(self.neighbours1) != 0:
            # ueber Druecke mitteln
            self.P2 = sum([n.P1 for n in self.neighbours1]) / float(len(self.neighbours1))
        if len(self.neighbours2) != 0:
            self.Q1 = sum([n.Q2 / float(len(n.neighbours1)) for n in self.neighbours2])

    # time variable
    @property
    def t(self):
        return self.r.t

    @property
    def P1(self):
        return self.y[0]

    @property
    def Q2(self):
        return self.y[1]

    # the rhs of the equation of the single compartment system
    def rhs(self, t, y):
        P1 = y[0]
        Q2 = y[1]
        return [(self.Q1 - Q2) / self.C,
                (P1 - self.P2 - self.R * Q2) / self.L]

    # integrate this single compartment up to time t with an arbitrary
    #  number of RK4 steps. returns the integration variables P1 and Q2
    def integrate(self, t):
        self.r.integrate(t)
        self.y = self.r.y
        # set end of integration as new initial values
        self.r = ode(self.rhs).set_integrator(
            Compartment.integrator, nsteps=Compartment.nsteps)
        self.r.set_initial_value(self.y, t)
        return self.P1, self.Q2
