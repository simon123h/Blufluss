"""
Simulation eines simplen Blutkreislaufs des menschlichen Koerpers
"""


from __future__ import print_function
import os
from compartments import Vorhof, Artery, CompartmentSet, Herzkammer, TerminalVessel
from subprocess import Popen, PIPE

tIntegration = 4.0       # integration end time
tEinschwing = 2.
dt = 0.01                # time step size


# generate one heart to be connected to multiple cycles
theHeart = [
    Vorhof(),
    Herzkammer()
]
theHeart[0].addNeighbour(theHeart[1])

# create a list of blood circuits, each sharing the same heart
compartments = []
compartments += theHeart
numberOfCircuits = 2
for i in range(numberOfCircuits):
    # create a new circuit
    newCircuit = [
        Artery(),
        TerminalVessel(),
        Artery()
    ]
    # add to list of all compartments
    compartments += newCircuit

    # connect as a ring
    theHeart[1].addNeighbour(newCircuit[0])
    newCircuit[0].addNeighbour(newCircuit[1])
    newCircuit[1].addNeighbour(newCircuit[2])
    newCircuit[2].addNeighbour(theHeart[0])


system = CompartmentSet(*compartments)
subsystem = CompartmentSet(*(theHeart + newCircuit))


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
                                for v in subsystem.P1]), file=outputFileP)
                print(" ".join([str(v)
                                for v in subsystem.Q2]), file=outputFileQ)


# call gnuplot for plotting
labels = " ".join([c.label for c in subsystem.compartments])
Popen("gnuplot -e \"labels='" + labels + "'\" plot.plt", shell=True, stdout=PIPE)
