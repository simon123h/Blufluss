

from __future__ import print_function
from compartment import Compartment
from newTerminalVessel import TerminalVessel
from artery import Artery
from heart import Heart
from cmptSet import CompartmentSet
from subprocess import Popen, PIPE

tMax = 20.              # integration end time
dt = 0.1                # time step size


tv = TerminalVessel()
t = Compartment.t0
while t < tMax:
    t += dt
    tv.integrate(t)
    print(tv.P1)

exit()

# generate a ring of connected compartments
cmpts = [Heart(), Artery(), TerminalVessel(), Artery()]
cmpts[0].addNeighbour(cmpts[1])
cmpts[1].addNeighbour(cmpts[2])
cmpts[2].addNeighbour(cmpts[3])
cmpts[3].addNeighbour(cmpts[0])

system = CompartmentSet(*cmpts)

# integration and output
with open("out/ringP.dat", "w+") as outputFileP:
    with open("out/ringQ.dat", "w+") as outputFileQ:
        t = Compartment.t0
        while t < tMax:
            t += dt
            system.integrate(t)
            # print to file
            print(" ".join([str(v) for v in system.getPvals()]), file=outputFileP)
            print(" ".join([str(v) for v in system.getQvals()]), file=outputFileQ)


# call gnuplot for plotting
Popen("gnuplot ringDemo.plt", shell=True, stdout=PIPE)
