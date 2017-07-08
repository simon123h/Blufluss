"""
Simulation eines simplen Blutkreislaufs des menschlichen Koerpers
"""


from __future__ import print_function
from compartments import Herzkammer, Vorhof, Artery, TerminalVessel, CompartmentSet
from plotting import plot

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
t = 0
P1vals = []
Q2vals = []
while t < tIntegration + tEinschwing:
    t += dt
    system.integrate(t)
    # print to file
    if t > tEinschwing:
        P1vals.append(system.P1)
        Q2vals.append(system.Q2)

plot(P1vals, Q2vals)
