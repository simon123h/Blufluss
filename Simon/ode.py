from __future__ import print_function
from scipy.integrate import ode
from subprocess import Popen, PIPE


# physical inital values
R = 1.              # viscosity
L = 1.              # inertia
C = 1.              # compliance
Q1 = 1.             # boundary Q
Q2 = 1.             # initial Q2
P1 = 1.             # initial P1
P2 = 1.             # boundary P

# mathematical initial values
y0 = [P1, Q2]       # initial (pressure P, flow rate Q)
t0 = 0.             # integration start time
t1 = 20.            # integration end time
dt = 0.01           # time step


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
with open("out/output.dat", "w+") as outputFile:
    print("t\tP1\tQ2", file=outputFile)
    while r.successful() and r.t < t1:
        r.integrate(r.t + dt)
        # print to file
        print("{:f}\t{:f}\t{:f}".format(r.t, r.y[0], r.y[1]), file=outputFile)


# call gnuplot for plotting
Popen("gnuplot plot.plt", shell=True, stdout=PIPE)
