from compartment import Compartment


# a simple artery
class Artery(Compartment):
    label = "Arterie"
    # constructor
    def __init__(self,
                 R=100000.,            # viscosity
                 L=300.,               # inertia
                 C=0.0000005,          # compliance
                 P1=10000.,             # initial P1
                 P2=10000.,             # boundary P
                 Q1=0.000,             # boundary Q  0.3 mm/s
                 Q2=0.000              # initial Q2
                 ):
        # call parent constructor with default values
        super(Artery, self).__init__(R=R, L=L, C=C, P1=P1, P2=P2, Q1=Q1, Q2=Q2)
