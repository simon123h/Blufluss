from scipy.integrate import ode


class Compartment(object):
    # mathematical configuration
    t0 = 0.             # integration start time
    dt = 0.1           # time step
    integrator = "dopri5"

    def __init__(self, R=0., L=0., C=0., P1=0., Q2=0., P2=0., Q1=0.):
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

        # integration configuration: dopri5 --> Runge-Kutta 4
        self.r = ode(self.rhs).set_integrator(Compartment.integrator)
        self.r.set_initial_value(self.y, Compartment.t0)

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

    def setInitial(self, P1, Q2):
        self.y = [P1, Q2]
        self.r.set_initial_value(self.y, Compartment.t0)

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
    def communicate(self):
        if len(self.neighbours1) != 0:
            self.P2 = sum([n.P1 for n in self.neighbours1])
        if len(self.neighbours2) != 0:
            self.Q1 = sum([n.Q2 for n in self.neighbours2])

    # boolean integration status
    @property
    def successful(self):
        return self.r.successful()

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

    # integrate this single compartment for an arbitrary number of RK4 steps
    # returns the integration variables P1 and Q2
    def integrate(self, steps=1):
        i = 0
        while self.r.successful() and i < steps:
            self.r.integrate(self.r.t + Compartment.dt)
            i += 1
        self.y = self.r.y
        return self.t, self.P1, self.Q2
