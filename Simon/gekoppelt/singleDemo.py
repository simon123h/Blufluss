

from __future__ import print_function
from compartment import Compartment
from subprocess import Popen, PIPE


tMax = 100.              # integration end time
dt = 0.1                # time step size

cmpt = Compartment(1., 1., 1., 1., 1., 1., 1.)
# cmpt = Compartment(233333., 1., 1. / 233333., 2500., 0.0001, 5000., 0.0006)

# integration and output
with open("out/output.dat", "w+") as outputFile:
    print("t\tP1\tQ2", file=outputFile)
    t = Compartment.t0
    while t < tMax:
        t += dt
        P1, Q2 = cmpt.integrate(t)
        # print to file
        print("{:f}\t{:f}\t{:f}".format(t, P1, Q2), file=outputFile)


# call gnuplot for plotting
Popen("gnuplot singleDemo.plt", shell=True, stdout=PIPE)
