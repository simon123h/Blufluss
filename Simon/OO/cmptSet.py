"""
Class for a set of connected compartments.
The whole set can be integrated.
"""


class CompartmentSet(object):
    def __init__(self, *compartments):
        self.compartments = list(compartments)

    # add a new compartment
    def addCompartment(self, compartment):
        if compartment not in self.compartments:
            self.compartments += [compartment]

    # coherently integrate all compartments in the set
    def integrate(self, t, steps=1):
        # integrate all compartments separately
        for cmpt in self.compartments:
            cmpt.integrate(t, steps)
        # update each compartment bounds
        self.communicate()

    # update each compartments bounds from connected compartments
    def communicate(self):
        for cmpt in self.compartments:
            cmpt.communicate()

    # get Q values of each compartment in the set
    def getQvals(self):
        return [c.Q2 for c in self.compartments]

    # get P values of each compartment in the set
    def getPvals(self):
        return [c.P1 for c in self.compartments]
