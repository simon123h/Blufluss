

from __future__ import print_function
from compartment import Compartment
from subprocess import Popen, PIPE

# integration end time
tMax = 10.

cmpt = Compartment(1., 1., 1., 1., 1., 1., 1.)


# integration and output
with open("out/output.dat", "w+") as outputFile:
    print("t\tP1\tQ2", file=outputFile)
    t = Compartment.t0
    while t < tMax:
        t, P1, Q2 = cmpt.integrate()
        # print to file
        print("{:f}\t{:f}\t{:f}".format(t, P1, Q2), file=outputFile)


# call gnuplot for plotting
Popen("gnuplot singleDemo.plt", shell=True, stdout=PIPE)
