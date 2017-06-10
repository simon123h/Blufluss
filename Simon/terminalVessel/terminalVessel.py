from __future__ import print_function
from subprocess import PIPE, Popen
from scipy.integrate import ode

# physical inital values
R = 8333333              # viscosity
# L = 0.0              # inertia
C = 1. / 333333              # compliance
Q1 = 0.0003             # boundary Q  0.3 mm/s
Q2 = 0.0003             # initial Q2
P1 = 2500.             # initial P1   13 kPa
P2 = 2500.             # boundary P


# mathematical initial values
t0 = 0.             # integration start time
t1 = 10.            # integration end time
dt = 0.01           # time step


# reduced rhs of the equation of the system
# taken from 10.80 / 10.81
def rhs(t, P1):
    return [(Q1 - Q2) / C]


# integration configuration: dopri5 --> Runge-Kutta 4
r = ode(rhs).set_integrator('dopri5')
r.set_initial_value(P1, t0)

# integration and output
with open("./out/output.dat", "w+") as outputFile:
    # header line
    print("t\tP1\tQ2", file=outputFile)
    # integration loop
    while r.successful() and r.t < t1:
        r.integrate(r.t + dt)
        P1 = r.y[0]
        Q2 = (P1 - P2) / R
        # print to file
        print("{:f}\t{:f}\t{:f}".format(r.t, P1, Q2), file=outputFile)


# call gnuplot for plotting
# not necessary, but convenient for instant plotting
Popen("gnuplot ./plot.plt", shell=True, stdout=PIPE)
