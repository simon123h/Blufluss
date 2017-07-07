

from __future__ import print_function
from compartment import Compartment
from terminalVessel import TerminalVessel
from artery import Artery
from heart import Herzkammer, Vorhof
from cmptSet import CompartmentSet
from subprocess import Popen, PIPE

tIntegration = 3.0       # integration end time
tEinschwing = 10.
dt = 0.01                # time step size


# generate a ring of connected compartments
compartments = [
    Vorhof(
        R=100.,
        L=1.,
        C=0.001,
        P1=800.,
        P2=800.,
        Q1=0.0003,
        Q2=0.0003
    ),
    Herzkammer(
        R=100.,
        L=1.,
        C=0.001,
        P1=800.,
        P2=800.,
        Q1=0.0003,
        Q2=0.0003
    ),
    Artery(
        R=1000000.,
        L=3000.,
        C=0.00000001,
        P1=10000.,
        P2=10000.,
        Q1=0.0003,
        Q2=0.0003
    ),
    TerminalVessel(
        R=10000000.,
        L=1.,
        C=0.00000004,
        P1=2500.,
        P2=2500.,
        Q1=0.0003,
        Q2=0.0003
    ),
    Artery(
        R=1000000.,
        L=3000.,
        C=0.00000001,
        P1=10000.,
        P2=10000.,
        Q1=0.0003,
        Q2=0.0003
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
        t = Compartment.t0
        while t < tIntegration + tEinschwing:
            t += dt
            system.integrate(t)
            # print to file
            if t > tEinschwing:
                print(" ".join([str(v)
                                for v in system.getPvals()]), file=outputFileP)
                print(" ".join([str(v)
                                for v in system.getQvals()]), file=outputFileQ)


# call gnuplot for plotting
Popen("gnuplot humanDemo.plt", shell=True, stdout=PIPE)
