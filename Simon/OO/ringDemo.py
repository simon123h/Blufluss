

from __future__ import print_function
from compartment import Compartment
from cmptSet import CmptSet
from subprocess import Popen, PIPE

tMax = 20.              # integration end time
dt = 0.1                # time step size

# generate a ring of connected compartments
ringLength = 51
cmpts = [Compartment(R=1., L=1., C=1., P1=0., Q2=0.) for i in range(ringLength)]
for i in range(ringLength):
    cmpts[i].addNeighbour(cmpts[(i + 1) % ringLength])

# excitation in the middle
cmpts[24].setInitial(P1=0.7, Q2=0.)
cmpts[25].setInitial(P1=1., Q2=0.)
cmpts[26].setInitial(P1=0.7, Q2=0.)

cmptRing = CmptSet(*cmpts)

# integration and output
with open("out/ringP.dat", "w+") as outputFileP:
    with open("out/ringQ.dat", "w+") as outputFileQ:
        t = Compartment.t0
        while t < tMax:
            t += dt
            cmptRing.integrate(t)
            # print to file
            print(" ".join([str(v) for v in cmptRing.getPvals()]), file=outputFileP)
            print(" ".join([str(v) for v in cmptRing.getQvals()]), file=outputFileQ)


# call gnuplot for plotting
Popen("gnuplot ringDemo.plt", shell=True, stdout=PIPE)
