"""
Simulation eines simplen Blutkreislaufs des menschlichen Koerpers
"""


from __future__ import print_function
from compartments import Herzkammer, Vorhof, Artery, TerminalVessel, CompartmentSet
from subprocess import Popen, PIPE

tIntegration = 4.0       # integration end time
tEinschwing = 16.
dt = 0.01                # time step size


# generate a ring of connected compartments
compartments = [
    Vorhof(
        C=0.000005
    ),
    Herzkammer(
        C=0.0000001
    ),
    Artery(
        R=100000.,
        L=300.,
        C=0.0000001
    ),
    TerminalVessel(
        R=10000000.,
        C=0.0000001
    ),
    Artery(
        R=100000.,
        L=300.,
        C=0.0000001
    )
]

# connect as a ring
compartments[0].addNeighbour(compartments[1])
compartments[1].addNeighbour(compartments[2])
compartments[2].addNeighbour(compartments[3])
compartments[3].addNeighbour(compartments[4])
compartments[4].addNeighbour(compartments[0])
system = CompartmentSet(*compartments)

# integration and output
with open("out/humanP.dat", "w+") as outputFileP:
    with open("out/humanQ.dat", "w+") as outputFileQ:
        t = 0
        while t < tIntegration + tEinschwing:
            t += dt
            system.integrate(t)
            # print to file
            if t > tEinschwing:
                print(" ".join([str(v)
                                for v in system.P1]), file=outputFileP)
                print(" ".join([str(v)
                                for v in system.Q2]), file=outputFileQ)


# call gnuplot for plotting
labels = " ".join([c.label for c in system.compartments])
Popen("gnuplot -e \"labels='" + labels + "'\" plot.plt", shell=True, stdout=PIPE)
