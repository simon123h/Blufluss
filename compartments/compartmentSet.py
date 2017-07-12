"""
Class for a set of connected compartments.
The whole set can be integrated.
"""


class CompartmentSet(object):
    def __init__(self, *compartments):
        self.compartments = list(compartments)
        self.communicate()

    # add a new compartment
    def addCompartment(self, compartment):
        if compartment not in self.compartments:
            self.compartments += [compartment]

    # coherently integrate all compartments in the set
    def integrate(self, t):
        # integrate all compartments separately
        for cmpt in self.compartments:
            cmpt.integrate(t)
        # update each compartment bounds
        self.communicate()

    # update each compartments bounds from connected compartments
    def communicate(self):
        for cmpt in self.compartments:
            cmpt.communicate()

    # get P1 values of each compartment in the set
    @property
    def P1(self):
        return [c.P1 for c in self.compartments]

    # get P2 values of each compartment in the set
    @property
    def P2(self):
        return [c.P2 for c in self.compartments]

    # get Q1 values of each compartment in the set
    @property
    def Q1(self):
        return [c.Q1 for c in self.compartments]

    # get Q2 values of each compartment in the set
    @property
    def Q2(self):
        return [c.Q2 for c in self.compartments]
