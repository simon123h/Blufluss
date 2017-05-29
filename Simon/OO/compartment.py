from scipy.integrate import ode


class Compartment(object):
    # mathematical configuration
    t0 = 0.             # integration start time
    dt = 0.01           # time step
    integrator = "dopri5"

    def __init__(self, R=0., L=0., C=0., Q1=0., Q2=0., P1=0., P2=0.):
        # physical property values
        self.R = R              # viscosity
        self.L = L              # inertia
        self.C = C              # compliance

        # boundary values (pressure P, flow rate Q)
        self.Q1 = Q1             # boundary Q1
        self.P2 = P2             # boundary P2

        # initial values (pressure P, flow rate Q)
        self.y0 = [P1, Q2]

        # integration configuration: dopri5 --> Runge-Kutta 4
        self.r = ode(self.rhs).set_integrator(Compartment.integrator)
        self.r.set_initial_value(self.y0, Compartment.t0)

    # Setter
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

    # boolean integration status
    @property
    def successful(self):
        return self.r.successful()

    # time variable
    @property
    def t(self):
        return self.r.t

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
        self.y0 = [self.r.y[0], self.r.y[1]]
        return self.r.y[0], self.r.y[1]
