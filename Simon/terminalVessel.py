from __future__ import print_function
from subprocess import PIPE, Popen
from scipy.integrate import ode

# physical inital values
R = 10000              # viscosity
L = 0.1              # inertia
C = 1. / R              # compliance
Q1 = 0.003             # boundary Q  0.3 mm/s
Q2 = 0.003             # initial Q2
P1 = 13000.             # initial P1   13 kPa
P2 = 13000.             # boundary P

# mathematical initial values
t0 = 0.             # integration start time
t1 = 10.            # integration end time
dt = 0.01           # time step


# the rhs of the equation of the system
# taken from 10.80 / 10.81
def rhs(t, y, R, L, C):
    P1 = y[0]
    Q2 = y[1]
    return [(Q1 - Q2) / C,
            (P1 - P2 - R * Q2) / L]


# integration configuration: dopri5 --> Runge-Kutta 4
r = ode(rhs).set_integrator('dopri5')
r.set_initial_value([P1, Q2], t0).set_f_params(R, L, C)

# integration and output
with open("out/output.dat", "w+") as outputFile:
    # header line
    print("t\tP1\tQ2", file=outputFile)
    # integration loop
    while r.successful() and r.t < t1:
        r.integrate(r.t + dt)
        # print to file
        print("{:f}\t{:f}\t{:f}".format(r.t, r.y[0], r.y[1]), file=outputFile)


# call gnuplot for plotting
# not necessary, but convenient for instant plotting
Popen("gnuplot fancyPlot.plt", shell=True, stdout=PIPE)
