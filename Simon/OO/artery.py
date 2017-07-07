from compartment import Compartment


# a simple artery
class Artery(Compartment):
    # constructor
    def __init__(self,
                 R=1000000.,            # viscosity
                 L=3000.,               # inertia
                 C=0.00000001,          # compliance
                 P1=10000.,             # initial P1
                 P2=10000.,             # boundary P
                 Q1=0.0003,             # boundary Q  0.3 mm/s
                 Q2=0.0003              # initial Q2
                 ):
        # call parent constructor with default values
        super(Artery, self).__init__(R=R, L=L, C=C, P1=P1, P2=P2, Q1=Q1, Q2=Q2)
