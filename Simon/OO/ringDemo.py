

from __future__ import print_function
from compartment import Compartment
from cmptSet import CmptSet
from subprocess import Popen, PIPE

tMax = 10.            # integration end time

# generate a ring of connected compartments
ringLength = 10
cmpts = [Compartment(1., 1., 1., 1., 1., 1., 1.) for i in range(ringLength)]
for i in range(ringLength):
    cmpts[i].addNeighbour(cmpts[(i + 1) % ringLength])

cmptRing = CmptSet(*cmpts)


# integration and output
with open("out/ringP.dat", "w+") as outputFileP:
    with open("out/ringQ.dat", "w+") as outputFileQ:
        t = Compartment.t0
        while t < tMax:
            t = cmptRing.integrate()
            # print to file
            print(" ".join([str(v) for v in cmptRing.getPvals()]), file=outputFileP)
            print(" ".join([str(v) for v in cmptRing.getQvals()]), file=outputFileQ)
            # print("{:f}\t{:f}\t{:f}".format(t, P1, Q2), file=outputFile)


# call gnuplot for plotting
Popen("gnuplot ringDemo.plt", shell=True, stdout=PIPE)
