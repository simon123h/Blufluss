"""
Simulation eines simplen Blutkreislaufs des menschlichen Koerpers
"""


from __future__ import print_function
import os
from compartments import Herzkammer, Vorhof, Artery, TerminalVessel, CompartmentSet
from subprocess import Popen, PIPE

tIntegration = 4.0       # integration end time
tEinschwing = 10.
dt = 0.01                # time step size


# generate a ring of connected compartments
compartments = [
    Vorhof(
        C=0.0001,
        P1=10000.,
        P2=10000.,
        Q1=0.0,
        Q2=0.0
    ),
    Herzkammer(
        C=0.0000002,
        P1=10000.,
        P2=10000.,
        Q1=0.0,
        Q2=0.0
    ),
    Artery(
        R=1000000.,
        L=300.,
        C=0.0000001,
        P1=10000.,
        P2=10000.,
        Q1=0.0000,
        Q2=0.000
    ),
    TerminalVessel(
        R=1000000000.,
        C=0.0000001,
        P1=3000.,
        P2=3000.,
        Q1=0.0,
        Q2=0.0
    ),
    Artery(
        R=100000.,
        L=300.,
        C=0.0000001,
        P1=2000.,
        P2=2000.,
        Q1=0.0,
        Q2=0.0
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
if not os.path.exists('out'):
    os.makedirs('out')
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
