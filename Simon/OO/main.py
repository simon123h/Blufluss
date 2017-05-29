

from __future__ import print_function
from compartment import Compartment
from subprocess import Popen, PIPE


cpt1 = Compartment(1., 1., 1., 1., 1., 1., 1.)


# mathematical initial values
tMax = 10.            # integration end time

# implementation configuration
plotEvery = 1



# integration and output
with open("out/output.dat", "w+") as outputFile:
    print("t\tP1\tQ2", file=outputFile)
    t = Compartment.t0
    dt = Compartment.dt
    while t < tMax:
        t += dt
        P1, Q2 = cpt1.integrate()
        # print to file
        print("{:f}\t{:f}\t{:f}".format(t, P1, Q2), file=outputFile)


# call gnuplot for plotting
Popen("gnuplot plot.plt", shell=True, stdout=PIPE)
