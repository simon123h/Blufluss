from __future__ import print_function
from scipy.integrate import ode


class Compartment(object):
    # mathematical configuration
    t0 = 0.             # integration start time
    t1 = 10.            # integration end time
    dt = 0.01           # time step

    def __init__(self):
        # physical inital values
        self.R = 1.              # viscosity
        self.L = 1.              # inertia
        self.C = 1.              # compliance
        self.Q1 = 1.             # boundary Q
        self.Q2 = 1.             # initial Q2
        self.P1 = 1.             # initial P1
        self.P2 = 1.             # boundary P
        self.y0 = [self.P1, self.Q2]       # initial (pressure P, flow rate Q)

    def setR(self, val):
        self.R = val

    def setL(self, val):
        self.L = val

    def setC(self, val):
        self.C = val


# implementation configuration
plotEvery = 1


# the rhs of the equation of the system
def rhs(t, y, R, L, C):
    P1 = y[0]
    Q2 = y[1]
    return [(Q1 - Q2) / C,
            (P1 - P2 - R * Q2) / L]


# integration configuration: dopri5 --> Runge-Kutta 4
r = ode(rhs).set_integrator('dopri5')
r.set_initial_value(y0, t0).set_f_params(R, L, C)

# integration and output
i = 0
with open("out/output.dat", "w+") as outputFile:
    print("t\tP1\tQ2", file=outputFile)
    while r.successful() and r.t < t1:
        r.integrate(r.t + dt)
        # print to file
        print("{:f}\t{:f}\t{:f}".format(r.t, r.y[0], r.y[1]), file=outputFile)
