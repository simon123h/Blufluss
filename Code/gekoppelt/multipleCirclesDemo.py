"""
Simulation eines simplen Blutkreislaufs des menschlichen Koerpers
"""


from __future__ import print_function
from compartments import Vorhof, Artery, CompartmentSet, Herzkammer
from subprocess import Popen, PIPE

tIntegration = 4.0       # integration end time
tEinschwing = 10.
dt = 0.01                # time step size


# generate one heart to be connected to multiple cycles
theHeart = [
    Vorhof(),
    Herzkammer()
]

# create a list of blood circuits, each sharing the same heart
circuits = []
numberOfCircuits = 2
for i in range(numberOfCircuits):
    # create a new circuit
    compartments = theHeart + [
        Artery(),
        Artery(),
        Artery()
    ]

    # connect as a ring
    compartments[0].addNeighbour(compartments[1])
    compartments[1].addNeighbour(compartments[2])
    compartments[2].addNeighbour(compartments[3])
    compartments[3].addNeighbour(compartments[4])
    compartments[4].addNeighbour(compartments[0])
    # append it to the list of circuits
    circuits.append(CompartmentSet(*compartments))


# integration and output
with open("out/humanP.dat", "w+") as outputFileP:
    with open("out/humanQ.dat", "w+") as outputFileQ:
        t = 0
        while t < tIntegration + tEinschwing:
            t += dt
            for system in circuits:
                system.integrate(t)
            # print to file
            if t > tEinschwing:
                print(" ".join([str(v)
                                for v in circuits[0].P1]), file=outputFileP)
                print(" ".join([str(v)
                                for v in circuits[0].Q2]), file=outputFileQ)


# call gnuplot for plotting
labels = " ".join([c.label for c in circuits[0].compartments])
Popen("gnuplot -e \"labels='" + labels + "'\" plotSet.plt", shell=True, stdout=PIPE)
