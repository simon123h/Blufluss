"""
Simulation eines simplen Blutkreislaufs des menschlichen Koerpers
"""


from __future__ import print_function
from compartments import Vorhof, Artery, CompartmentSet
from subprocess import Popen, PIPE

tIntegration = 1.0       # integration end time
tEinschwing = 0.
dt = 0.01                # time step size


# generate a line of connected compartments
compartments = [
    Artery(Q1=0.0003),          # eine Arterie mit einer Quelle links
    Artery(),
    Vorhof(C=Artery().C),       # eine Klappe ohne Vorhof Compliance
    Artery(),
    Artery()
]

# connect as a ring
compartments[0].addNeighbour(compartments[1])
compartments[1].addNeighbour(compartments[2])
compartments[2].addNeighbour(compartments[3])
compartments[3].addNeighbour(compartments[4])
# compartments[4].addNeighbour(compartments[0])
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
Popen("gnuplot -e \"labels='" + labels + "'\" plotSet.plt", shell=True, stdout=PIPE)
