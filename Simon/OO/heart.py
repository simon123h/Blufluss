from compartment import Compartment
import numpy as np
from heartPulse import dPulse_dt

# the heart, inherits from the Compartment class
class Heart(Compartment):

    # constructor
    def __init__(self, R=0., L=0., C=0., P1=0., Q2=0., P2=0., Q1=0.):
        # physical inital values
        R = 800000.             # viscosity
        L = R                 # inertia
		self.V_max = 0.13   			#Liter
		self.V_min = 0.06			#Liter
		self.E = 300000				#Pacal, fuer Arterien 150000 (die Haelfte)
        C = 20./3/E*(V_max+V_min)/2            # compliance
        Q1 = 0.             # boundary Q  0.3 mm/s
        Q2 = 0.             # initial Q2
		self.Qs = 0.0003
		self.alpha = 0.002
        P1 = 2500.              # initial P1
        P2 = 2500.              # boundary P
        # call parent constructor with default values
        super(Heart, self).__init__(R=R, L=L, C=C, P1=P1, Q2=Q2, P2=P2, Q1=Q1)
        self.freq = 1.   # pulses per second
        self.amp = 0.01
        self.y = [P1]
        self.r.set_initial_value(self.y, Compartment.t0)


    # output flow is determined by Ohm's law (reduced form of the rhs)
    @property
    def Q2(self):
		return self.Qs*(np.exp(self.alpha*(self.P1-self.P2))-1)

    # the rhs of terminal vessel, reduced form of the Compartment rhs
    def rhs(self, t, y):
        return [1/self.C*(self.Q2)]

		

class Vorhof(Heart):
	pass
	

class Herzkammer(Heart):
	def rhs(self, t, y):
		return [1/self.C*(self.Q2) + dPulse_dt(t)]